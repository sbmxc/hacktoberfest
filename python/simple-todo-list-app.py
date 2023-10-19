class TodoItem:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self) -> str:
        status = "Done" if self.completed else "Not Done"
        return f"Description: {self.description} | Status: {status}"


class TodoList:
    def __init__(self):
        self.items = []

    def create_item(self, description) -> None:
        new_item = TodoItem(description)
        self.items.append(new_item)

    def read_item(self, index) -> TodoItem:
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            return None

    def update_item(self, index, description, completed=False) -> None:
        if 0 <= index < len(self.items):
            item = self.items[index]
            item.description = description
            item.completed = completed

    def complete_item(self, index) -> None:
        if 0 <= index < len(self.items):
            item = self.items[index]
            item.completed = True

    def delete_item(self, index) -> None:
        if 0 <= index < len(self.items):
            del self.items[index]

    def list_items(self) -> None:
        for index, item in enumerate(self.items):
            print(f"Item {index}:\n{item}\n")


# Option 1: List all Items
def app_list_all_items(todoList) -> None:
    todoList.list_items()


# Option 2: Create a new Item
def app_create_new_item(todoList) -> None:
    description = input("Enter the item description: ")
    todoList.create_item(description)
    print("Item created.")


# Option 3: Show an item
def app_show_item(todoList) -> None:
    index = int(input("Enter the index of the item you want to show: "))
    item = todoList.read_item(index)
    if item:
        print(item)
    else:
        print("Item not found.")


# Option 4: Complete an item
def app_complete_an_item(todoList) -> None:
    index = int(input("Enter the index of the item you want to complete: "))
    todoList.complete_item(index)
    print("Item completed.")


# Option 5: Update an item
def app_update_an_item(todoList) -> None:
    index = int(input("Enter the index of the item you want to update: "))
    description = input("Enter the new item description: ")
    todoList.update_item(index, description)
    print("Item updated.")


# Option 6: Delete an item
def app_delete_an_item(todoList) -> None:
    index = int(input("Enter the index of the item you want to delete: "))
    todoList.delete_item(index)
    print("Item deleted.")


def startApp() -> None:
    todoList = TodoList()
    while True:
        try:
            menu = """
            1. list all Items
            2. create a new Item
            3. show an item
            4. complete an item
            5. update an item
            6. delete an item
            what option would you like to select next (0 to exit):
            """
            option = int(input(menu))

            if option == 0:
                print("Goodbye")
                break
            elif option == 1:
                app_list_all_items(todoList)
            elif option == 2:
                app_create_new_item(todoList)
            elif option == 3:
                app_show_item(todoList)
            elif option == 4:
                app_complete_an_item(todoList)
            elif option == 5:
                app_update_an_item(todoList)
            elif option == 6:
                app_delete_an_item(todoList)
            else:
                print("Invalid option. Please enter a valid number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


startApp()
