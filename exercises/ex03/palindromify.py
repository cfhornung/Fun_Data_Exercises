"""EX03 - palindromify function."""

__author__: str = "720053793"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("han", True))
    print(palindromify("race", False))
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))


def palindromify(word: str, even: bool) -> str:
    """Palindrome function."""
    i: int = -1
    palindrome = word
    if not even is True:
        word = word[0:-1]
    while i >= (-(len(word))):
        palindrome += word[i]
        i -= 1
    return palindrome





if __name__ == "__main__":
    main()