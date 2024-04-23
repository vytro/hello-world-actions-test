import os

def hello():
    # print("Hello, World!")
    message = os.environ.get("A_VARIABLE", "World")
    print(f"Hello, {message}!")
    print(f"Se puede ver el secreto: {os.environ.get('A_VARIABLE', 'no hay')}")
    message2 = os.environ.get("B_VARIABLE", "World")
    print(f"Hello, {message2}!")

if __name__ == "__main__":
    hello()