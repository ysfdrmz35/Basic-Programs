import time
print("\nWelcome to the right triangle checker algorithm\n")
time.sleep(0.5)


def get_edge_lengths():
    while True:
        edge_lengths = input("Please enter the edge lenghts of the triangle (Please use ',' to seperate)   :  ")
        numbers = "0123456789"
        comma_number = 0
        error = False
        for c in edge_lengths:
            if not(c == "," or c in numbers):
                error = True
            if c == ",":
                comma_number += 1
        if error or comma_number != 2:
            time.sleep(0.5)
            print("\nYou entered something wrong, please try again\n")
            continue
        else:
            edge_lengths = edge_lengths.split(",")
            for x in edge_lengths:
                edge_lengths[edge_lengths.index(x)] = int(x)
            return edge_lengths


def check(x):
    a, b, c = x[0], x[1], x[2]
    if a**2 + b**2 == c**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    else:
        return False
while True:
    if check(get_edge_lengths()):
        print("\nYour triangle is right triangle\n")
    else:
        print("\nYour triangle is not right triangle\n")










