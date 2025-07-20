num1 = int(input("Enter the first number: "))
num2 = int (input("Enter the second number: "))

operation = str(input("Choose the operation (+, -, *, /): "))

match num2:
     case 0:
         print("Cannot divide by 0")

match operation:
    case "+":
        print("The result is",num1+num2)
    case "-":
        print("The result is",num1-num2)
    case "*":
        print("The result is",num1*num2)
    case "/":
        print("The result is",num1/num2)






