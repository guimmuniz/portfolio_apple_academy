height = input("Height (1-8): ")

while not height.isdigit() or int(height)>8 or int(height)<1:
    height = input("Height (1-8): ")

height = int(height)

n = height - 1

for i in range(height):
    for k in range(n):
        print(" ", end="")

    for j in range(height - n):
        print("#", end="")

    print(" "*2, end="")
    for l in range(height - n):
        print("#", end="")
    n = n - 1
    print()
