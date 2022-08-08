import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tkinter as ttk
from tkinter import *
#matplotlib.use('Agg')

def plotting(df,plotype):
    if plotype=="classic":
        print("plotting started:")
        df.plot()
        plt.grid()
        plt.show()
        input("Press Enter to continue...")
    elif plotype=="customized":
        x=input("X:")
        y=input("Y:")
        kind=input("Kind:")
        print("plotting started:")
        df.plot(kind=str(kind),x=str(x),y=str(y))
        plt.grid()
        plt.show()
        input("Press Enter to continue...")

def json():
    file=input("Filename:")
    df = pd.read_json(file)
    print("Data has been dataframed")
    print("Type 1 first 5,2 last 5,3 all variables ")
    type1=input("Type:")
    if type1=="1":
        print(df.head())
    elif type1=="2":
        print(df.tail())
    elif type1=="3":
        print(df.to_string())
    else:
        print("Not Found")
    plot=input("Do you want plotting:")
    if plot=="yes":
        plottype=input("Plotting type 1 classic,2 customized:")
        if plottype=="1":
            plotting(df,"classic")
        elif plottype=="2":
            plotting(df,"customized")
    else:
        print("Analyze finished")
def csv():
    file=input("Filename:")
    df = pd.read_csv(file)
    print("Data has been dataframed")
    print("Type 1 first 5,2 last 5,3 all variables ")
    type1=input("Type:")
    if type1=="1":
        print(df.head())
    elif type1=="2":
        print(df.tail())
    elif type1=="3":
        print(df.to_string())
    else:
        print("Not Found")
    plot=input("Do you want plotting:")
    if plot=="yes":
        plottype=input("Plotting type 1 classic,2 customized")
        if plottype=="1":
            plotting(df,"classic")
        elif plottype=="2":
            plotting(df,"customized")
    else:
        print("Analyze finished")


print("File Type: 1 csv,2 json")
filetype=input("File Type:")
if filetype=="1":
    csv()
elif filetype=="2":
    json()
else:
    print("Not found")
