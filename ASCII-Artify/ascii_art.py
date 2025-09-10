import sys
import argparse
from PIL import Image

# Define the default character ramp
DEFAULT_ASCII_CHARS = " .:-=+*#%@"

def resize_and_convert_to_grayscale(image, target_width=100):
    """Resize the image while maintaining aspect ratio and convert to grayscale."""
    aspect_ratio = image.height / image.width
    target_height = int(target_width * aspect_ratio)
    resized_image = image.resize((target_width, target_height), Image.LANCZOS)  # Use LANCZOS for better quality
    grayscale_image = resized_image.convert("L")
    return grayscale_image

def pixel_to_character(pixel_value, ascii_chars):
    """Map a grayscale pixel value to the corresponding character in a ramp string."""
    if not (0 <= pixel_value <= 255):
        raise ValueError("Pixel value must be between 0 and 255.")
    
    num_chars = len(ascii_chars)
    index = int(pixel_value / 255 * (num_chars - 1))  # Scale pixel value to ramp indices
    return ascii_chars[index]

def main(image_path, target_chars):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File not found at '{image_path}'")
        return

    # Resize the image to 100 characters wide and convert to grayscale
    processed_image = resize_and_convert_to_grayscale(image, target_width=target_chars)

    # Iterate through each pixel and create ASCII art
    ascii_art = ""
    for y in range(processed_image.height):
        for x in range(processed_image.width):
            pixel_value = processed_image.getpixel((x, y))  # Get the pixel brightness
            ascii_char = pixel_to_character(pixel_value, DEFAULT_ASCII_CHARS)  # Convert to character
            ascii_art += ascii_char
        ascii_art += "\n"  # New line at the end of each row

    # Print the final ASCII art to the console
    print(ascii_art)

if __name__ == "__main__":
    # Setup command-line argument parsing using argparse
    parser = argparse.ArgumentParser(description='Convert an image to ASCII art.')
    parser.add_argument('image_path', help='Path to the image file to be converted.')
    parser.add_argument('--chars', type=int, default=100, help='Number of characters wide for the output ASCII art (default: 100).')

    args = parser.parse_args()

    main(args.image_path, args.chars)