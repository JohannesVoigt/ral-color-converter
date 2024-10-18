# Image color converter to RAL CLASSIC
This project provides a tool to convert the colors in any image to the closest matching RAL classic colors. The script processes each pixel of the image and replaces its color with the corresponding RAL color based on RGB similarity. This can be useful for image analysis, design consistency, or color standardization in projects involving the RAL color system.

## Features
- Converts image colors to the closest matching RAL classic colors.
- Supports batch processing of images.
- Provides an easy-to-use interface for handling image files and RAL color mapping.
- The RAL color list used in this project is sourced from a [Gist by lunohodov](https://gist.github.com/lunohodov/1995178).

## Installation
1. Clone the Repository:
```bash
git clone https://github.com/your-username/image-ral-converter.git
cd image-ral-converter
```
2. Create and Activate a Virtual Environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install Dependencies: Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

## Usage
Load your image(s) in the *images* folder and the tool will automatically map its colors to the nearest RAL equivalents by running the main script. Example usage:
```bash
python convert_image.py
```
