from exercises.ex08.river import River

def my_river() -> None:
    Fish: int = 10
    Bear: int = 2
    assert River(Fish, Bear)

my_river.view_river()
