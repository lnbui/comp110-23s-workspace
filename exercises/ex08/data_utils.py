"""Utilities of EX08: Data Wrangling."""

__author__ = "730398384"


from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table under a certain header."""
    result: list[str] = []
    # step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys.""" 
    result: dict[str,list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all colmn values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], input_int: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    row_number: int = input_int
    for column in table:
        result_list: list[str] = []
        if len(table) <= input_int:
            result = table
        else: 
            i: int = 0
            while i < row_number:
                result_list.append(table[column][i])
                i += 1
            result[column] = result_list
    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Selects columns to return a new table of those selected columns."""
    result: dict[str, list[str]] = {}
    for column in table:
        for column in column_names:
            result[column] = table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Adds tables together to produce a new table."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1 [column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result
