from matplotlib.pyplot import *
from numpy import *


x = linspace(0,1,1000)

def g(x):
	return 1-(1 - exp(-10))*x - exp(-10*x)

infile = open("test.dat","r")
x_ = []
y_ = []

lines = infile.readlines()
for line in lines:
	words = line.split()
	x_.append(words[0])
	y_.append(words[1])


plot(x_,y_,"k-")
plot(x,g(x),"g-")
show()