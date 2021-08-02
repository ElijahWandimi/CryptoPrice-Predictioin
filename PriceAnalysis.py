#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:31:38 2021

@author: elijah
"""
# importing the neccessary libraries for analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# libraries configurations
pd.set_option('display.max_columns', None)


# reading the data from csv
prices = pd.read_csv('Train.csv')

# checking the shape and basic description of the data
print(prices.shape)
print(prices.describe())