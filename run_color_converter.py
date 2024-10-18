"""Run the image color converter from RGB to RAL Classic color space."""

import argparse
import os
import sys

import numpy as np
from scipy.spatial import KDTree

import color_converter as cc


def process_image(
    img_path: str,
    ral_tree: KDTree,
    ral_rgb_values: list[tuple[int, int, int]],
    output_folder: str,
    suffix: str = "",
) -> None:
    """Process a single image and save the converted image."""
    try:
        img = cc.load_image(img_path)
        img_array = np.array(img)
        new_img_array = cc.convert_image_to_ral(img_array, ral_tree, ral_rgb_values)

        img_filename, img_ext = os.path.splitext(os.path.basename(img_path))
        output_filename = f"{img_filename}{suffix}{img_ext}"
        output_path = os.path.join(output_folder, output_filename)
        cc.save_image(new_img_array, output_path)
        print(f"Processed and saved: {output_path}")
    except FileNotFoundError:
        print(f"File not found: {img_path}")
    except IOError:
        print(f"IO error occurred while processing {img_path}")
    except ValueError as e:
        print(f"Value error: {e} while processing {img_path}")


def main(args: argparse.Namespace) -> int:
    """Run the image color converter."""
    input_folder = args.input
    output_folder = args.output
    image_file = args.file
    suffix = args.suffix

    # Create paths (and folders)
    dir_ = os.path.dirname(os.path.abspath(__file__))
    colors_path = os.path.join(dir_, "ral_classic.csv")
    os.makedirs(output_folder, exist_ok=True)

    # Load RAL colors
    ral_colors = cc.load_ral_colors(colors_path)
    ral_rgb_values = list(ral_colors.values())
    ral_tree = KDTree(ral_rgb_values)

    # Get images to process
    if image_file:
        img_paths = [os.path.join(input_folder, image_file)]
    else:
        img_paths = [
            os.path.join(input_folder, f)
            for f in os.listdir(input_folder)
            if f.endswith((".jpg", ".jpeg", ".png", ".webp"))
        ]

    # Process images
    for idx, img_path in enumerate(img_paths, start=1):
        img_filename = os.path.basename(img_path)
        print(f"Processing file {idx}/{len(img_paths)}: {img_filename}")
        process_image(img_path, ral_tree, ral_rgb_values, output_folder, suffix)

    return 0


if __name__ == "__main__":
    default_in = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    default_out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "converted")
    default_file = os.path.join(default_in, "example1.jpg")

    parser = argparse.ArgumentParser(
        description="Convert images from RGB to RAL Classic color space."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default=default_in,
        help="Input folder containing images.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=default_out,
        help="Output folder to save converted images.",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Specific image file to convert.",
    )
    parser.add_argument(
        "-s",
        "--suffix",
        type=str,
        default="_ral",
        help="Suffix to append to the filename before the extension.",
    )

    sys.exit(main(parser.parse_args()))
