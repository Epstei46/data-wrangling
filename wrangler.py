# Working on the exercise at https://ed.devmountain.com/materials/data-bp-1/exercises/data-wrangling/
# Pulled a CSV file from https://data.sfgov.org/Culture-and-Recreation/San-Francisco-Arts-Commission-Grants-FY2004-2016/mxvq-mfs5

# Code Review Feedback -- Good idea to break into functions, good for reusability, but want functions to run independent of each other. Can put them in a new file and import them into this file, as well as use try-except so that the rest of the code can run if a function runs into an error.

""""Exploratory Data Analysis"""
import numpy as np
import pandas as pd
import functions as fn
# print(pd.__version__)
    
    
"""This reads the CSV file using Pandas and saves it to a dataFrame object"""
df = pd.read_csv("San_Francisco_Arts_Commission_Grants_FY2004-2016.csv") # nrows=int if I want to limit # of rows read 
# new_header = df.iloc[0] #grab the first row for the header
# df = df[1:] #take the data less the header row
# df.columns = new_header #set the header row as the df header

"""Step 1: Exploration"""
print("Step 1: Exploration")
fn.try_or(lambda: fn.exploratory_info(df))
# print(df.dtypes)
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print(" /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")


"""Step 2: Select, Filter, Sort"""
print("Step 2: Select, Filter, Sort")
subset = fn.try_or(lambda: fn.create_subset(df))
subset = fn.try_or(lambda: fn.alphabetize(subset))
maths = fn.try_or(lambda: fn.quick_maths(subset, "Grant Amount"))
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print(" /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")


"""Step 3: Clean Data"""
print("Step 3: Clean Data")
fn.try_or(lambda: fn.incomplete_check(df))
# print(df.columns.tolist()) # Check to make sure column 'Community Focus: Women' was removed from the df
big_outlier_list, small_outlier_list = fn.try_or(lambda: fn.outlier_check(df, "Grant Amount", 12))
# print(f"Big Outliers: {big_outlier_list}\nSmall Outliers: {small_outlier_list}") # Check to make sure returning correctly
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print(" /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")


"""Step 4: Transform Data"""
print("Step 4: Transform Data")
fn.try_or(lambda: fn.groupby_count_sum(df, "Grant Category"))
fn.try_or(lambda: fn.groupby_count_sum(df, "Grant Category", "Grant Amount"))
fn.try_or(lambda: fn.groupby_count_sum(df, "Grant Fiscal Year", "Grant Amount"))