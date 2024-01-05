#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    # Import required libraries

    import pandas as pd
    import numpy as np
    from fredapi import Fred
    import getpass

    # Create a key object to access the FRED API
    fred_api_key = getpass.getpass("Enter FRED API key: ")

    # Create a connection object using fred_api.Fred()
    Fred_conn = Fred(api_key=fred_api_key)

    # Create list to store series dataframes
    glob_oil_prices = []
    # Create a loop to iterate through each series and pull data for each class of oil
    for s in ["POLVOILUSDM", "PSUNOUSDM", "PPOILUSDM", "PROILUSDM", "PSOILUSDM"]:
        results = Fred_conn.get_series(s)
        # Rename series values to respective id
        results = results.to_frame(name=s)
        # Append to list
        glob_oil_prices.append(results)

    # Concatenate listed series data into a single dataframe
    glob_oil_prices_df = pd.concat(glob_oil_prices, axis=1)

    # Rename the index to 'date'
    glob_oil_prices_df.index.rename("date", inplace=True)

    # Drop null values.
    glob_oil_prices_df.dropna(inplace=True)

    # Create dictionary for renaming columns
    new_column_titles = {
        "POLVOILUSDM": "Olive Oil",
        "PSUNOUSDM": "Sunflower Oil",
        "PPOILUSDM": "Palm Oil",
        "PROILUSDM": "Rapeseed Oil",
        "PSOILUSDM": "Soybean Oil",
    }

    # Rename columns in the dataframe
    glob_oil_prices_df.rename(columns=new_column_titles, inplace=True)

    # Sort the DataFrame by 'item' and 'date' to ensure it's in the correct order
    glob_oil_prices_df = glob_oil_prices_df.sort_values(by=["date"])

    # Create the price change percentage columns
    # Calculate the price change percentage for each price column
    glob_oil_prices_df["Olive Oil Change %"] = glob_oil_prices_df[
        "Olive Oil"
    ].pct_change()
    glob_oil_prices_df["Sunflower Oil Change %"] = glob_oil_prices_df[
        "Sunflower Oil"
    ].pct_change()
    glob_oil_prices_df["Palm Oil Change %"] = glob_oil_prices_df[
        "Palm Oil"
    ].pct_change()
    glob_oil_prices_df["Rapeseed Oil Change %"] = glob_oil_prices_df[
        "Rapeseed Oil"
    ].pct_change()
    glob_oil_prices_df["Soybean Oil Change %"] = glob_oil_prices_df[
        "Soybean Oil"
    ].pct_change()

    # reset the index
    glob_oil_prices_df.reset_index(inplace=True)
    print(glob_oil_prices_df)


if __name__ == "__main__":
    main()
