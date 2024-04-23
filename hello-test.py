def hello():
    # print("Hello, World!")
    message = os.environ.get("A_VARIABLE", "World")
    print(f"Hello, {message}!")

if __name__ == "__main__":
    hello()