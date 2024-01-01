import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('sample-image.png')
fig,axes =  plt.subplots(2,3,figsize = (7,7))

axes[1][0].imshow(image[:,:,0],cmap='gray') # Red Channel in gray colour
axes[1][1].imshow(image[:,:,1],cmap='gray') # Green Channel in gray colour
axes[1][2].imshow(image[:,:,2],cmap='gray') # Blue Channel in gray colour

plt.tight_layout()   # spaces out the plots 

plt.show()