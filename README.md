# GomokuAI

Welcome to the Gomoku AI project! This project features an interactive game of Gomoku, also known as Five in a Row, where players aim to place five of their marks in a horizontal, vertical, or diagonal row on a 15x15 board. The project showcases two graphical user interfaces (GUIs) for playing the game: a basic GUI built with Tkinter and a more interactive and visually appealing version using Pygame. Additionally, the project includes an AI opponent implemented in `GomukuAI.py`, making the game not only a test of strategy against human opponents but also a challenge against a computer.

## Features

- **Two GUIs**: Choose between a simple, straightforward interface with Tkinter (`gui.py`) and a more dynamic, visually enhanced experience with Pygame (`pygameGUI.py`).
- **Intelligent AI**: The game's AI, detailed in `GomukuAI.py`, uses pattern recognition and strategic evaluation to make moves, providing a challenging opponent that adapts to the flow of the game.
- **Online Playability**: The project is hosted on Replit, allowing you to play the game online without the need for local installation. [Play on Replit](#replit-link-placeholder)

### Tkinter GUI

The Tkinter version (`gui.py`) provides a basic, easy-to-use interface for playing Gomoku. It features a 15x15 board and allows players to select their moves with a simple click. This GUI supports playing against the AI or another human player in a turn-by-turn fashion. Additionally, it includes options to start a new game or adjust AI settings through a simple menu.

### Pygame GUI

The Pygame version (`pygameGUI.py`) offers a more immersive experience with enhanced graphics and animations. It includes custom game piece visuals, board design, and interactive elements like buttons and hover effects. This version also supports playing against the AI, with moves visually represented on the board for both the player and the AI.

### Gomoku AI

The artificial intelligence for playing Gomoku (`GomukuAI.py`) is a sophisticated component that uses advanced techniques to evaluate the game board, recognize patterns, and determine the best moves. It considers immediate threats, potential wins, and strategic positions, adapting its strategy as the game progresses. The AI is capable of learning new patterns, enhancing its play over time.

## Installation and Usage

To play Gomoku on your local machine, you will need Python installed, along with the Tkinter and Pygame libraries. Follow these steps to get started:

1. **Clone the project** or download the files to your local machine.
2. **Install dependencies**: Ensure you have Python installed, then install Pygame if you wish to use the more interactive GUI.
    - Install Pygame: `pip install pygame`
3. **Run the game**:
    - For Tkinter GUI: `python gui.py`
    - For Pygame GUI: `python pygameGUI.py`

Alternatively, you can play the game online without installation by visiting the Replit project page: [Replit Link Placeholder]

## Contribution

Contributions to the Gomoku AI project are welcome! Whether you're interested in enhancing the AI, improving the GUIs, or fixing bugs, your input can help make this project even better.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you see fit.

---

Enjoy playing Gomoku, and may the best player win!
