def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question + ' (y/n)? ').lower()
        return response
def ask_number(question, low, high):
    response = None
    while response not in range(low, high + 1):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("вы запустили модуль games, а не импортировали его")
    input("\n\nажмите Enter, чтобы выйти")
