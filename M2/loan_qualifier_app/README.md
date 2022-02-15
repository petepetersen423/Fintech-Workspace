# Loan Qualifier Application ver. 1.1

![Loan Qualifier Prompts](Images/loan_qual_logo.jpg)

Loan Qualifier is an applications designed to quickly and easily retrieve a list of loans for which a user is qualified. The application will prompt the user for input the needed in order to make the retieval of the qualifying loans possible. The application will ask the user for location of the `daily_rate_sheet` of loans from various lenders.  

**New in this version 1.1:**  

1. Once the qualifying loans list is created the user will be prompted whether to save the file and or to include an optional header.
2. The questionss will default to convenient values where possible.  
3. Added command line argument `save_file='n'`to supress file save function and and related prompts.
4. To run the **app,py** program with the optional CLI argument, use the following syntax.  

**python app.py save_file = "n"**

---

## Technologies

This project uses python 3.7 with the following packages:

* [fire 4.0](https://pypi.org/project/fire/) - Python Fire is a library for automatically generating command line interfaces (CLIs) with a single line of code.  It will turn any Python module, class, object, function, etc. (any Python component will work!) into a CLI. It’s called Fire because when you call Fire(), it fires off your command.

* [questionary 1.10.0](https://pypi.org/project/questionary/) - Questionary is a Python library for effortlessly building pretty command line interfaces

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

Upon launching the loan qualifier application you will be greeted with the following prompts.

![Loan Qualifier Prompts](Images/loan_qalifier.png)

---

## Contributors

Pete Petersen  
Tarek Atwan  
Anand Krishnan  

---

## Works Cited

Python Software Foundation. Python Language Reference, version 3.7. Available at [python.org](http://www.python.org)
[Python Standard Library](https://docs.python.org/3/library/index.html)

Pepperdine Loan Qualifier App fileio.py [Adding in Fire to Loan Qualifier App](https://courses.bootcampspot.com/courses/1103/files/1264429/download)

## License

MIT

## Changes

### 1. Added user requested function to save file in fileio.py

```def save_csv(csvpath, list, header_option=None):
    """
    Write a CSV that contains the rows in the supplied lists.  
    This function was modeled on save_csv in the adding 
    fire_to_the_Loan_Qualifier_App

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
```

### 2.  Added interactive function for save implementation in app.py

```def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!

    while True:
        save_y_n = questionary.confirm(
            "Would you like to save the file?", default=True
        ).ask()
        if save_y_n:
            break

    if save_y_n:

        while True:
            csv_file_name = questionary.text(
                "Enter the path and name for the file to save?",
                default="./data/my_qualifying_loans.csv",
            ).ask()
            if len(csv_file_name) > 1:
                break

        while True:
            header_option = questionary.confirm(
                "Would you like a header?", default=True
            ).ask()
            if header_option:
                qualifying_loans_header = [
                    "Lender",
                    "Max Loan" "Amount",
                    "Max LTV",
                    "Max DTI",
                    "Min Credit Score",
                    "Interest Rate",
                ]
                break

    if header_option:
        save_csv(
            csv_file_name, qualifying_loans, header_option == qualifying_loans_header
        )
    else:
        save_csv(csv_file_name, qualifying_loans, header_option == None)
```
