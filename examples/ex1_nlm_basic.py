import matplotlib.pyplot as plt
from nlmpy import nlmpy


nlm = nlmpy.mpd(nRow=50, nCol=50, h=0.75)
# Plot image of terrain above
plt.imshow(nlm)
plt.show()
