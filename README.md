# Rock-Paper-Scissors Game with Real-Time Hand Gesture Recognition

A fun and interactive implementation of the classic Rock-Paper-Scissors game, allowing a user to play against the computer using **hand gestures** captured through a webcam. This project leverages computer vision to provide a hands-free gaming experience.

-----

## ✨ Features

  * **Real-Time Hand Gesture Recognition:** Accurately detects and classifies the user's hand sign (Rock, Paper, or Scissors) using the MediaPipe framework.
  * **Interactive Gameplay:** Provides real-time visual feedback, displaying both the user's and the computer's choice.
  * **Performance Metrics:** Displays the current Frames Per Second (**FPS**) to monitor performance.
  * **Statistics Tracking:** Persistent tracking of the user's score, including **Wins, Losses, Total Rounds**, and a calculated **Win Percentage**.
  * **User-Friendly Controls:** Simple keyboard commands to start and quit the game.

-----

## 🛠️ Requirements & Installation

This project requires **Python 3.12** or newer and a connected webcam.

### 1\. Installation

Install the required Python packages using `pip`. The project relies on OpenCV for video processing and MediaPipe for hand tracking.

```bash
pip install opencv-python mediapipe numpy
```

### 2\. How to Run

1.  Ensure your webcam is connected and working.
2.  Run the main Python script from your terminal:

<!-- end list -->

```bash
python main.py
```

-----

## 🎮 Usage

Once the script is running and your webcam feed appears:

| Action | Key Press |
| :--- | :--- |
| **Start/Play** | `d` (for "detect" or "deal") |
| **Quit Game** | `q` (for "quit") |

Make your hand gesture clearly in front of the camera. The game will automatically detect your choice, display the computer's choice, and announce the winner of the round.

-----

## 💻 Project Structure

The core logic is contained within a single file.

| File | Description |
| :--- | :--- |
| `main.py` | Contains all the game logic, webcam capture, hand detection (MediaPipe), gesture classification, and score tracking. |
| `README.md` | This file. |

-----

## 🔍 Code Deep Dive (How It Works)

*(**NOTE:** I could not retrieve the source code, so the sections below are placeholders based on the necessary implementation details. You should fill in the specifics.)*

### Hand Gesture Logic

The project uses MediaPipe's hand tracking solution to identify the landmarks (key points) on the user's hand. The final gesture (Rock, Paper, or Scissors) is determined by analyzing the positions of these landmarks.

**Gesture Mapping (To be filled from code):**

  * **Rock:** Defined by... *(e.g., all fingers closed/flexed).*
  * **Paper:** Defined by... *(e.g., all fingers fully extended).*
  * **Scissors:** Defined by... *(e.g., the index and middle fingers extended, and others closed).*

### Game Logic

The game logic is handled by a standard conditional system where the computer's choice is randomly generated, and the outcome is decided by comparing the two choices:

```python
# Pseudo-Code for Determining Winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "User Wins"
    else:
        return "Computer Wins"
```

-----

## 📜 License

This project is open source and available under the **MIT License**.
