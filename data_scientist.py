import numpy as mp
import matplotlib as mpl
mpl.use('tkagg')
import pylab as pl

# Use numpy to load the data contained in the file
# 'data.txt' into a 2-D array called data
data = np.loadtxt('data.txt')
# plot the first column as x, and second column as y
pl.plot(data[:,0], data[:,1])
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(9., 26.)
pl.show()

