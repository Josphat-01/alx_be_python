def main(shopping_list, choice):
    add = shopping_list.append()
    remove  = shopping_list.remove(input())
    error = ("Goodbye!")


    match  choice:
        case "1" :
            return (add)
        case "2":
             return (remove)
        case "3":
            return(shopping_list)
        case  "4":
            return(error)
        case _ :
          return ("Invalid Choice. Please try again.")

print("Shopping List Manager")
print("1. Add Item")
print("2. Remove Item")
print("3. View List")
print("4. Exit")

choice = int(input("Choose Task: "))




