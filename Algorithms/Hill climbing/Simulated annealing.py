import numpy as np
import math
import random


class Queen:
    def __init__(self, N):
        self.N = N
        self.queen_loc = dict()
        self.chess_board = [[0] * self.N for _ in range(self.N)]

    def add_queen(self):
        number_Q = 0
        while True:
            flag = 0
            r = np.random.randint(self.N)
            c = np.random.randint(self.N)
            # print(f'r:{r} c:{c}')
            for q in self.queen_loc:
                row, col = self.queen_loc[q]
                if (r == row and c == col) or (c == col):
                    flag = 1
            if flag == 0:
                Q = f"Q{number_Q}"
                if Q not in self.queen_loc:
                    self.queen_loc[Q] = []
                self.queen_loc[Q].append(r)
                self.queen_loc[Q].append(c)
                self.chess_board[r][c] = Q
                number_Q += 1
            if number_Q == self.N:
                break

        # self.queen_loc["Q1"] = []
        # self.queen_loc["Q1"].append(2)
        # self.queen_loc["Q1"].append(0)
        # self.chess_board[2][0] = "Q1"

        # self.queen_loc["Q2"] = []
        # self.queen_loc["Q2"].append(1)
        # self.queen_loc["Q2"].append(1)
        # self.chess_board[1][1] = "Q2"

        # self.queen_loc["Q3"] = []
        # self.queen_loc["Q3"].append(2)
        # self.queen_loc["Q3"].append(2)
        # self.chess_board[2][2] = "Q3"

        # self.queen_loc["Q4"] = []
        # self.queen_loc["Q4"].append(1)
        # self.queen_loc["Q4"].append(3)
        # self.chess_board[1][3] = "Q4"

    def print_board(self):
        board = [["."] * self.N for _ in range(self.N)]
        for queen, (row, col) in self.queen_loc.items():
            board[row][col] = queen
        for row in board:
            print(" ".join(row))


def conflict(r1, c1, r2, c2):
    return r1 == r2 or c1 == c2 or r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2


def get_conflict(state, queen_id):
    count = 0
    r1, c1 = state[queen_id]
    for q, (r2, c2) in state.items():
        if q != queen_id and conflict(r1, c1, r2, c2):
            count += 1
    return count


def calc_cost(state):
    total_cost = 0
    for q in state:
        total_cost += get_conflict(state, q)
    return total_cost // 2  # Each conflict counted twice


def goal_test(state):
    return calc_cost(state) == 0


# Simulated Annealing Helpers
def moveOrNot(delE):
    if delE >= 0:
        return True  # Always accept improvements
    e = math.exp(delE)
    p = random.random()
    return p <= e


def state_gen(state, cost):
    state_list = [state[f"Q{i}"][0] for i in range(len(state))]
    node = state_list.copy()

    found_better = False
    for i in range(len(node)):
        for j in range(len(node)):
            if i != j:  # Only swap different indices
                node[i], node[j] = node[j], node[i]

                # Update state dictionary based on node
                new_state = state.copy()
                for idx, row in enumerate(node):
                    new_state[f"Q{idx}"] = [row, idx]

                cur_cost = calc_cost(new_state)
                deltaE = cost - cur_cost

                if cur_cost < cost or moveOrNot(deltaE):
                    cost = cur_cost
                    state = new_state
                    found_better = True
                else:
                    node[i], node[j] = node[j], node[i]  # Revert the change

    # Introduce random perturbation if no better state is found
    if not found_better:
        random_idx = random.randint(0, len(node) - 1)
        node[random_idx] = random.randint(0, len(node) - 1)

        # Update state with random perturbation
        for idx, row in enumerate(node):
            state[f"Q{idx}"] = [row, idx]

    return state, cost


def HCSA(state):
    cur_cost = calc_cost(state)
    iteration = 0
    while not goal_test(state):
        state, cur_cost = state_gen(state, cur_cost)
        iteration += 1
        if iteration > 1000:  # Safeguard to prevent infinite loops
            print("Stuck in loop, restarting...")
            break
    return state


queen = Queen(4)
queen.add_queen()

print("Initial Board:")
queen.print_board()

print("\nRunning Simulated Annealing with HCSA...")
final_state = HCSA(queen.queen_loc)

if final_state:
    print("\nSolution found:")
    queen.queen_loc = final_state
    queen.print_board()
else:
    print("No solution found within the iteration limit.")
