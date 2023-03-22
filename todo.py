# create a global variable to hold the todo list
todo_list = []

# create a function to add items to the todo list
def add_item(item):
    todo_list.append(item)  # add the item to the list

# create a function to remove items from the todo list
def remove_item(item):
    todo_list.remove(item)  # remove the item from the list

# create a function to print the todo list in a hideous, overwrought format
def print_list():
    print('To do list:')
    for item in todo_list:
        print(' - ' + item)


# provide a main function that adds a few house chores to the to do list
def main():
    add_item('dishes')
    add_item('laundry')
    add_item('vacuum')
    add_item('dust')
    print_list()

# call the main function if this file is run as a script
if __name__ == '__main__':
    main()