# Rock Paper Scissors

Three versions of the classic game, from simplest to most advanced. All three are available as ready-to-run Windows programs on the [Releases page](https://github.com/Kylekk29/Rock_paper_scissors_game/releases).

| Folder | Version | Entry point | Windows download |
|---|---|---|---|
| `Rock_Paper_Scissors_Game_CLI/` | Command line | `CLI.py` | `RockPaperScissors-CLI.exe` |
| `Rock_Paper_Scissors_Game_GUI/` | Tkinter window | `GUI.py` | `RockPaperScissors-GUI.exe` |
| `Rock_Paper_Scissors_Game_hand/` | Webcam hand-gesture game (OpenCV + MediaPipe) | `main.py` | `RockPaperScissors-Hand.exe` |

## Run from source

The CLI and GUI versions need only Python 3 (the GUI uses the built-in `tkinter`).

```bash
python Rock_Paper_Scissors_Game_CLI/CLI.py
python Rock_Paper_Scissors_Game_GUI/GUI.py
```

The hand-gesture version needs a webcam and the packages in `requirements.txt`:

```bash
pip install -r requirements.txt
python Rock_Paper_Scissors_Game_hand/main.py
```

Press `d` to play a round and `q` to quit. See [`Rock_Paper_Scissors_Game_hand/README.md`](Rock_Paper_Scissors_Game_hand/README.md) for details. It reads the default camera (index 0).

## Hand-gesture version

Play against the computer using hand gestures captured through your webcam:

- Real-time rock / paper / scissors recognition with MediaPipe hand landmarks
- On-screen FPS counter
- Running statistics: wins, losses, total rounds and win percentage

## Build the executables yourself

```bash
pip install pyinstaller
pyinstaller --onefile --console  --name RockPaperScissors-CLI  Rock_Paper_Scissors_Game_CLI/CLI.py
pyinstaller --onefile --windowed --name RockPaperScissors-GUI  Rock_Paper_Scissors_Game_GUI/GUI.py
pyinstaller --onefile --console  --name RockPaperScissors-Hand --collect-data mediapipe --collect-binaries mediapipe ^
  --exclude-module jax --exclude-module jaxlib --exclude-module scipy Rock_Paper_Scissors_Game_hand/main.py
```

## License

MIT, see [LICENSE](LICENSE).
