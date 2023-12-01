import os
import pandas as pd
import argparse
import requests

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--id', help='ID to search for', default=None)
parser.add_argument('--schema', help='Schema to search for', default=None)
parser.add_argument('--name', help='Name to search for', default=None)
parser.add_argument('--aliases', help='Aliases to search for', default=None)
parser.add_argument('--birth_date', help='Birth date to search for', default=None)
parser.add_argument('--countries', help='Countries to search for', default=None)
parser.add_argument('--addresses', help='Addresses to search for', default=None)
parser.add_argument('--identifiers', help='Identifiers to search for', default=None)
parser.add_argument('--sanctions', help='Sanctions to search for', default=None)
parser.add_argument('--phones', help='Phones to search for', default=None)
parser.add_argument('--emails', help='Emails to search for', default=None)
parser.add_argument('--dataset', help='Dataset to search for', default=None)
parser.add_argument('--first_seen', help='First seen to search for', default=None)
parser.add_argument('--last_seen', help='Last seen to search for', default=None)
parser.add_argument('--last_change', help='Last change to search for', default=None)
parser.add_argument('--update', help='Update the lists', action='store_true')
args = parser.parse_args()


if args.update:
    # Define the URL
    url = "https://data.opensanctions.org/datasets/20231130/sanctions/targets.simple.csv"

    # Delete old file
    old_filename = "OpenSanctionsAllConList.csv"
    if os.path.exists(old_filename):
        os.remove(old_filename)

    # Download new file
    response = requests.get(url)
    with open(old_filename, 'wb') as f:
        f.write(response.content)

if not args.update:
    search_columns = ['id', 'schema', 'name', 'aliases', 'birth_date', 'countries', 'addresses', 'identifiers', 'sanctions', 'phones', 'emails', 'dataset', 'first_seen', 'last_seen', 'last_change']
    search_values = [args.id, args.schema, args.name, args.aliases, args.birth_date, args.countries, args.addresses, args.identifiers, args.sanctions, args.phones, args.emails, args.dataset, args.first_seen, args.last_seen, args.last_change]

    # Define the file
    file = "OpenSanctionsAllConList.csv"

    # Read the CSV file
    df = pd.read_csv(file)

    # Loop through the search columns and values
    for column, value in zip(search_columns, search_values):
        if value is not None and column in df.columns:
            df[column] = df[column].astype(str)
            df_filtered = df[df[column].str.contains(value, case=False, na=False)]
            if not df_filtered.empty:
                print(f"{column} - {value} found")
                print(', '.join(df.columns.tolist()))
                for index, row in df_filtered.iterrows():
                    print(', '.join(row.astype(str).tolist()))
            else:
                print(f"{column} - {value} not found")