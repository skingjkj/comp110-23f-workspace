"""Dictionary unit tests."""

__author__ = "730665331"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Invert unit tests
def test_empty_dict() -> None:
    """Test the invert function with an empty dictionary."""
    test: dict[str, str] = {}
    assert invert(test) == {}


def test_char() -> None:
    """Test the invert function with characters."""
    test: dict[str, str] = {'d': 'l', 'r': 'a', 's': 'j'}
    assert invert(test) == {'l': 'd', 'a': 'r', 'j': 's'}


def test_word() -> None:
    """Test the invert function with words."""
    test: dict[str, str] = {'tar': 'heels', 'north': 'carolina', 'chapel': 'hill'}
    assert invert(test) == {'heels': 'tar', 'carolina': 'north', 'hill': 'chapel'}


# Favorite_color unit tests

def test_one_color() -> None:
    """Tests the favorite color function with one favorite color."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test) == "blue"


def test_two_color() -> None:
    """Tests the favorite color function with two favorite colors."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Michael": "yellow"}
    assert favorite_color(test) == "yellow"


def test_no_color() -> None:
    """Tests the favorite color function with no favorite color."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "green"}
    assert favorite_color(test) == ""


# Count unit tests

def test_empty_list() -> None:
    """Tests the count function with an empty list."""
    test: list[str] = []
    count(test)
    assert count(test) == {}


def test_repeat() -> None:
    """Tests the count function with repeated value."""
    test: list[str] = ["Dominic", "Dominic", "Dominic"]
    count(test)
    assert count(test) == {'Dominic': 3}


def test_diff() -> None:
    """Tests the count function with different values and different counts."""
    test: list[str] = ["Dominic", "Luke", "Dominic"]
    count(test)
    assert count(test) == {'Dominic': 2, 'Luke': 1}


# Alphabetizer unit tests

def test_empty() -> None:
    """Tests the alphabetizer function with an empty list."""
    test: list[str] = []
    assert alphabetizer(test) == {}


def test_two() -> None:
    """Test the alphabetizer function with two words per character."""
    test: list[str] = ["dominic", "luke", "jordan", "larry", "daniel", "jess"]
    assert alphabetizer(test) == {'d': ['dominic', 'daniel'], 'l': ['luke', 'larry'], 'j': ['jordan', 'jess']}


def test_different() -> None:
    """Test the alphabetizer function with different number of words per character."""
    test: list[str] = ["dominic", "luke", "jordan", "daniel",]
    assert alphabetizer(test) == {'d': ['dominic', 'daniel'], 'l': ['luke'], 'j': ['jordan']}


# Update_attendance unit tests

def test_no_change() -> None:
    """Test the update attendance function with no changes made."""
    test: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Monday"
    student: str = "Vrinda"
    assert update_attendance(test, day, student) == {'Monday': ["Vrinda", "Kaleb"], 'Tuesday': ["Alyssa"]}


def test_multiple() -> None:
    """Test the update attendance function with multiple days with the same number of students."""
    test: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Monday"
    student: str = "Vrinda"
    update_attendance(test, "Tuesday", "Vrinda")
    update_attendance(test, "Wednesday", "Kaleb")
    assert update_attendance(test, day, student) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}


def test_difference() -> None:
    """Test the update attendance function with multiple days with a different number of students."""
    test: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Monday"
    student: str = "Vrinda"
    update_attendance(test, "Tuesday", "Vrinda")
    update_attendance(test, "Wednesday", "Kaleb",)
    update_attendance(test, "Wednesday", "Dominic")
    assert update_attendance(test, day, student) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb', 'Dominic']}