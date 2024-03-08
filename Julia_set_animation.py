import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def julia(c, z, max_iter):
    """
    Compute the number of iterations until the Julia sequence escapes or reaches maximum iterations.

    Parameters:
        c (complex): The complex parameter defining the Julia set.
        z (complex): The initial complex number.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The number of iterations until escape or reaching the maximum iterations.
    """
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter


def generate_frame(frame, c, colormap):
    """
    Generate a frame for the Julia set animation.

    Parameters:
        frame (int): The current frame number.
        c (complex): The complex parameter defining the Julia set.
        colormap (str): The colormap to use for plotting.

    Returns:
        tuple: The plotted image.
    """
    plt.clf()  # Clear the current plot
    image = np.zeros((WIDTH, HEIGHT))  # Initialize the image array
    # Vary 'max_iter' from 1 to 1000 linearly over 100 frames
    current_max_iter = int(1 + (frame / 100) * 999)
    # Iterate over each pixel in the image
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Convert pixel coordinates to complex numbers in the specified range
            real = X_MIN + (x / WIDTH) * (X_MAX - X_MIN)
            imag = Y_MIN + (y / HEIGHT) * (Y_MAX - Y_MIN)
            z = complex(real, imag)
            # Compute the color based on the number of iterations for the current pixel
            color = julia(c, z, current_max_iter)
            # Set the pixel value in the image array based on the color and threshold
            image[x, y] = 1 if color / current_max_iter < THRESHOLD else 0
    # Plot the image using the specified colormap and range
    plt.imshow(image, cmap=colormap, extent=(X_MIN, X_MAX, Y_MIN, Y_MAX))
    # Remove x and y axis labels, ticks, and the coordinate system
    #plt.axis('off')
    return (plt.imshow(image, cmap=colormap, extent=(X_MIN, X_MAX, Y_MIN, Y_MAX)),)


# Define the boundaries of the plot
X_MIN, X_MAX, Y_MIN, Y_MAX = -2, 2, -2, 2

# Define the threshold for the Julia set
THRESHOLD = 0.1

# Define the width and height of the image
WIDTH, HEIGHT = 400, 400

# Choose the colormap for the plot
CMAP = 'magma'

# Define the number of iterations for the Julia set calculation
ITERATIONS = 100

# Define the speed of the animation (in milliseconds per frame)
SPEED = 100

# Define the complex parameter for the Julia set
C = -0.8 + 0.156j


# Create a figure for the animation
fig = plt.figure(figsize=(8, 8))
# Create the animation object
anim = animation.FuncAnimation(fig, generate_frame, fargs=(C, CMAP), frames=ITERATIONS, interval=SPEED, repeat=False)

# Save the animation as a GIF
#anim.save('julia_set_max_iter_variation.gif', writer='imagemagick', fps=5)

# Display the animation
plt.show()
