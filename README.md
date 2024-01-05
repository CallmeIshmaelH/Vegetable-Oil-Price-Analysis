# Global-Vegetable-Oil-Price-Analysis
Data Project using St. Louis Federal Reserve Economic Data FRED API


## Overview
This project involves fetching and analyzing global price data for various edible oils using data from the St. Louis Federal Reserve Economic Data Portal (https://fred.stlouisfed.org/), via the FRED API. Our goal is to observe trends over the years and identify any significant coincidental patterns among different types of oils. The analysis is performed using a Python script that retrieves data, cleans and processes it, and creates a consolidated dataset for further analysis. The provided Python script is designed to be used as a pipeline within Power BI.

## Prerequisites
Before running the script, ensure you have the required libraries installed. You can install them using the following:

!pip3 install --upgrade certifi

!pip3 install python-certifi-win32

!pip3 install pandas

!pip3 install numpy

!pip3 install matplotlib

!pip3 install plotly --upgrade

!pip3 install plotly.express

!pip3 install fredapi 

## Getting Started
FRED API Key: You will need to obtain an API key from the FRED (Federal Reserve Economic Data) website. The script will prompt you to enter your FRED API key when executed.

## Power BI Connection 
This script is intended to be used with Power BI. You can easily integrate it into Power BI by copying and pasting the code into the Power BI "Python Script" editor.

<img width="721" alt="image" src="https://github.com/CallmeIshmaelH/Vegetable-Oil-Price-Analysis/assets/48251325/f51ec8e1-2766-4b26-9259-7d1de4565067">

## Results
The script fetches data for Olive Oil, Sunflower Oil, Palm Oil, Rapeseed Oil, and Soybean Oil prices from the FRED API, cleans and processes the data, and calculates the percentage change in prices over time. The resulting dataset is suitable for analysis within Power BI.

Looking at the time series data, we notice a large uptick in the price of Sunflower oil, coinciding with the start of the Russo-Ukraine War.
This was accompanied by modest increase in the price of rapeseed, palm, and soya bean oil as well, likely due to increased demand. 
In later 2022, the global price of Olive Oil began to increase. By the end of 2023, the price of Olive Oil had increased by almost 200%.
The sudden price increase, may likely have been caused by a poor yield of olives in Spain in 2022 (https://www.oliveoiltimes.com/topic/2022-olive-harvest).
As, the largest producer of olives in the world, Spain accounts for 30.2% of the world's olive oil production, consequently, any fluctuation in Spain's output could have significant consequences for the global price of olive-related commodities.






