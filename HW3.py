#!/usr/bin/env 
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:17:09 2020

@author: dangruber, sljohansen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so
#we want to use a fitting function from scipy.optimize

plt.close("all")
state_list=[]
lat_list=[]
long_list=[]
temp_list = []
#we are going to put the state names, latitudes, longitudes, and temperatures in these lists

#LOOK AT THE DATA FILE BEFORE YOU START. MAKE SURE YOU KNOW WHAT'S IN THERE.

with open("StateYlyTempAndLocData.csv","r") as csv_file:
    #this opens the desired file and assigns the file contents to the variable "csv_file"
    #the "r" indicates that we are just reading this file, "w" would let us write to it
    headers=csv_file.readline()
    #We actually will use these headers again, we are trying to fit a line to the plot of the temps (y) over the years (x)

    
    for line in csv_file:
        #this loops through every line in the file
        state_data = line.split(",")
#        print(state_data)


        for i in range(len(state_data)):
            state_data[i] = state_data[i].strip()
        # This line just strips out any unwanted spaces and characters from
        # each element of state_data.
#        print(state_data)
        
        state_list.append(str(state_data[0]))
        
        lat_list.append(float(state_data[1]))
        
        long_list.append(float(state_data[2])*(-1))
        
        temps = []
        for i in state_data[3:]:
            if i != '':
                temps.append(float(i))
        temp_list.append(temps)
        # The numbers in the file are in '', so they are strings. Numbers
        # should be processed as floats or integers, so we have to change them.

        
#print(state_list)
#print(lat_list)
#print(long_list)
#print(temp_list)
#print out your lists to make sure they contain the correct data before continuing. 


def fit_eq(x, m, b):
    return (m*x)+b
#We want to fit a trend line to each set of temperatures. This is the equation that will be called later in the curve_fit function.


curve_list = []
years = headers.split(',')

#This takes the headers of all the columns and turns it into a list. 
for i in range(len(years)):
    years[i] = years[i].strip()
#again, this removes unwanted formatting from the list

years = years[3:]
#this pulls out just the actual years

plot_year = []
# Turn all the years into floats so we can use them as numbers
for year in years:
    plot_year.append(float(year))

for i in temp_list:
    #this will loop through the list of temps for each state
    fit_years = plot_year[0:len(i)]
    #this makes sure the years and temps are the same length, so Alaska won't be a problem

    fit_years.reverse()
    i.reverse()

    
    popt,pcov = so.curve_fit(fit_eq,fit_years,i)
    
#    print(popt)
    curve_list.append(popt[0])
    

plt.scatter(long_list,lat_list,c=curve_list,cmap='seismic')        
plt.title("Locations of the Centers of US States")
plt.xlabel("Longitudes")
plt.ylabel("Latitudes")
plt.savefig("Day_3_HW_Answer")
