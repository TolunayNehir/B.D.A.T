import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tkinter as ttk
from tkinter import *
#matplotlib.use('Agg')


def json():
    file=input("Filename:")
    df = pd.read_json('data.csv')
    print("Data has been dataframed")
    print("Type 1 first 5,2 last 5,3 all variables ")
    type1=input("Type:")
    if type1==1:
        print(df.head())
    elif type1==2:
        print(df.tail())
    elif type1==3:
        print(df)
    else:
        print("Not Found")
    plot=input("Do you want plotting")
    if plot=="yes":
        plotype=input("Plotting type 1 classic,2 customized")
        if plottype=="classic":
            plotting(df,"classic")
        elif plottype=="cutomized":
            plotting(df,"customized")
    else:
        print("Analyze finished")
def csv():
    file=input("Filename:")
    df = pd.read_csv('data.csv')
    print("Data has been dataframed")
    print("Type 1 first 5,2 last 5,3 all variables ")
    type1=input("Type:")
    if type1==1:
        print(df.head())
    elif type1==2:
        print(df.tail())
    elif type1==3:
        print(df)
    else:
        print("Not Found")
    plot=input("Do you want plotting")
    if plot=="yes":
        plotype=input("Plotting type 1 classic,2 customized")
        if plottype=="classic":
            plotting(df,"classic")
        elif plottype=="cutomized":
            plotting(df,"customized")
    else:
        print("Analyze finished")

def plotting(df,plotype):
    if plotype=="classic":
        print("plotting started:")
        df.plot()
        plt.show()
    elif plotype=="customized":
        x=input("X:")
        y=input("Y:")
        kind=input("Kind:")
        print("plotting started:")
        df.plot(kind=str(kind),x=str(x),y=str(y))
        plt.show()


print("File Type: 1 csv,2 json")
filetype=input("File Type:")
if filetype=="1":
    csv()
elif filetype=="2":
    json()
else:
    print("Not found")


