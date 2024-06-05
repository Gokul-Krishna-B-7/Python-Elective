import matplotlib.pyplot as plt

# Sample data points
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]

# Create the stem plot without using LineCollection
markerline, stemlines, baseline = plt.stem(x, y, use_line_collection=False)

# Customize the markerline
markerline.set_markerfacecolor('blue')  # Set the face color of the markers
markerline.set_markeredgecolor('black') # Set the edge color of the markers
markerline.set_marker('o')              # Change the marker style

# Customize the stemlines
for stem in stemlines:
    stem.set_color('green')             # Set the color of the stem lines
    stem.set_linewidth(2)               # Set the width of the stem lines
    stem.set_linestyle('--')            # Set the style of the stem lines

# Customize the baseline
baseline.set_color('red')               # Set the color of the baseline
baseline.set_linewidth(1.5)             # Set the width of the baseline

# Display the plot
plt.title('Customized Stem Plot')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.show()
