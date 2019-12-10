# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:13:00 2019

@author: Ronghui Zhou, zhou.uf@gmail.com

"""

# =============================================================================
# Download data file from this website
# https://insights.stackoverflow.com/survey
# 
# Rename data files as: survey_results_[YEAR].csv in .\data folder
# Rename schema files as: survey_results_schema_[YEAR].csv in .\data\schema folder

# Python files are in .\analysis folder

# =============================================================================


# import os and pandas
import os
import pandas as pd

# set up the relative data directory

datapath='..\\data\\'

# get the current directory

dirpath=os.getcwd()

def listfiles(folder):
    return [d for d in os.listdir(folder) if not os.path.isdir(os.path.join(folder, d))]

# =============================================================================
# list files and directories
# file_list=os.listdir(datapath)
# =============================================================================

# List data files, not directories
    
file_list=listfiles(datapath)

print(file_list)

print(len(file_list))

# List schema files, not directories

schemapath='..\\data\\schema\\'

schema_list=listfiles(schemapath)

print(schema_list)

print(len(schema_list))

# Get a sorted list of the years for data files
data_year_list=[]
for file_name in file_list:
    data_year_list.append(int(file_name[-8:-4]))
    
# sort the list
data_year_list.sort()

# print the list and the type
print(data_year_list)
print(type(data_year_list))


# Get a sorted list of the years for schema files
schema_year_list=[]
for schema_name in schema_list:
    schema_year_list.append(int(schema_name[-8:-4]))

# sort the list
schema_year_list.sort()

# print the list and the type
print(schema_year_list)
print(type(schema_year_list))

year=2019
for file in file_list:
    if str(year) in file:
        print(file)


df_2019=pd.read_csv()

