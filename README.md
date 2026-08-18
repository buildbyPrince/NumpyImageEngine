# Pure NumPy Image Engine

A simple image transformation tool built using pure NumPy array operations without using OpenCV or PIL for image processing.

### Features
- Grayscale: Converts RGB images to grayscale using vectorized math.
- Channel Extraction: Isolates Red, Green, or Blue channels.
- Flip: Flips image horizontally or vertically using array slicing.
- Rotate 90: Rotates image clockwise or counterclockwise using swapaxes.
- Brightness and Contrast: Adjusts lighting and clips values between 0 and 255.
- Metadata: Prints image shape, data type, and min/max pixel values.

### Requirements
- Python 3
- numpy
- matplotlib (only used to load and save image files)

### How to Run
1. Put an image inside the assets folder named sample.jpg
2. Run the main script:
python main.py
