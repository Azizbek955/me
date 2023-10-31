def chop(lst):

    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
    else:

        print("The list should has at least 2 elements to chop .")


def middle(lst):

    if len(lst) >= 2:
        return lst[1:-1]
    else:

        print("The list should  have at least 2 elements to highlight the middle.")


My_list = [1, 2, 3, 4, 5]
print("Original list:", My_list)

chop(My_list)
print("After chop:", My_list)

Second_list = middle(My_list)
print("Middle elements:", Second_list)
