"""`Ex04: list` Utility Functions"""
__author__ = "730665331"


def main() -> None:
    print(is_equal([1, 1, 21], [1, 1, 21]))

# First function: given a list of ints and an int, return a bool indicating whether all the ints in the list are the same as given int.


def all(int_list: list[int], number: int) -> bool:
    # Declaring the variable that's going to be used.
    i = 0
    # Condition to return false if the list is empty.
    if len(int_list) == 0:
        return False
    # While loop to check the int through every index of the list. If they are the same, it keeps checking until the last index or when it isn't the same. Returns true if it's the same until loops ends, false other wise.
    while i <= (len(int_list) - 1):
        if number == int_list[i]:
            i += 1
        else:
            return False
    return True

# Second function: given a list of ints, return the largest in the list. 


def max(input: list[int]) -> int:
    # Declaring the variable that's going to be used.
    i = 0
    biggest_int = 0
    # Condition to return false if the list is empty.
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # while loop to check through every number to see if it's bigger than the value stored, if yes, the index is stored as the new biggest number and compared to the rest of the list.
    while i <= (len(input) - 1):
        if biggest_int < input[i]:
            biggest_int = input[i]
            i += 1
        else:
            biggest_int = biggest_int
            i += 1
    return biggest_int

# Third function: given two lists of int values, return true if every element at every index is equal in both lists.


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    # Declaring the variable that's going to be used.
    i = 0
    q = 0
    # Make sure the length are equal
    if len((first_list)) != len((second_list)):
        return False
    # Loop to make sure that the two lists are indentical to each other, if not, return false.
    while i <= (len(first_list) - 1) and q <= (len(second_list) - 1):
        if first_list[i] == second_list[q]:
            i += 1
            q += 1
        else:
            return False
    return True


if __name__ == "__main__":
    main()