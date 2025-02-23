def main():
    print("Hello World")
    
def add(a:int, b:int) -> int:
    return a+b

def mul(a:int, b:int) -> int:
    return a*b

def division(a:int, b:int) -> int:
    return a/b

if __name__ == "__main__":
    main()
    result = add(int(input("Enter A Number: ")), int(input("Enter A Number: ")))
    print(f'The result is: {result}')