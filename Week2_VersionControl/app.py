def greet(name):
    return "Hello, " + name + "!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Sum:", add(x, y))
    except:
        print("Please enter valid numbers.")
