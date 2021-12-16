# Working on the exercise at https://ed.devmountain.com/materials/data-bp-1/exercises/data-wrangling/
# Pulled a CSV file from https://data.sfgov.org/Culture-and-Recreation/San-Francisco-Arts-Commission-Grants-FY2004-2016/mxvq-mfs5

""""Exploratory Data Analysis"""
import numpy as np
import pandas as pd
# print(pd.__version__)
    
def exploratory_info(df):
    """Using pandas to print basic information about your dataset such as number of rows, averages for numeric columns, and any other useful explanatory information about your dataset."""
    
    print(f"    Table has {df.shape[0]} rows and {df.shape[1]} columns.\n")
    
    avg = df["Grant Amount"].mean().__round__(2)
    median = df["Grant Amount"].median().__round__(2)
    minn = df["Grant Amount"].min().__round__(2)
    maxx = df["Grant Amount"].max().__round__(2)
    print(f"    Analysis of Grants Amounts:\nAverage of ${avg}\nMedian of ${median}\nMinimum of ${minn}\nMaximum of ${maxx}\n")
    
    # count = df["Community Focus: Disabled"].value_counts() #.fillna(False) if NaN values
    true_counts = df[["Community Focus: African American","Community Focus: Asian American","Community Focus: Disabled","Community Focus: Immigrant","Community Focus: L/G/B/T/Q","Community Focus: Latino American","Community Focus: Multiple People of Color","Community Focus: Native","Community Focus: Native American","Community Focus: Pacific Islander","Community Focus: Transgender","Community Focus: Women","Community Focus: No specified focus"]].sum()
    print(f"    Below is a list of the number of applicants with the specified Community Focus:\n{true_counts}\n")
    
def create_subset(df):
    """This function produces a subset of your data and prints the before/after difference (rows,columns), then returns the subset so it can be saved to an object."""
    df_sub = df.iloc[0:13]
    df_sub = df_sub[["Name of Applicant","Grant Category","Grant Amount"]]
    print(f"{df.shape} reduced to {df_sub.shape}\n")
    return df_sub
    
    
def alphabetize(df):
    """This function organizes the data in alphabetical order, returning the alphabetized dataFrame."""
    ### Below print is for the original look
    # print("Below is a subset of the data, before re-ordering:\n",df_abc,'\n')
    df_abc = df.sort_values("Name of Applicant", ascending=True)
    ### Below print is for the re-ordered look
    print("Below is a subset of the data, ordered alphabetically by applicant name:\n",df_abc,'\n')
    return df_abc
    
def quick_maths(df, column):
    """This function calculates the [avg, median, min, max] for the given (df, column), printing a readable result and returning those results in a list for further use."""
    avg = df[f"{column}"].mean().__round__(2)
    median = df[f"{column}"].median().__round__(2)
    minn = df[f"{column}"].min().__round__(2)
    maxx = df[f"{column}"].max().__round__(2)
    print(f"    Analysis of {column}:\nAverage of ${avg}\nMedian of ${median}\nMinimum of ${minn}\nMaximum of ${maxx}\n")
    return [avg, median, minn, maxx]

def incomplete_check(df):
    """This function checks for the following values in each cell: None, NaN, NaT, numpy.NaN, '', numpy.inf. If the column did not have too many null values, they are replaced with a meaninful value or returned in a list of every column where there were some unhandled null values. If the column was mostly null values, it is removed from the dataFrame (df)."""
    bad_lists = []
    pd.options.mode.use_inf_as_na = True
    column_names = list(df.columns)
    for column in column_names:
        nulls = df[f"{column}"].isnull().sum()
        if nulls > 0:
            print(f"The column '{column}' has {nulls} nulls in it. The data type is {df[f'{column}'].dtype}.")
            if nulls > df.shape[0]/2:
                print(f"The table has {df.shape[0]} rows. Because most of the values in this column have a null value, this column has been dropped from the table.")
                df.drop(f"{column}", axis=1, inplace=True)
            elif df[f'{column}'].dtype == 'bool':
                df[f'{column}'] = df[f'{column}'].fillna(False, inplace=True)
            elif df[f'{column}'].dtype == 'float64':
                df[f'{column}'] = df[f'{column}'].fillna(0, inplace=True)
            else:
                bad_lists.append(f"{column}")

def outlier_check(df, column, median_multiplier=10):
    """This function checks for big/small outliers in the given (df, column), prints a readable result, then returns [[big_outliers], [small_outliers]]."""
    median = df[f"{column}"].median().__round__(2)
    
    big_outliers = [value for value in df[f"{column}"] if value > (median*median_multiplier)]
    print(f"    Outliers {median_multiplier} times greater than the median {median}:\n{big_outliers}") if len(big_outliers) > 0 else print(f"No Big Outliers {median_multiplier} times greater than the median {median}.")
    
    small_outliers = [value for value in df[f"{column}"] if value < (median/median_multiplier)]
    print(f"    Outliers {median_multiplier} times smaller than the median {median}:\n{small_outliers}") if len(small_outliers) > 0 else print(f"No Small Outliers {median_multiplier} times smaller than the median {median}.")
    return [big_outliers,small_outliers]
    
    
    
    
"""This reads the CSV file using Pandas and saves it to a dataFrame object"""
df = pd.read_csv("San_Francisco_Arts_Commission_Grants_FY2004-2016.csv") # nrows=int if I want to limit # of rows read 
# new_header = df.iloc[0] #grab the first row for the header
# df = df[1:] #take the data less the header row
# df.columns = new_header #set the header row as the df header

"""Step 1: Exploration"""
# exploratory_info(df)
# print(df.dtypes)

"""Step 2: Select, Filter, Sort"""
# subset = create_subset(df)
# subset = alphabetize(subset)
# maths = quick_maths(subset, "Grant Amount")

"""Step 3: Clean Data"""
incomplete_check(df)
# print(df.columns.tolist()) # Check to make sure column 'Community Focus: Women' was removed from the df
big_outlier_list, small_outlier_list = outlier_check(df, "Grant Amount", 12)
# print(f"Big Outliers: {big_outlier_list}\nSmall Outliers: {small_outlier_list}") # Check to make sure returning correctly

"""Step 4: Transform Data"""
