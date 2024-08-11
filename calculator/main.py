from calc import Calculator

def main():
    calculator = Calculator()
    while True:
        op = input("Select operation: ")
        if op == 'r':
            print("Reseting...")
            calculator.reset()
        if op == 'g':
            print("Getting result...")
            print(calculator.get_current_value())
        x = int(input("Enter the number: "))
        if op == '1':
            print("Addition")
            calculator.add(x)
        if op == '2':
            print("Subtraction")
            calculator.subtract(x)
        if op == '3':
            print("Multiplication")
            calculator.multiply(x)
        if op == '4':
            print("Division")
            calculator.divide(x)
        if op == '0':
            print("Closing...")
            break
        else:
            continue

if __name__ == "__main__":
    main()