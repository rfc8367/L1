users_string = input("Введите строку: ")

def list_of_elements(func):
    def sort_split():
        sorted_split = list(users_string.split(' '))
        print(sorted_split)
        func()
    return sort_split()


@list_of_elements
def new_string():
    return users_string
