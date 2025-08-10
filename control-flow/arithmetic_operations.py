def perform_operation (num1, num2, operation):
    match num2:
        case 0:
            print("Cannot divide by 0")

    match operation:
        case "add":
            return (num1 + num2)
        case "sutract":
            return (num1 - num2)
        case "multiply":
            return(num1 * num2)
        case "divide":
            return (num1 / num2)

