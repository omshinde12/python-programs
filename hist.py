import matplotlib.pyplot as plt
ages=[2,3,6,87,56,34,76,23,34,56,76]
range=(0,100)
bins=10
plt.hist(ages,bins,range,color='pink',histtype='bar',rwidth=0.8)
plt.xlabel('ages')
plt.ylabel('no.of people')
plt.title('my histrogram')
plt.show()
