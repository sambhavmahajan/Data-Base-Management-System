# DataFrame Command-Line Interface

This repository provides a command-line interface for manipulating a DataFrame using numpy, pandas, and matplotlib. You can perform various operations such as creating tables, inserting rows, deleting rows, saving to a file, loading from a file, and more.

## Prerequisites

Make sure you have the following libraries installed:

- numpy
- pandas
- matplotlib

You can install these libraries using pip:

```sh
pip install numpy pandas matplotlib
```

## Usage

Run the script using Python:

```sh
python script_name.py
```

Once the script is running, you can type commands to interact with the DataFrame. Type `help` to see a list of available commands.

## Commands

Here is a list of available commands and their syntax:

- `clear`  
  Clear the entire database.

- `command0;command1;command2;........`  
  Chain multiple commands together using semicolons.

- `create:<column_name1>:<column_name2>:...`  
  Create a new table with specified column names.

- `insert:<row_name>:<value1>:<value2>:...`  
  Insert a new row with specified values.

- `delete_row:<row_name>`  
  Delete a row with the specified row name.

- `save:<filename>`  
  Save the current table to a CSV file.

- `open:<filename>`  
  Load a table from a CSV file.

- `show`  
  Display the current table.

- `sum:<column_name>`  
  Calculate the sum of the specified column.

- `avg:<column_name>`  
  Calculate the average of the specified column.

- `shape`  
  Display the shape of the current table (number of rows and columns).

- `plot:title:xlabel:ylabel:xcolumn:columntoplot`  
  Create a plot with the specified title, x-axis label, y-axis label, x-axis column, and column to plot.

- `modify:<row_name>:<column_name>:<new_value>`  
  Modify a specific cell in the table.

- `quit`  
  Exit the program.

- `help`  
  Display this list of commands.

## Example Commands

Here's a quick example of how you might use some of these commands:

1. Create a table:

    ```sh
    create:Name:Age:Salary
    ```

2. Insert a row:

    ```sh
    insert:John:30:50000
    ```

3. Show the table:

    ```sh
    show
    ```

4. Save the table:

    ```sh
    save:my_table.csv
    ```

5. Load a table:

    ```sh
    open:my_table.csv
    ```

6. Plot data:

    ```sh
    plot:Employee Age vs Salary:Age:Salary:Age:Salary
    ```

## Code Overview

The main logic of the program is contained within the `main` function, which enters an infinite loop to accept and process user commands. The commands are parsed, and the appropriate functions are called to perform the specified operations.

### Function Descriptions

- **tokens(li)**: Splits a command string into its constituent tokens.
- **removespace(s)**: Removes spaces from a string.
- **CreateTable(li)**: Creates a new table with specified column names.
- **Insert(li)**: Inserts a new row into the table.
- **GetIndex(arr, Indexname)**: Gets the index of a specified element in a list.
- **DeleteRow(Row_Name)**: Deletes a specified row from the table.
- **Generate_DF()**: Generates a pandas DataFrame from the current table data.
- **SaveToFile(filename)**: Saves the current table to a CSV file.
- **OpenFile(filename)**: Loads a table from a CSV file.
- **Show()**: Displays the current table.
- **modify(i, c, newVal)**: Modifies a specific cell in the table.
- **Sum(columnName)**: Calculates the sum of a specified column.
- **Avg(columnName)**: Calculates the average of a specified column.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
