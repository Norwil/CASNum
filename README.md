# CAS Number Database Project

This project is a simple database that stores chemical compounds information using CAS (Chemical Abstracts Service) numbers. The user can interact with the database by fetching information of a specific chemical compound using its CAS number.
![Screenshot 2023-05-09 115709](https://user-images.githubusercontent.com/46763365/237062596-f024333e-f3da-49ee-a0f9-80096fca0f62.png)


## Requirements

- Python 3.x
- SQLite


## Installation

1. Clone the repository to your local machine using the following command:

git clone https://github.com/Norwil/CASNum.git


2. Install the required packages using the following command:


pip install -U prettytable

## Usage

1. Run the `main.py` file using the following command:

python main.py

2. The program will prompt you to enter a CAS number, simply type the desired CAS number and press enter.

3. The program will retrieve the information of the chemical compound with the specified CAS number from the database.

## Project Structure

The project consists of two main files:

- `database.py`: This file contains the `Database` class, which is responsible for connecting to the database and performing CRUD (Create, Read, Update, Delete) operations on the `chemicals` table.

- `main.py`: This file contains the `main` function, which is the entry point of the program. It interacts with the user and calls the `Database` class methods to perform database operations.

## Contributing

Your contributions are always welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/Norwil/CASNum/blob/master/LICENSE).



