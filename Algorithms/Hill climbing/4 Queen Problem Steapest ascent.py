import numpy as np


class Queen:
    def __init__(self, N):
        self.N = N
        self.queen_loc = dict()
        self.initialize = False
        self.chess_board = [[0] * self.N for _ in range(self.N)]

    def add_queen(self):
        if self.initialize == False:
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
            self.initialize = True

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

    def move_queen(self, queen_id, new_row):
        col = self.queen_loc[queen_id][1]
        # Remove the queen from the current position
        current_row = self.queen_loc[queen_id][0]
        self.chess_board[current_row][col] = 0
        # Update the queen's position
        self.queen_loc[queen_id] = [new_row, col]
        # Place the queen in the new position
        self.chess_board[new_row][col] = f"{queen_id}"

    def get_neighbor(self, queen_id):
        row, col = self.queen_loc[queen_id]
        neighbors = []
        for new_row in range(self.N):
            if new_row != row:
                neighbors.append((queen_id, new_row))
        return neighbors
        
    def print_Queen(self):
        print(self.chess_board)
        for Q in self.queen_loc:
            print(f'{Q}->{self.queen_loc[Q]}')


def conflict(r1, c1, r2, c2):
    if r1 == r2:
        return True
    if c1 == c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    return False


def get_conflict(Q, dict):
    count = 0
    for q in dict:
        if q is not Q:
            r1, c1 = dict[Q]
            r2, c2 = dict[q]
            if conflict(r1, c1, r2, c2):
                count += 1
    return count


def calc_cost(dict):
    cost = 0
    max = -999
    maxQ = None
    # print(state)
    for Q in dict:
        q_cost = get_conflict(Q, dict)
        cost += q_cost
        if q_cost > max:
            max = q_cost
            maxQ = Q
    return cost // 2, max, maxQ


def goal_test(dict):
    if calc_cost(dict)[0] == 0:
        return True
    else:
        return False


def hill_climbing(queen):
    while not goal_test(queen.queen_loc):
        _, max_cost, max_queen = calc_cost(queen.queen_loc)
        neighbors = queen.get_neighbor(max_queen)
        best_move = None
        lowest_cost = float("inf")

        for queen_id, new_row in neighbors:
            original_row = queen.queen_loc[queen_id][0]
            queen.move_queen(queen_id, new_row)
            cost = calc_cost(queen.queen_loc)[0]

            if cost < lowest_cost:
                best_move = (queen_id, new_row)
                lowest_cost = cost

            queen.move_queen(queen_id, original_row)

        if best_move is None or lowest_cost >= calc_cost(queen.queen_loc)[0]:
            print("Local maximum reached")
            break
        else:
            queen.move_queen(*best_move)

    print("Solution found with Hill Climbing:")
    queen.print_Queen()


queen = Queen(4)
queen.add_queen()
print("Initial Board:")
queen.print_Queen()

print("\nRunning Hill Climbing...")
hill_climbing(queen)
