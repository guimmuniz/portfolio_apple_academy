import os

from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    holdings = db.execute("SELECT symbol, SUM(CASE WHEN type = 'buy' THEN amount ELSE -amount END) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])

    portfolio = []
    grand_total = 0

    for holding in holdings:
        total_shares = holding["total_shares"]
        symbol = holding["symbol"]

        data = lookup(symbol)

        total = data["price"] * total_shares

        portfolio.append({
            "symbol": symbol,
            "enterprise": data["name"],
            "amount": total_shares,
            "price": data["price"],
            "total": total
            })

        grand_total += total

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    grand_total += cash[0]["cash"]

    return render_template("index.html", portfolio=portfolio, cash=cash[0]["cash"], grand_total=grand_total)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide a symbol", 400)

        amount = request.form.get("shares")
        if not amount or not amount.isdigit():
            return apology("give a valid number of shares", 400)
        amount = int(amount)
        if amount == 0:
            return apology("give a valid number of shares", 400)

        data = lookup(symbol)
        if data == None:
            return apology("symbol doesn't exists", 400)

        total = data["price"] * amount
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        if total > cash[0]["cash"]:
            return apology("you don't have enough money", 400)

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total, session["user_id"])

        db.execute("INSERT INTO transactions (user_id, type, amount, symbol, price, date) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], "buy", amount, symbol, data["price"], datetime.now())

        return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT symbol, type, amount, price, date FROM transactions WHERE user_id = ? ORDER BY date DESC", session["user_id"])

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 400)

        data = lookup(symbol)
        if data == None:
            return apology("symbol doesn't exist", 400)

        return render_template("quoted.html", data=data)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("must provide username", 400)

        password = request.form.get("password")
        if not password:
            return apology("must provide password", 400)

        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("must provide confirmation", 400)

        if confirmation != password:
            return apology("passwords don't match", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0:
            return apology("username already exists", 400)

        hash_password = generate_password_hash(password)
        id = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash_password)

        session["user_id"] = id

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        shares = request.form.get("shares")
        if not shares or not shares.isdigit():
            return apology("give a valid number of shares", 400)
        shares = int(shares)
        if shares == 0:
            return apology("give a valid number of shares", 400)

        buys = db.execute("SELECT SUM(amount) as total FROM transactions WHERE user_id = ? AND symbol = ? AND type = 'buy'", session["user_id"], symbol)
        sells = db.execute("SELECT SUM(amount) as total FROM transactions WHERE user_id = ? AND symbol = ? AND type = 'sell'", session["user_id"], symbol)

        total_buyed = buys[0]["total"] or 0
        total_sold = sells[0]["total"] or 0
        shares_owned = total_buyed - total_sold

        if shares > shares_owned:
            return apology("you don't have enough shares", 400)

        data = lookup(symbol)
        total = data["price"] * shares

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, type, amount, symbol, price, date) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], "sell", shares, symbol, data["price"], datetime.now())

        return redirect("/")
    else:
        symbols = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = ?", session["user_id"])

        owned = []

        for row in symbols:
            symbol = row["symbol"]

            buys = db.execute("SELECT SUM(amount) as total FROM transactions WHERE user_id = ? AND symbol = ? AND type = 'buy'", session["user_id"], symbol)
            sells = db.execute("SELECT SUM(amount) as total FROM transactions WHERE user_id = ? AND symbol = ? AND type = 'sell'", session["user_id"], symbol)

            total_buyed = buys[0]["total"] or 0
            total_sold = sells[0]["total"] or 0
            shares_owned = total_buyed - total_sold

            if shares_owned > 0:
                owned.append({"symbol": symbol.upper()})

        return render_template("sell.html", stocks=owned)
