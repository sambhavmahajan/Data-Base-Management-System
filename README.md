# Data-Base-Management-System (DBMS)

This Database Management System (DBMS) is crafted to facilitate basic database operations via a command-line interface. It empowers users to create tables, execute data insertion, perform various operations, and visualize data using matplotlib.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This DBMS is designed to handle basic database operations through a set of command-line commands. It allows users to create tables, insert data, perform various operations, and visualize data using matplotlib.

## Features

- **Table Creation:** Create tables with specified column names.
- **Data Manipulation:** Insert, delete, modify rows, and perform basic operations like sum and average.
- **File Handling:** Save and open tables to/from CSV files.
- **Data Visualization:** Generate simple plots using matplotlib.
- **Command-Line Interface:** Use a set of commands to interact with the database.

## Installation

First install numoy, pandas and matplotlib, Download the source code and then run!

Usage

After running the program, follow the command-line prompts to interact with the DBMS. Type help to view available commands.
Commands

The following commands are supported:

    clear
    create:<column_name1>:<column_name2>:...
    insert:<row_name>:<value1>:<value2>:...
    delete_row:<row_name>
    save:<filename>
    open:<filename>
    show
    sum:<column_name>
    avg:<column_name>
    shape
    plot:title:xlabel:ylabel:xcolumn:columntoplot
    modify:<row_name>:<column_name>:<new_value>
    quit
    help

Contributing

Feel free to contribute by opening issues or submitting pull requests. Your contributions are highly appreciated.
