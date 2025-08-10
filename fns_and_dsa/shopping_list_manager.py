
def display_menu():
     print(f"Shopping List Manager")
     print("1. Add item")
     print("2. Remove item")
     print("3. View list")
     print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' Added to the shopping list.")
    else:
        print("Cannot be empty.")

def remove_item(shopping_list):
    item_to_remove = input("Enter the item to remove: ").strip()
    if not item_to_remove:
        print("Cannot be empty.")
        return

    for existing_item in shopping_list:
        if existing_item.lower() == item_to_remove.lower():
            shopping_list.remove(existing_item)
            print(f"'{existing_item}' removed list.")
            return

    print(f"'{item_to_remove}' is not in the shopping list.")


def view_list(shopping_list):
    if shopping_list:
        print("\n--- Your Shopping List ---")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("\nYour shopping list is empty.")

def main():

    shopping_list = []

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
