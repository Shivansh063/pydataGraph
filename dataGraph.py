#!/usr/bin/python
import matplotlib.pyplot  as  plt  
x=["C","python","Java","C++"]
y=[100,30,20,150]

plt.xlabel("name of Languages")
plt.ylabel("No. of Users")
plt.scatter(x,y,label="general word count with dots ")
plt.plot(x,y,label="general word count with line")
plt.legend()

plt.show()




