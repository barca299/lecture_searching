from pathlib import Path
import json


def read_data(file_name, field):
    with open(file_name, "r") as file:
        data = json.load(file)

    if field not in data.keys():
        return None
    else:
        return data[field]


    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
def linear_search(sequence, searched_number):
    count = 0
    seznam_pozic = []
    for i, number in enumerate(sequence):
        if searched_number == number:
            seznam_pozic.append(i)
            count += 1
    slovnik = {"seznam_pozic": seznam_pozic, "count": count}
    return slovnik



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    cislo = linear_search(sequential_data, 5)
    print(cislo)
if __name__ == "__main__":
    main()
