"""Dictionary functions."""

__author__ = "730665331"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """The keys of the input list becomes the values of the output list and vice versa."""
    new_dict: dict[str, str] = dict()
    for elem in inp_dict:
        if inp_dict[elem] in new_dict:
            raise KeyError("KeyError")
        else: 
            new_dict[inp_dict[elem]] = elem
    return new_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Should return the color that is most frequent.""" 
    new_dict: dict[str, int] = dict()
    color_list: list[str] = list()
    for elem in color_dict:
        color_list.append(color_dict[elem])
    new_dict = count(color_list)
    counter: int = 0
    fav_color: str = ""
    for color in new_dict:
        if new_dict[color] > counter:
            fav_color = color
            counter = new_dict[color]
    return fav_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Each key is associated with the count of the number of times that value appeared in the input list."""
    count_dict: dict[str, int] = dict()
    for item in inp_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Each key is a unique letter in the alphabet and each value is a list of words that began with that letter."""
    new_dict: dict[str, list[str]] = dict()
    new_list: list[str] = list()
    i = 0
    for word in inp_list:
        first_letter = word[0].lower()
        new_list.append(first_letter)
    for letter in new_list:
        new_dict[letter] = list()
    for word in inp_list:
        if word[0].lower() == new_list[i]:
            new_dict[new_list[i]] += [word]    
        i += 1
    return new_dict


def update_attendance(existing_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Mutate and return the same dictionary given."""
    if (day in existing_dict) is False:
        existing_dict[day] = [student]
    elif (student in existing_dict[day]) is False:
        existing_dict[day].append(student)
    else:
        existing_dict == existing_dict
    return existing_dict
