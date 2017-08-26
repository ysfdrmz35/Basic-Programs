import time
print("\nWelcome ...\n")
time.sleep(0.5)


def get_numbers():
    numbers_input = input("Please enter the numbers you want to order (Use \" \" or \",\" to seperate): ")
    return numbers_input


def select_operation():
    operation_number = input("\nPlease select the operation number,\n\nfor min to max order enter 1"
                             "\nfor max to min order enter 2\n\n:  ")
    if operation_number == "1":
        return 1
    elif operation_number == "2":
        return 2
    else:
        return 3

def clean_numbers():
    characters = "0123456789, "
    numbers = get_numbers()
    numbers_list = list(numbers)
    for c in numbers_list:
        if c not in characters:
            return "Wrong"
    else:
        for c in numbers_list:
            if c == " ":
                numbers_list[numbers_list.index(c)] = ","
        numbers = ""
        for c in numbers_list:
            numbers += c
        return numbers.split(",")


while True:
    numbers = clean_numbers()
    if not numbers == "Wrong":
        ordered_numbers = []
        operation = select_operation()
        if operation == 1:
            for i in range(len(numbers)):
                min_value = min(numbers)
                ordered_numbers.append(min_value)
                numbers.remove(numbers[numbers.index(min_value)])
            result = "<".join(ordered_numbers)
            print("\n" + result)
            break
        elif operation == 2:
            for i in range(len(numbers)):
                max_value = max(numbers)
                ordered_numbers.append(max_value)
                numbers.remove(numbers[numbers.index(max_value)])
            result = ">".join(ordered_numbers)
            print("\n" + result)
            break
        elif operation == 3:
            print("\nYou entered wrong !!")
            print("\nPlease try again ...\n")
            continue
    print("\nYou entered wrong !!")
    print("\nPlease try again ...\n")
