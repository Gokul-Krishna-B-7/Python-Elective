from matplotlib import pyplot as plt
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
# Function to plot scatter
plt.stem(x, y,use_line_collection=True)
plt.show()