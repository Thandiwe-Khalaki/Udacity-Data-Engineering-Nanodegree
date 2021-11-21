# Data Modeling with PostgreSQL

Data Modelling is the first project required to be done for the Data Engineering Nanodegree at Udacity.

## Purpose

Sparkify are a new music streaming app. They've been collecting data on the songs in their catalogue as well as user activity. The data are currently found in a directory of JSON logs on user activity, as well as a directory with JSON metadata on the songs in their app. The analytics team wish to understand what songs users are listening to, but there's currently no straightforward and simply way to query the data in its current form.

## Schema
This project uses the star schema to optimize queries on the tables. The start schema is the simplest style of data schema and consists of one or more fact tables referencing any number of dimension tables. The star schema is shown in figure 1

**Fact Table**:
* `songplays`

**Dimension Tables**:
* `users`
* `songs`
* `artists`
* `time`

![StarSchema](./images/star.png#center) 
Figure 1: The Star Schema.
      
## Usage

1. The `create_tables.py` script creates tables and inserts queries.
2. The`etl.ipynb` script reads and processes a single file  from `song_data` and `log_data` and loads the data into the tables.
3. The `etl.py` script reads and processes all files from `song_data` and `log_data` and loads the data into tables.
4. The `sql_queries` contains all sql queries to create tables and tables columns.
5. The `test.ipynb` displays the first rows of each table to test if they are correct.

## How to run the scripts

   1. Switch to terminal
   2. Run `python sql_queries.py`
   3. Run `create_tables.py`
   4. Go to the `etl.ipynb` notebook and run the cells.
   5. Go to `test.ipynb` noteboook and run the test to see if the tables are created and have column structure.
   6. Run `etl.py` to populate the tables.
   7. Go back to the `test.ipynb` to check if the test have been populated.

