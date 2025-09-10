import cv2
from PIL import Image
import numpy as np

def resize_and_convert_to_grayscale(image, target_width=100):
    """Resize the image while maintaining aspect ratio and convert to grayscale."""
    aspect_ratio = image.height / image.width
    target_height = int(target_width * aspect_ratio)
    resized_image = image.resize((target_width, target_height), Image.LANCZOS)
    grayscale_image = resized_image.convert("L")
    return grayscale_image

def pixel_to_character(pixel_value, ascii_chars=' .:-=+*#%@'):
    """Map a grayscale pixel value to the corresponding character in a ramp string."""
    if not (0 <= pixel_value <= 255):
        raise ValueError("Pixel value must be between 0 and 255.")
    
    num_chars = len(ascii_chars)
    index = int(pixel_value / 255 * (num_chars - 1))
    return ascii_chars[index]

def generate_ascii_art(image):
    """Generate ASCII art from a Pillow image."""
    ascii_art = ""
    for y in range(image.height):
        for x in range(image.width):
            pixel_value = image.getpixel((x, y))
            ascii_char = pixel_to_character(pixel_value)
            ascii_art += ascii_char
        ascii_art += "\n"
    return ascii_art

def main():
    # Initialize webcam capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Convert the frame from BGR (OpenCV format) to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Create a Pillow image from the frame
            pil_image = Image.fromarray(frame_rgb)

            # Resize and convert the image to grayscale
            processed_image = resize_and_convert_to_grayscale(pil_image, target_width=100)

            # Generate ASCII art from the processed image
            ascii_art = generate_ascii_art(processed_image)
            
            # Clear the console before printing
            print("\033[H\033[J", end='')

            # Print ASCII art to the console
            print(ascii_art)

            # Press 'q' on the keyboard to exit the webcam capture
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the webcam and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()