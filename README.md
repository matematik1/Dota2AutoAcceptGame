# 🎮 Dota 2 Auto Accept

An automated Python utility designed to detect when a Dota 2 match is found and automatically accept it for you. Includes a sleek, custom animated pop-up notification designed in Figma.

![Notification Preview](https://raw.githubusercontent.com/matematik1/Dota2AutoAcceptGame/main/img/notification.png)

---

## ✨ Features

- **Automated Match Acceptance:** Scans the screen for the "Accept" button and sends the Enter key automatically.
- **Figma UI Overlay:** Displays a clean, smooth fade-in/fade-out notification pop-up when the game is accepted.
- **Auto-Dependency Installer:** Included batch script automatically checks and installs any missing Python libraries on startup.
- **Window Management:** Automatically brings the Dota 2 window to the front when a match is found.

---

## 🛠️ Requirements

- **OS:** Windows 10 / 11
- **Python:** Python 3.10+ installed and added to PATH.
- **Game Language:** English / Ukrainian / Russian interface supported (depends on your target template in img/).

---

## 🚀 How to Run

### Option 1: Quick Launch (Recommended)
Simply double-click start.bat. 
Note: Run start.bat as Administrator to ensure the script has permissions to send keystrokes to game windows.

The script will automatically check for required dependencies (pyautogui, pillow, keyboard, pygetwindow, opencv-python) and launch main.py.

### Option 2: Manual Launch via Terminal

1. Install dependencies:
   pip install pyautogui pillow keyboard pygetwindow opencv-python

2. Run the application:
   python main.py

---

## 📁 Project Structure

Dota2AutoAcceptGame/

├── img/

│   ├── buttom.png           # Target image of the "Accept Match" button

│   └── notification.png     # Custom UI pop-up exported from Figma

├── main.py                  # Core Python logic

├── start.bat                # Auto-dependency checker & script launcher

└── README.md                # Project documentation

---

## ⚙️ How It Works

1. Window Detection: Checks if the Dota 2 window is running and brings it to focus.
2. Screen Scanning: Continuously scans for img/buttom.png using computer vision (pyautogui with OpenCV confidence matching).
3. Action: Once detected, it simulates pressing the Enter key 3 times to accept the match.
4. Notification: Displays a borderless, transparent overlay with an animated smooth slide and fade effect before exiting.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📜 License

This project is open-source and available under the MIT License.
