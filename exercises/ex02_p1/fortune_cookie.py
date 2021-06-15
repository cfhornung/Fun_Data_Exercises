"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "720053793"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """The Fortunes."""
    if fortune == 1:
        return "Be careful or you could fall for some tricks today."
    else:
        if fortune == 2:
            return "A fresh start will put you on your way."
        else:
            if fortune == 3:
                return "When you believe in yourself, others will too."
            else:
                if fortune == 4:
                    return "Change is happening in your life, so go with the flow!"
                else:
                    if fortune == 5:
                        return "One good friendship is often more important than a passionate romance."
                    else:
                        return "Everyday in your life is a special occasion."


fortune: int = randint(1, 6)
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
