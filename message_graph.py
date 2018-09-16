#!/usr/bin/python

import sys
import matplotlib.pyplot as plt

data = raw_input("Enter your Message : ")
# spliting complete message into list 
x = data.split()

# Defining empty dictionary 
y ={}
# Storing values from list into Dictionary 
for i in x :
	y[i] = y.get(i,0)+1


# Plotting graph using key, values from dictionary (plt as object)
r= y.items()
a,b = zip(*r)
plt.plot(a,b)
plt.xlabel("Different Type of Words")
plt.ylabel("number of occurance")
plt.scatter(a,b,label="dot plot",s=200)
plt.plot(a,b,label="line plot")
plt.bar(a,b,label="bar plot",color='green')
plt.legend()
plt.grid()
plt.show()

