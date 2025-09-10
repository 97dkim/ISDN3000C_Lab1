# Webcam ASCII Art

This project captures video from your webcam, processes each frame, and converts it into ASCII art using Python libraries OpenCV and Pillow. The ASCII representation is printed to the console in real-time.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the script files to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Create a `requirements.txt` file (if not present) and include the following dependencies:

    ```
    opencv-python>=4.5.1
    Pillow>=8.0.0
    numpy>=1.19.0
    ```

4. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Make sure your webcam is connected and functioning.
2. Run the script `webcam_ascii_art.py` using Python:

    ```bash
    python webcam_ascii_art.py
    ```

3. The script will capture video from the webcam and continuously convert it into ASCII art.
4. Press the 'q' key to exit the program.

## Functionality

- The program uses OpenCV to capture frames from your webcam.
- Each frame is converted to a Pillow image for processing.
- The image is resized and converted to grayscale, then transformed into ASCII art based on pixel brightness.
- ASCII art is printed in real-time in the console.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository or create a pull request with your improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.