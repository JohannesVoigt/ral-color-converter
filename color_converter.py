"""Image color converter from RGB to RAL Classic color space."""

from typing import TYPE_CHECKING

import numpy as np
from pandas import read_csv
from PIL import Image
from tqdm import tqdm as pbar

if TYPE_CHECKING:
    from scipy.spatial import KDTree


def load_image(image_path: str) -> Image.Image:
    """Load an image and convert it to RGB."""
    image = Image.open(image_path)
    return image.convert("RGB")


def load_ral_colors(csv_path: str) -> dict[str, tuple[int, int, int]]:
    """Load RAL colors from a CSV file."""
    ral_df = read_csv(csv_path)
    ral_df["RGB"] = ral_df["RGB"].apply(lambda x: tuple(map(int, x.split("-"))))
    return dict(zip(ral_df["RAL"], ral_df["RGB"]))


def get_nearest_ral_color(
    rgb_color: tuple[int, int, int],
    ral_tree: "KDTree",
    ral_rgb_values: list[tuple[int, int, int]],
) -> tuple[int, int, int]:
    """Find the nearest RAL color for a given RGB color."""
    _, index = ral_tree.query(rgb_color)
    return ral_rgb_values[index]


def convert_image_to_ral(
    img_array: np.ndarray,
    ral_tree: "KDTree",
    ral_rgb_values: list[tuple[int, int, int]],
) -> np.ndarray:
    """Convert an image array to RAL colors."""
    height, width, _ = img_array.shape
    new_img_array = np.zeros_like(img_array)

    for i in pbar(range(height), desc="Processing rows"):
        for j in range(width):
            rgb_color = img_array[i, j]
            nearest_ral_color = get_nearest_ral_color(
                rgb_color, ral_tree, ral_rgb_values
            )
            new_img_array[i, j] = nearest_ral_color

    return new_img_array


def save_image(img_array: np.ndarray, output_path: str) -> None:
    """Save an image array to a file."""
    new_image = Image.fromarray(np.uint8(img_array))
    new_image.save(output_path)
