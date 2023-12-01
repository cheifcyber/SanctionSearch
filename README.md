# SanctionSearch

SanctionSearch is a Python program that allows you to search the Open Sanctions Consolidated List.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

`pip install -r requirements.txt`

## Usage

`python3 search.py --update`
` `
`python3 search.py --name [name] --id [id] --schema [schema] --aliases [aliases] --birth_date [birth_date] --countries [countries] --addresses [addresses] --identifiers [identifiers] --sanctions [sanctions] --phones [phones] --emails [emails] --dataset [dataset] --first_seen [first_seen] --last_seen [last_seen] --last_change [last_change]`

Replace the arguments in square brackets with the values you want to search for. You can use any combination of arguments. If you don't provide an argument, that field will not be searched.

The `--update` argument downloads the latest version of the Open Sanctions Consolidated List.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.