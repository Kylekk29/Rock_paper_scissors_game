[English](README.md) | **简体中文**

# 石头剪刀布（Rock Paper Scissors）

经典游戏的三个版本，从最简单到最复杂。三个版本都在[发布页](https://github.com/Kylekk29/Rock_Paper_Scissors/releases)提供可直接运行的 Windows 程序。

| 文件夹 | 版本 | 入口 | Windows 下载 |
|---|---|---|---|
| `Rock_Paper_Scissors_Game_CLI/` | 命令行 | `CLI.py` | `RockPaperScissors-CLI.exe` |
| `Rock_Paper_Scissors_Game_GUI/` | Tkinter 窗口 | `GUI.py` | `RockPaperScissors-GUI.exe` |
| `Rock_Paper_Scissors_Game_hand/` | 摄像头手势游戏（OpenCV + MediaPipe） | `main.py` | `RockPaperScissors-Hand.exe` |

## 从源码运行

命令行版和图形界面版只需要 Python 3（图形界面使用内置的 `tkinter`）。

```bash
python Rock_Paper_Scissors_Game_CLI/CLI.py
python Rock_Paper_Scissors_Game_GUI/GUI.py
```

手势版需要摄像头，以及 `requirements.txt` 中的软件包：

```bash
pip install -r requirements.txt
python Rock_Paper_Scissors_Game_hand/main.py
```

按 `d` 玩一局，按 `q` 退出。详情见 [`Rock_Paper_Scissors_Game_hand/README.md`](Rock_Paper_Scissors_Game_hand/README.md)。它读取默认摄像头（编号 0）。

## 手势版

通过摄像头捕捉你的手势，与电脑对战：

- 用 MediaPipe 手部关键点实时识别石头 / 布 / 剪刀
- 屏幕上显示 FPS
- 实时统计：胜、负、总局数和胜率

## 自己构建可执行文件

```bash
pip install pyinstaller
pyinstaller --onefile --console  --name RockPaperScissors-CLI  Rock_Paper_Scissors_Game_CLI/CLI.py
pyinstaller --onefile --windowed --name RockPaperScissors-GUI  Rock_Paper_Scissors_Game_GUI/GUI.py
pyinstaller --onefile --console  --name RockPaperScissors-Hand --collect-data mediapipe --collect-binaries mediapipe ^
  --exclude-module jax --exclude-module jaxlib --exclude-module scipy Rock_Paper_Scissors_Game_hand/main.py
```

## 许可证

MIT，见 [LICENSE](LICENSE)。
