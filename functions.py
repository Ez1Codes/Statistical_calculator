import statistics as st
import numpy as np

def mean(data):
    mean = st.mean(data)
    return mean 

def mode(data):
    mode  = st.mode(data)
    return mode  

def median(data):
    medina = st.median(data)
    return median

def stdv(data):
    standv = st.stdev(data)
    return standv
def variance(data):
    variance = st.variance(data)

if __name__ == "__main__":
    mean(data)
    median(data)
    stdv(data)
    variance(data)
