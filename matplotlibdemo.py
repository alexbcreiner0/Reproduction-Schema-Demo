import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, output_filename):
    # Set up Matplotlib figure
    fig, ax = plt.subplots(figsize=(5, 5))  # You can adjust the figure size as needed

    # Hide axes
    ax.axis('off')

    # Add text to the figure
    ax.text(0.5, 0.5, text, ha='center', va='center', fontsize=12, color='black')  # Adjust fontsize as needed

    # Adjust layout to minimize margins
    plt.tight_layout(pad=0)

    # Save the figure to a temporary file
    temp_filename = 'temp_figure.png'
    plt.savefig(temp_filename, bbox_inches='tight', pad_inches=0, transparent=True)

    # Close the Matplotlib figure
    plt.close()

    # Open the saved image using Pillow
    img = Image.open(temp_filename)
    
    # Crop the image to remove any extra transparent space
    bbox = img.getbbox()
    img_cropped = img.crop(bbox)

    # Save the final cropped image
    img_cropped.save(output_filename, format='PNG')

    # Remove the temporary file
    import os
    os.remove(temp_filename)

if __name__ == "__main__":
    # Replace 'Your text goes here' with the desired text
    text_content = 'Your text goes here'

    # Replace 'output_image.png' with the desired output filename
    output_filename = 'output_image.png'

    create_text_image(text_content, output_filename)
    print(f"Image saved as {output_filename}")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, output_filename):
    # Set up Matplotlib figure
    fig, ax = plt.subplots(figsize=(5, 5))  # You can adjust the figure size as needed

    # Hide axes
    ax.axis('off')

    # Add text to the figure
    ax.text(0.5, 0.5, text, ha='center', va='center', fontsize=12, color='black')  # Adjust fontsize as needed

    # Adjust layout to minimize margins
    plt.tight_layout(pad=0)

    # Save the figure to a temporary file
    temp_filename = 'temp_figure.png'
    plt.savefig(temp_filename, bbox_inches='tight', pad_inches=0, transparent=True)

    # Close the Matplotlib figure
    plt.close()

    # Open the saved image using Pillow
    img = Image.open(temp_filename)
    
    # Crop the image to remove any extra transparent space
    bbox = img.getbbox()
    img_cropped = img.crop(bbox)

    # Save the final cropped image
    img_cropped.save(output_filename, format='PNG')

    # Remove the temporary file
    import os
    os.remove(temp_filename)

if __name__ == "__main__":
    # Replace 'Your text goes here' with the desired text
    text_content = 'Your text goes here'

    # Replace 'output_image.png' with the desired output filename
    output_filename = 'output_image.png'

    create_text_image(text_content, output_filename)
    print(f"Image saved as {output_filename}")
