"""EX03 - prime functions."""

__author__: str = "720053793"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(17))
    print(list_primes(-1, 20))


def is_prime(integer: int) -> bool:
    """Produces a boolean."""
    i: int = 2
    prime: bool = True
    if integer < 2:
        prime = False
    while i < integer:
        if integer % i == 0:
            prime = False
        i += 1
    return prime


def list_primes(start: int, stop: int) -> list[int]:
    """Lists primes numbers."""
    integer: int = start
    primes: list[int] = []
    while integer < stop:
        if integer > 1:
            if is_prime(integer) is True:
                primes.append(integer)
        integer += 1
    return primes


if __name__ == "__main__":
    main()