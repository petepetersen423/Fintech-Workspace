import fire
import questionary
import sqlalchemy
import pandas as pd
from pathlib import Path

# Create a temporary sqlite database
database_connection_string = "sqlite:///"

# Create an engine to interact with the database
engine = sqlalchemy.create_engine(database_connection_string)

# Create a test DataFrame
stocks_dataframe = pd.DataFrame({"AAPL": [1, 2], "GOOG": [3, 4]})


def create_table(engine, table_name, table_data_df):
    table_data_df.to_sql(table_name, engine, index=False, if_exists="replace")


def confirm_tables(engine):
    tables = engine.table_names()
    print(f"The tables in the database are: {tables}")


def read_table(engine, table_name):
    return pd.read_sql_table(table_name, con=engine)


def read_top_n(engine, table_name, number_results=1):
    top_n_query = """
    SELECT * from {table_name}
    ORDER BY AAPL DESC
    LIMIT {number_results};
    """
    return pd.read_sql_query(top_n_query, con=engine)


def run():
    """The main function for running the application."""

    table_name = questionary.text("What table would you like to display?").ask()
    table_dataframe = read_table(engine, table_name)
    print(table_dataframe)


if __name__ == "__main__":
    fire.Fire(run)


def run():
    """The main function for running the application."""

    top_n_results = read_top_n(engine, "stocks", 1)
    print("The top 1 result was: ", top_n_results)


if __name__ == "__main__":
    fire.Fire(run)
