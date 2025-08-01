def greet(name):
    return "Hello, " + name + "!"


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Sum:", add(x, y))
        print("Multiply:", mul(x, y))

    except ValueError:
        print("Please enter valid numbers.")
