"""EX03 - avoid_fifth function."""

__author__: str = "720053793"


def main() -> None:
    """Entrypoint of the program."""
    string: str = ("The sentence we have here possesses E's galore!")
    print(avoid_fifth(string))


def avoid_fifth(string: str) -> str:
    """Avoid e's function."""
    i: int = 0
    stringE: str = ""
    while i < len(string):
        if string[i] == "e" or string[i] == "E":
            stringE += ""
        else:
            stringE += string[i]
        i += 1
    return stringE


if __name__ == "__main__":
    main()