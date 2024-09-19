import matplotlib.pyplot as plt
import numpy as np

class10=np.array([97,90,92,80,77])
class12=np.array([91,86,92,92,84])
per_10=np.sum(class10)/5
per_12=np.sum(class12)/5
grad=83.11

x=["highschool","secodry school","graduation"]
y=[per_10,per_12,grad]
plt.title("student graph")
plt.plot(x,y)
plt.show()