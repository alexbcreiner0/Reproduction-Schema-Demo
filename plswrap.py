import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Add the first text
text1 = 'This is the first text'
ax.text(0.1, 0.5, text1, fontsize=12, transform=fig.transFigure)

# Add the second text next to the first one
text2 = 'This is the second text'
ax.text(0.1, 0.5, text2, fontsize=12, transform=fig.transFigure, ha='left', va='center')

plt.show()
