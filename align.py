import matplotlib.pyplot as plt
from matplotlib import rc

def render_latex(latex_code):
    # Set up matplotlib to use LaTeX for rendering
    rc('text', usetex=True)
    
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot an empty graph (we don't actually need a graph, just a canvas for rendering LaTeX)
    ax.plot([])

    # Display the LaTeX code in an array environment
    ax.text(0.5, 0.5, f'\\[\\begin{{array}}{{rcl}}{latex_code}\\end{{array}}\\]', fontsize=14, va='center', ha='center')

    # Remove x and y ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Display the plot
    plt.show()

# Example LaTeX code in an align environment
latex_code = r'''
x &= 2 + 3 \\
y &= 5 - 1 \\
z &= 4 \times 2
'''

# Render and display the LaTeX code
render_latex(latex_code)
