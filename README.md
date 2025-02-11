# Image Color Converter to RAL CLASSIC
This project provides a tool to convert the colors in any image to the closest matching RAL classic colors using a nearest-neighbor search on a k-d tree. The script processes each pixel of the image and replaces its color with the corresponding RAL color based on RGB similarity. This can be useful for image analysis, design consistency, or color standardization in projects involving the RAL color system.

Example:
<p align="center">
  <img src="images/example3.jpg" width="350" alt="Original image">
  <img src="converted/example3_ral.jpg" width="350" alt="Converted image">
</p>
<p align="center">
  <b>Original Image</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Converted Image</b>
</p>


## Features
- Converts image colors to the closest matching RAL classic colors using a nearest-neighbor search on a k-d tree.
- Supports batch processing of images.
- Provides an easy-to-use interface for handling image files and RAL color mapping.
- The RAL color list used in this project is sourced from a [Gist by lunohodov](https://gist.github.com/lunohodov/1995178).

## Installation
1. Clone the Repository:
```bash
git clone https://github.com/JohannesVoigt/ral-color-converter.git
cd ral-color-converter
```
2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
```
3. Activate the virtual environment
* On Linux
```
source venv/bin/activate
```
* On Windows
```
venv\Scripts\activate
```
4. Install Dependencies: Install the required Python libraries by running
```bash
pip install .
```

## Usage
Load your image(s) in the *images* folder and the tool will automatically map its colors to the nearest RAL equivalents by running the main script. Example usage:
' On Linux
```bash
python run_collor_converter.py
```
* On Windows
```bash
python .\run_color_converter.py
```
