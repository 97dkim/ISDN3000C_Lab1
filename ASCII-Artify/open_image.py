from PIL import Image
import sys

def open_image(image_path):
    try:
        # Open an image file
        with Image.open(image_path) as img:
            img.show()  # This will open the image using the default image viewer
            print(f"Image '{image_path}' opened successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        open_image(image_path)