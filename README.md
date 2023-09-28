# sqlalchemy-challenge

# Hawaii Weather Data Analysis

This project involves the analysis of weather data for Hawaii, specifically focusing on precipitation and temperature data. The analysis is performed using Python, SQLAlchemy for database interaction, and Matplotlib for data visualization.

## Prerequisites

Before running the script, ensure that you have the necessary libraries installed. You can install them using `pip`:

## Getting Started

1. **Database Setup**: This script assumes that you have a SQLite database named "hawaii.sqlite" located in a "Resources" directory. The database should contain two tables: "measurement" and "station."

2. **Script Overview**: The script is organized as follows:

   - Importing necessary libraries and setting up Matplotlib styles.
   - Creating an SQLAlchemy engine to connect to the database.
   - Using SQLAlchemy to reflect the database tables and create ORM classes.
   - Querying the database for weather data, including precipitation and temperature.
   - Creating Pandas DataFrames for the queried data.
   - Generating plots to visualize precipitation and temperature data.
   - Calculating summary statistics for the precipitation data.
   - Determining the number of weather stations and finding the most active station.
   - Obtaining temperature statistics for the most active station.
   - Visualizing temperature data as a histogram.
   - Closing the database session.

## Running the Script

Execute the script by running it in your Python environment. Make sure you have the "hawaii.sqlite" database in the "Resources" directory.

It should be noted that due to conflicts with flask and numpy imports, the code was executed from the git terminal using 'python app.py.'

## Results

The script will generate visualizations of precipitation and temperature data and display them using Matplotlib. Additionally, it will provide summary statistics for precipitation and temperature data.

## Author

Jason Stone

Readme assistance via Chat GPT



---

