import numpy as np
import matplotlib.pyplot as plt
    
x = [1, 2, 2, 4]
y = [95, 38, 54, 35]
labels = ['Geeks1', 'Geeks2', 'Geeks3', 'Geeks4']
  
plt.plot(x,y,'.b')
  
# You can specify a rotation for the tick
# labels in degrees or with keywords.
plt.xticks([1,2.5], rotation ='vertical')
  
# Pad margins so that markers don't get 
# clipped by the axes
plt.margins(0.2)
  
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom = 0.15)
plt.show()
