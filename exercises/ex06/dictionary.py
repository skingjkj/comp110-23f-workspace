"""Dictionary functions."""

__author__ = "730665331"

def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """The keys of the input list becomes the values of the output list and vice versa."""
    new_dict: dict[str, str] = []
    for elem in inp_dict:
        if inp_dict[elem] in new_dict:
            raise KeyError("KeyError")
        else: 
            new_dict[inp_dict[elem]] = elem
    return new_dict
        

def favorite_color(color_dict: dict[str, str]) -> str:
    """Should return the color that is most frequent.""" 
    new_dict: dict[str, str] = []
    color_list: list[str] = list()
    for elem in color_dict:
        color_list.append(color_dict[elem])
    for item in new_dict:
        new_dict[item] = 0
    for color in color_list:
        if color in new_dict is True:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    counter: int = 0
    fav_color: str = ""
    for color in color_dict:
        if color_dict[color] > counter:
            fav_color = color
            counter = color_dict[color]
    return fav_color
    

   
def count(inp_list: list[str]) -> dict[str, int]:
    """Each key is associated with the count of the number of times that value appeared in the input list."""
    count_dict: dict[str, int] = []
    for item in inp_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Each key is a unique letter in the alphabet and each value is a list of words that began with that letter"""
    new_list: list[str] = list()
    new_dict: dict[str, list[str]] = []
    for item in inp_list:
        new_list.append(item[0])
    for beginning_letter in new_list:
        if beginning_letter == item[0]:
            new_dict[beginning_letter] = item
    return new_dict



def update_attendance(existing_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Mutate and return the same dictionary given."""
    for item in existing_dict:
        if day in existing_dict:
            existing_dict[item] += student
        else:
            existing_dict[day] = student
        