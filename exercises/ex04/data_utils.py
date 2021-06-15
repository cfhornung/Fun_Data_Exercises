
"""Utility functions for wrangling data."""

__author__ = "720053793"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Column Values."""
    col_val: list[str] = []
    for row in table:
        col_val.append(row[key]) 
    return col_val


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Columnar."""
    dict_table: dict[str, list[str]] = {}
    keys = table[0].keys()
    for i in keys:
        dict_table[i] = column_values(table, i)   
    return dict_table    


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Creating a head function."""
    head_dict: dict[str, list[str]] = {}
    keys = table.keys()
    for i in keys:
        col_val: list[str] = []
        row: int = 0
        for j in i:
            while row < n:
                col_val.append(table[i][row])
                head_dict[i] = col_val
                row += 1
    return head_dict


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Select Function."""
    select_dict: dict[str, list[str]] = {}
    for i in names:
        select_dict[i] = table[i]
    return select_dict


def count(values: list[str]) -> dict[str, int]:
    """Count."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1    
    return counts