let buttons = document.querySelectorAll(".resp");

for (let button of buttons){
    button.addEventListener("click", function(event){
        button = event.target;
        if (button.innerHTML == "Correct!" || button.innerHTML == "Incorrect!"){
            return;
        }
        if (button.innerHTML == "c)Júpiter"){
            button.innerHTML = "Correct!";
            button.style.backgroundColor = "lightgreen";
            button.style.color = "green";
        }else{
            button.innerHTML = "Incorrect!";
            button.style.backgroundColor = "#F08080";
            button.style.color = "red";
        }
    })
}

document.getElementById("enviar").addEventListener("click", function(event){
    let elemento = document.getElementById("resposta");

    if (elemento.value == "Correct!" || elemento.value == "Incorrect!"){
        return;
    }
    if (elemento.value.toLowerCase() == "co2"){
        elemento.value = "Correct!";
        elemento.style.color = "green";
        elemento.style.backgroundColor = "lightgreen";
    }else{
        elemento.value = "Incorrect!";
        elemento.style.color = "red";
        elemento.style.backgroundColor = "#F08080";
    }
})
