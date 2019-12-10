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


# import os
import os

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

