# Rock-Paper-Scissors Game with Hand Gesture Recognition

## Introduction

This project implements a Rock-Paper-Scissors game using hand gesture recognition. The game detects hand signs through a webcam and allows a user to play against a computer opponent. The hand gestures are processed in real-time using OpenCV and MediaPipe libraries. 

## Features

- **Hand Gesture Recognition**: Detects and processes hand gestures for rock, paper, or scissors.
- **Real-Time Feedback**: Displays the current frames per second (FPS) and game results on the screen.
- **Statistics Tracking**: Keeps track of wins, losses, and total rounds played.
- **User Instructions**: Provides clear instructions on how to start and quit the game.

## Requirements

- Python 3.12
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- NumPy (for array manipulations)

## How to Run

1. Ensure you have the required libraries installed:
   ```bash
   pip install opencv-python mediapipe numpy
   ```

2. Connect a webcam to your computer.

3. Run the script:
   ```bash
   python your_script_name.py
   ```

4. Press `d` to play the game and `q` to quit.

## Usage

- Make hand gestures in front of the camera to play the game.
- The game will display the computer's choice, your choice, and the outcome of each round along with your win percentage.

## License

This project is open source and available under the MIT License.
