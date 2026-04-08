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

def binary_search(sequence, searched_number):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] == searched_number:
            return mid
        elif sequence[mid] < searched_number:
            left = mid + 1
        elif sequence[mid] > searched_number:
            right = mid - 1
    return None





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    sequential_data_serazene = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    cislo = linear_search(sequential_data, 5)
    print(cislo)
    mid = binary_search(sequential_data_serazene , 48)
    print(mid)
if __name__ == "__main__":
    main()
