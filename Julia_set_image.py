import numpy as np
import matplotlib.pyplot as plt


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


# Define the boundaries of the plot
X_MIN, X_MAX, Y_MIN, Y_MAX = -2, 2, -2, 2

# Define the threshold for the Julia set
THRESHOLD = 0.1

# Define the width and height of the image
WIDTH, HEIGHT = 400, 400

# Choose the colormap for the plot
CMAP = 'magma'

# Define the number of iterations for the Julia set calculation
ITERATIONS = 500

# Define the complex parameter for the Julia set
C = -0.8 + 0.156j


# Initialize the image array
image = np.zeros((WIDTH, HEIGHT))

# Iterate over each pixel in the image
for x in range(WIDTH):
    for y in range(HEIGHT):
        # Convert pixel coordinates to complex numbers in the specified range
        real = X_MIN + (x / WIDTH) * (X_MAX - X_MIN)
        imag = Y_MIN + (y / HEIGHT) * (Y_MAX - Y_MIN)
        z = complex(real, imag)
        # Compute the color based on the number of iterations for the current pixel
        color = julia(C, z, ITERATIONS)
        # Set the pixel value in the image array based on the color and threshold
        image[x, y] = 1 if color / ITERATIONS < THRESHOLD else 0

# Plot the Julia set
plt.imshow(image, cmap=CMAP, extent=(X_MIN, X_MAX, Y_MIN, Y_MAX))
# Optionally, save the plot as an image file
# plt.savefig("julia_set.png", dpi=1200)  # Save the plot as a PNG file with high resolution
# Show the plot
plt.show()
