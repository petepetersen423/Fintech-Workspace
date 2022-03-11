import fire
import questionary


def run_crud(message="Running CRUD"):

    table_name = questionary.text(
        "What is the name of the database table that you would like to create?"
    ).ask()

    print(message)
    print(table_name)


if __name__ == "__main__":
    fire.Fire(run_crud)

