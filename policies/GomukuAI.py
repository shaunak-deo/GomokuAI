import numpy as np

class Pattern:
    def __init__(self, stones, value):
        self.stones = stones  # List of tuples (x, y, player)
        self.value = value

    def matches(self, state, player,board_size):
        for x, y, pattern_player in self.stones:
            if not (0 <= x < board_size and 0 <= y < board_size):
                return False
            if state.board[0,x, y] != pattern_player:
                return False
        return True


class AdvancedGomokuAI:
    def __init__(self, board_size, win_size):
        self.board_size = board_size
        self.win_size = win_size
        self.known_patterns = []  # List to store known patterns

    def is_valid_pos(self, r, c):
        return 0 <= r < self.board_size and 0 <= c < self.board_size
    
    def learn_new_pattern(self, state, move):
        """
        Learns new patterns based on the game state and last move.
        """
        player = state.current_player()
        patterns_found = self.analyze_for_patterns(state, move, player)

        for pattern in patterns_found:
            if self.is_new_pattern(pattern):
                self.known_patterns.append(pattern)

    def analyze_for_patterns(self, state, move, player):
        new_patterns = []
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            pattern_stones = [(move[0], move[1], player)]
            for i in range(1, 5):
                r, c = move[0] + dr * i, move[1] + dc * i
                if not self.is_valid_pos(r, c):
                    break
                if state.board[0,r, c] == player:  
                    pattern_stones.append((r, c, player))
                else:
                    break

            for i in range(1, 5):
                r, c = move[0] - dr * i, move[1] - dc * i
                if not self.is_valid_pos(r, c):
                    break
                if state.board[0,r, c] == player:  
                    pattern_stones.append((r, c, player))
                else:
                    break

                if len(pattern_stones) >= 3:  
                    new_patterns.append(Pattern(pattern_stones, self.calculate_pattern_value(pattern_stones)))

            return new_patterns

    def is_new_pattern(self, pattern):
        """
        Checks if a pattern is new or already known.
        """
        for known_pattern in self.known_patterns:
            if known_pattern.stones == pattern.stones:
                return False
        return True

    def calculate_pattern_value(self, pattern_stones):
        """
        Assigns a value to a pattern based on its potential to lead to a win.
        """
        
        length = len(pattern_stones)
        return 1000 * length  #



    def evaluate_board(self, state, player):
        """
        Enhanced evaluation of board state, including pattern matching.
        """
        score = 0
        for r in range(self.board_size):
            for c in range(self.board_size):
                if state.board[player, r, c] == 1:
                    score += self.evaluate_position(state, player, r, c)

        # Pattern matching
        for pattern in self.known_patterns:
            if pattern.matches(state, player,self.board_size):
                score += pattern.value

        return score

    def evaluate_position(self, state, player, r, c):
        """
        Evaluate the position for a player in all directions.
        """
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        total_score = 0
        for dr, dc in directions:
            line_score, open_ends = self.evaluate_direction(state, player, r, c, dr, dc)
            total_score += self.calculate_potential(line_score, open_ends)
        return total_score

    def evaluate_direction(self, state, player, r, c, dr, dc):
        """
        Evaluate a direction from a position.
        """
        line_score = 0
        open_ends = 0

        # Forward direction
        for i in range(1, self.win_size):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < self.board_size and 0 <= nc < self.board_size):
                break
            if state.board[player, nr, nc] == 1:
                line_score += 1
            elif state.board[0, nr, nc] == 1:  # Check for empty space
                open_ends += 1
                break
            else:
                break

        # Backward direction
        for i in range(1, self.win_size):
            nr, nc = r - i * dr, c - i * dc
            if not (0 <= nr < self.board_size and 0 <= nc < self.board_size):
                break
            if state.board[player, nr, nc] == 1:
                line_score += 1
            elif state.board[0, nr, nc] == 1:  # Check for empty space
                open_ends += 1
                break
            else:
                break

        return line_score, open_ends

    def calculate_potential(self, line_score, open_ends):
        """
        Updated potential calculation with central focus.
        """
        # Winning move
        if line_score >= self.win_size - 1:
            return 200000

        # Imminent threat or opportunity
        if line_score == self.win_size - 2:
            if open_ends == 2:
                return 20000  # Double-open four
            if open_ends == 1:
                return 10000   # Single-open four

        # Central control enhancement
        central_bonus = 1
        if line_score >= 2:
            central_bonus = 2

        # Potential setup for future moves
        if line_score >= 2:
            score = 1000 * line_score * central_bonus
            if open_ends:
                score *= 2  # Open ends are more valuable
            return score
        return 10 * (open_ends + 1) * central_bonus  # Basic score for potential
    
    def immediate_threats(self, state):
        for player in [1, 2]:  
            for r in range(self.board_size):
                for c in range(self.board_size):
                    if state.board[0, r, c] == 1:  # Empty cell
                        state.board[player, r, c] = 1
                        if self.is_winning_move(state, player, r, c):
                            state.board[player, r, c] = 0
                            return (r, c)
                        state.board[player, r, c] = 0
        return None

    def is_winning_move(self, state, player, r, c):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # horizontal, vertical, diagonal, anti-diagonal
        for dr, dc in directions:
            count = 1  # Count the current stone
            # Check in one direction
            for i in range(1, self.win_size):
                nr, nc = r + dr * i, c + dc * i
                if 0 <= nr < self.board_size and 0 <= nc < self.board_size and state.board[player, nr, nc] == 1:
                    count += 1
                else:
                    break
            # Check in the opposite direction
            for i in range(1, self.win_size):
                nr, nc = r - dr * i, c - dc * i
                if 0 <= nr < self.board_size and 0 <= nc < self.board_size and state.board[player, nr, nc] == 1:
                    count += 1
                else:
                    break
            if count+1 >= self.win_size:  # Win condition met
                return True
        return False

    
class Submission:
    def __init__(self, board_size, win_size):
        self.board_size = board_size
        self.win_size = win_size
        self.ai = AdvancedGomokuAI(board_size, win_size)

    def __call__(self, state):
        player = state.current_player()
        opponent = 3 - player
        best_score = -np.inf
        best_move = None

        # Check for immediate win/loss moves
        immediate_move = self.ai.immediate_threats(state)
        if immediate_move is not None:
            return immediate_move

        move_candidates = self.get_prioritized_moves(state)

        # Evaluate each candidate move
        for r, c in move_candidates:
            if state.board[0, r, c] == 1:  # Check if the position is empty
                state.board[player, r, c] = 1
                score = self.ai.evaluate_board(state, player) - self.ai.evaluate_board(state, opponent)
                state.board[player, r, c] = 0  # Reset the board

                if score > best_score:
                    best_score = score
                    best_move = (r, c)

        # Learn new patterns if a move is made
        if best_move:
            self.ai.learn_new_pattern(state, best_move)

        return best_move


    def get_prioritized_moves(self, state, central_focus=False):
        """
        Generate move candidates with priority, focusing on central control.
        """
        center = self.board_size // 2
        center_range = self.board_size // 4  # Define a central area
        candidates = []
        for r in range(self.board_size):
            for c in range(self.board_size):
                if state.board[0, r, c] == 1:  # Empty cell
                    priority = 0
                    if central_focus and abs(r - center) <= center_range and abs(c - center) <= center_range:
                        priority += 10  # Higher priority for central positions

                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < self.board_size and 0 <= nc < self.board_size and state.board[0, nr, nc] != 1:
                                priority += 1
                    candidates.append(((r, c), priority))
        candidates.sort(key=lambda x: x[1], reverse=True)
        return [pos for pos, _ in candidates]