# Julia Set

Welcome to the Julia Set repository! Explore the fascinating world of fractals and artistic visualization.
<br/><br/>

## Description

The Julia Set is a set of complex numbers that exhibits fractal-like behavior when iterated using a simple algorithm. Named after the French mathematician Gaston Julia, the Julia Set showcases intricate patterns and self-similar structures.

For more information, you can refer to the [Wikipedia page](https://en.wikipedia.org/wiki/Julia_set).
<br/><br/>

## Visual Appeal and Artistic Representation

The Julia Set's fractal nature and intricate details make it visually captivating. Artists and mathematicians alike are drawn to its complexity, using it as inspiration for various forms of artistic expression, including digital art and sculptures.
<br/><br/>

## Applications

Beyond its aesthetic appeal, the Julia Set has practical applications in various fields, including computer graphics, image compression, and signal processing. Its self-similar structure and infinite complexity make it valuable for generating visually appealing patterns and textures.
<br/><br/>

## Code

Explore the code used to generate visualizations of the Julia Set. The code is written in Python and utilizes libraries such as matplotlib and numpy.

### Requirements

- Python 3.12
- ImageMagick (only for saving the animation)
- Matplotlib
- Numpy

### Usage (julia_set_animation.py)

1. Clone this repository or download the `julia_set_animation.py` file.
2. Make sure you have Python and the required dependencies installed.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `julia_set_animation.py`.
5. Run the script using the following command:

    ```bash
    python julia_set_animation.py
    ```

6. The script will generate an animation of the Julia Set and display it in a new window.

### Usage (julia_set_image.py)

1. Clone this repository or download the `julia_set_visualization.py` file.
2. Make sure you have Python and the required dependencies installed.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `julia_set_visualization.py`.
5. Run the script using the following command:

    ```bash
    python julia_set_visualization.py
    ```

6. The script will generate a plot of the Julia Set and display it in a new window.

### Customization

You can customize the behavior and appearance of the animation by modifying the parameters in the script:

- `X_MIN`, `X_MAX`, `Y_MIN`, `Y_MAX`: Define the region of the complex plane to visualize.
- `THRESHOLD`: Control the threshold for coloring pixels in the Julia Set.
- `WIDTH`, `HEIGHT`: Set the dimensions of the image.
- `CMAP`: Choose the colormap for the visualization.
- `ITERATIONS`: Define the number of frames in the animation.
- `SPEED`: Set the interval between frames in milliseconds.

You can also change the complex number `C` to generate different Julia Sets. Simply modify the `C` variable to a different complex number of your choice.

### Saving the Animation

You can save the animation as a GIF by uncommenting the following line in the script:

```python
# anim.save('julia_set_animation.gif', writer='imagemagick', fps=5)
```

### Saving the Image

You can save the plot as an image file by uncommenting the following line in the script:

```python
# plt.savefig("julia_set.png", dpi=1200)  # Save the plot as a PNG file with high resolution
```
<br/>

## Samples

Below is a sample image generated using the codes in this repository:

![Julia Set Image](https://github.com/mathmeetsart/Julia-Set/assets/157393083/d7afb20e-d7de-45ab-b735-01611480b992)



Explore the code, create your own visualizations, and let the beauty of the Julia Set inspire your artistic endeavors!
<br/><br/>

## Contribution Guidelines

Contributions to this project are welcome! If you would like to contribute, please follow these guidelines:
- Fork the repository
- Create a new branch for your feature or bug fix
- Make your changes
- Test your changes thoroughly
- Submit a pull request
<br/><br/>

## Contact Information

For questions, feedback, or collaboration opportunities, feel free to reach out to me:
- Email: mathmeetsart01@gmail.com
- Instagram: [art_meets_math](https://www.instagram.com/art_meets_math/)

---

This repository is a subrepository of [Math Meets Art](https://www.instagram.com/art_meets_math/), which is aimed at making math accessible, intriguing, and visually captivating for everyone. Through this platform, I aim to demonstrate that math is not merely about numbers but a realm of boundless creativity and discovery. Each piece of art presented here also offers an opportunity to learn and appreciate the underlying mathematical concepts.
