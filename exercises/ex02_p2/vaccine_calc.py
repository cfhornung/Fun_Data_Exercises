"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "720053793"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days: int = int(days_to_target(population, doses, doses_per_day, target))
    # TODO 4: Call future_date and store result in a variable.
    date: str = str(future_date(days))
    # TODO 5: Print the expected output using the variables above.
    print("We will reach {}% vaccination in {} days, which falls on {}." .format(target, days, date))
    return None


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculating Days."""
    days: int = int(round(((target * population / 100) - (doses / 2)) / (doses_per_day / 2)))
    return days


# TODO 3: Define future_date function
def future_date(days: int) -> str:
    """Calculating today's date."""
    # Pulling todays date
    today: datetime = datetime.today()
    # Calculating time delta
    time_delta: timedelta = timedelta(days)
    # Calculating the date
    date: datetime = today + time_delta
    # Formatting the date
    date_string: str = date.strftime("%B %d, %Y")
    return date_string


if __name__ == "__main__":
    main()