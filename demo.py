# demo.py

def greet():
    print("Hello, World!")


def add_numbers(x, y):
    return x + y


def main():
    greet()
    a = 5
    b = 7
    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}")


# Run the main function
if __name__ == "__main__":
    main()
