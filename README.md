# GomokuAI 🤖

Welcome to the Gomoku AI project! This project features an interactive game of Gomoku, also known as Five in a Row, where players aim to place five of their marks in a horizontal, vertical, or diagonal row on a 15x15 board. The project showcases two graphical user interfaces (GUIs) for playing the game: a basic GUI built with Tkinter and a more interactive and visually appealing version using Pygame. Additionally, the project includes an AI opponent implemented in `GomukuAI.py`, making the game not only a test of strategy against human opponents but also a challenge against a computer.

## Features

- **Two GUIs**: Choose between a simple, straightforward interface with Tkinter (`gui.py`) and a more dynamic, visually enhanced experience with Pygame (`pygameGUI.py`).
- **Intelligent AI**: The game's AI, detailed in `GomukuAI.py`, uses pattern recognition and strategic evaluation to make moves, providing a challenging opponent that adapts to the flow of the game.
- **Online Playability**: The project is hosted on Replit, allowing you to play the game online without the need for local installation. [Play on Replit](https://replit.com/@shaunakdeo/GomukuAI#main.py)

### Tkinter GUI

The Tkinter version (`gui.py`) provides a basic, easy-to-use interface for playing Gomoku. It features a 15x15 board and allows players to select their moves with a simple click. This GUI supports playing against the AI or another human player in a turn-by-turn fashion. Additionally, it includes options to start a new game or adjust AI settings through a simple menu.

### Pygame GUI

The Pygame version (`pygameGUI.py`) offers a more immersive experience with enhanced graphics and animations. It includes custom game piece visuals, board design, and interactive elements like buttons and hover effects. This version also supports playing against the AI, with moves visually represented on the board for both the player and the AI.

## Gomoku AI Explanation

### Pattern Recognition
- The AI leverages the `Pattern` class to define and utilize patterns, which are essentially configurations of stones on the board with assigned values indicating their strategic significance.
- It dynamically recognizes patterns based on the current game state and recent moves. This includes identifying configurations that are advantageous for winning or necessary for blocking the opponent's winning moves.
- New patterns observed during gameplay are added to a list of known patterns, enhancing the AI's ability to recognize and act upon these configurations in future games.

### Board Evaluation
- The AI evaluates the board by scoring positions based on their potential contribution to winning. This involves assessing the strategic value of individual positions, the formations created by stones, and the significance of open ends and central control.
- A scoring system is utilized where configurations that are closer to winning conditions (such as unblocked lines of stones) are assigned higher values. The evaluation also factors in both immediate threats and opportunities for strategic advantage.
- The AI performs pattern matching against known patterns to adjust the game state score according to the potential impact of these patterns.

### Strategic Move Selection
- To determine the best move, the AI evaluates the impact of each potential move on the game state, considering the perspectives of both the current player and the opponent.
- It prioritizes moves based on several criteria, including their potential to lead to an immediate win, block an opponent's winning strategy, or create opportunities for future wins.
- Moves are also prioritized based on their location relative to the board center, to gain greater control over the board, and their ability to form or extend potential winning patterns.
- The AI identifies immediate threats from the opponent and focuses on moves that either block the opponent's immediate winning opportunities or create two-way threats that require the opponent to defend.

### Learning and Adaptation
- The AI's pattern learning capability allows it to adapt to the opponent's strategies over time, improving its effectiveness in both offense and defense with each game played.
- This adaptive strategy is based on the analysis of specific moves and configurations, enabling the AI to enhance its strategic approach continuously.

### Implementation Details
- The AI uses NumPy for efficient manipulation of game state arrays, enabling quick evaluation of possible moves and the overall game state.
- It methodically evaluates all potential moves on the board, selecting the move with the highest score based on its comprehensive evaluation criteria.
- Special functions are employed to identify immediate win or loss scenarios, allowing the AI to act decisively in situations where an immediate win is possible or necessary to block the opponent's win.
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
