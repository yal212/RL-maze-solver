from array import array
from random import random, randint

import numpy as np
from convert import find_reachable_neighbors
from practice.task.convert import Feasibility


def get_possible_next_states(state: int, f_matrix: np.array, n_states: int) -> list[int]:
    # given a state s and a feasibility matrix F
    # get list of possible next states
    poss_next_states = []
    for j in range(n_states):
        if f_matrix[state, j] == 1:
            poss_next_states.append(j)
    return poss_next_states


def get_random_next_state(state, f_matrix, n_states) -> int:
    possible_states = get_possible_next_states(state, f_matrix, n_states)
    return possible_states[np.random.randint(0, len(possible_states))]


class Agent:
    def __init__(self, feasibility: Feasibility, gamma: float, lrn_rate: float, maze, start_x: int, start_y: int):
        self.gamma: float = gamma
        self.lrn_rate: float = lrn_rate
        self.path: list = []
        self.Q: np.ndarray = np.zeros(
            shape=[feasibility.cells, feasibility.cells], dtype=int)
        self.R: np.ndarray = np.copy(feasibility.F_matrix)
        self.start: int = feasibility.numbered_grid[start_x, start_y]
        self.goal: int = feasibility.numbered_grid[maze.end[0], maze.end[1]]
        self.n_states: int = feasibility.cells
        self.set_rewards()

    def set_rewards(self):
        previous = get_possible_next_states(
            self.goal, self.R, self.n_states)[0]
        self.R = np.where(self.R == 1, -0.1, self.R)
        self.R[previous, self.goal] = 1000.0

    def train(self, f_matrix: np.array, epochs: int):
        for _ in range(epochs):
            # Select random initial state
            current_state = np.random.randint(0, self.n_states)

            while True:
                next_state: int = get_random_next_state(
                    current_state, f_matrix, self.n_states)
                # Find the best next-next state
                max_q: float = -99999.9
                for next_next_state in get_possible_next_states(next_state, f_matrix, self.n_states):
                    max_q = max(max_q, float(
                        self.Q[next_state][next_next_state]))

                # Bellman's equation: Q = [(1 - alpha) * Q]  +  [alpha * (reward + (gamma * maxQ))]
                # Update the Q matrix
                self.Q[current_state][next_state] = (1 - self.lrn_rate) * self.Q[current_state][next_state] + (
                    self.lrn_rate * (self.R[current_state][next_state] + self.gamma * max_q))
                current_state = next_state
                if current_state == self.goal:
                    break

    def walk(self, maze, feasibility: Feasibility):
        current_state = self.start
        self.path.append(current_state)
        while current_state != self.goal:
            print(str(current_state) + "->", end="")
            next_state = np.argmax(self.Q[current_state])
            if next_state == current_state:
                self.path.append("break")
                print("Path not found")
                break
            self.path.append(next_state)
            current_state = next_state
        print("Done")
