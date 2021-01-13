import math #it will be useful for converting from degrees to radians
import numpy as np  #this library is very famous in dealing with matrices.
import matplotlib.pyplot as plt #this library is for making graphs and its commands are somewhat close to MatLab

x0=float(input("Enter the initial x position in cm: "))    #take input the initial x position in cm (for testing use 0) we also convert the input to float type
y0=float(input("Enter the initial y position in cm: "))    #initial y position in cm (for testing use 0)
theta0=float(input("Enter the initial theta angle in degrees: "))    #initial angle in degrees  (for testing use 0)
theta0=math.radians(theta0) #converting the angle to radians
r=float(input("Enter the wheel radius in cm: ")) #wheel radius in cm (for testing use 4)
l=float(input("Enter base length in cm: ")) #base length in cm (for testing use 2)

dt=0.1  #incremental time in sec

###########
phi1_dot=10 #first wheel speed in degrees/sec
phi2_dot=15 #second wheel speed in degrees/sec
phi1_dot=math.radians(phi1_dot) #converting to radians/s
phi2_dot=math.radians(phi2_dot) #converting to radians/s
t_end=15    #the ending time in sec




t=np.arange(0,t_end+dt,dt)  #making an array which will start from 0 end in t_end (the +dt is because python skips the last number) and increment in dt

theta=theta0+(r/(2*l)*(phi2_dot-phi1_dot))*t    #appling the function from the lecture

x=x0+l*(phi2_dot+phi1_dot)/(phi2_dot-phi1_dot)*(np.sin(theta)-np.sin(theta0))   #appling the function from the lecture

y=y0+l*(phi2_dot+phi1_dot)/(phi2_dot-phi1_dot)*(np.cos(theta0)-np.cos(theta))   #appling the function from the lecture

plt.plot(x,y)   #plot x array vs y array
plt.title("Path of the Robot"+ " (x0="+str(x0)+", y0="+ str(y0)+ ", theta0="+str(theta0)+"(in rad)"+", r="+ str(r)+",and l="+ str(l)+")")  #setting the title and displaying the input from the user
plt.xlabel("x axis in cm")  #setting the horizontal axis name
plt.ylabel("y axis in cm")  #setting the vertical axis name
plt.show()  #Note if this function is not used the plot will not be seen



