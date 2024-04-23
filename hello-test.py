import os

def hello():
    # print("Hello, World!")
    message = os.environ.get("A_VARIABLE", "World")
    print(f"Hello, {message}!")
    print(f"Se puede ver el secreto: {os.environ.get('A_VARIABLE', 'no hay')}")
    print(f"Hello, {os.environ.get("B_VARIABLE", "World")}!")

if __name__ == "__main__":
    hello()