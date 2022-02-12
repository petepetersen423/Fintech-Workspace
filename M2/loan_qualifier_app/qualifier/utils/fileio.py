# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


# PP 02/11/2022 - added function to save a CSV based on user requirements
# PP 02/12/2022 - modified docstring
# PP 02/02/2022 - added cition in doc string forreferenced code


def save_csv(csvpath, list, header_option=None):
    """
    Write a CSV that contains the rows in the supplied lists.
    This function was modeled on save_csv in the adding
    fire_to_the_Loan_Qualifier_App unit 2.3.4.
    (https://courses.bootcampspot.com/courses/1103/files/1264429/download)

    Args:
        csvpath (Path): The file path.
        list : A list of the rows of data for the CSV file.
        header (list): An header for the CSV.

    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        if header_option:
            csvwriter.writerow(header_option)
        csvwriter.writerows(list)
