"""
Q-learning reinforcement learning agent for maze solving.

This module implements a Q-learning agent that learns to navigate mazes by
exploring the environment and updating Q-values based on rewards and future
state values using the Bellman equation.
"""

from array import array
from random import random, randint

import numpy as np
from convert import find_reachable_neighbors
from convert import Feasibility


def get_possible_next_states(state: int, f_matrix: np.array, n_states: int) -> list[int]:
    """
    Get all possible next states from the current state.

    Args:
        state (int): Current state number.
        f_matrix (np.array): Feasibility matrix indicating valid transitions.
        n_states (int): Total number of states in the environment.

    Returns:
        list[int]: List of state numbers that can be reached from the current state.
    """
    poss_next_states = []
    for j in range(n_states):
        if f_matrix[state, j] == 1:
            poss_next_states.append(j)
    return poss_next_states


def get_random_next_state(state, f_matrix, n_states) -> int:
    """
    Randomly select a valid next state from the current state.

    Args:
        state (int): Current state number.
        f_matrix (np.array): Feasibility matrix indicating valid transitions.
        n_states (int): Total number of states in the environment.

    Returns:
        int: Randomly selected valid next state.
    """
    possible_states = get_possible_next_states(state, f_matrix, n_states)
    return possible_states[np.random.randint(0, len(possible_states))]


class Agent:
    """
    Q-learning reinforcement learning agent for maze navigation.

    This agent uses Q-learning to learn optimal policies for navigating mazes.
    It maintains Q-values for state-action pairs and updates them using the
    Bellman equation during training.

    Attributes:
        gamma (float): Discount factor for future rewards (0 < gamma <= 1).
        lrn_rate (float): Learning rate for Q-value updates (0 < lrn_rate <= 1).
        path (list): Sequence of states representing the agent's path.
        Q (np.ndarray): Q-value matrix for state-action pairs.
        R (np.ndarray): Reward matrix for state transitions.
        start (int): Starting state number.
        goal (int): Goal state number.
        n_states (int): Total number of states in the environment.
    """

    def __init__(self, feasibility: Feasibility, gamma: float, lrn_rate: float, maze, start_x: int, start_y: int):
        """
        Initialize the Q-learning agent.

        Args:
            feasibility (Feasibility): Feasibility matrix object containing maze structure.
            gamma (float): Discount factor for future rewards.
            lrn_rate (float): Learning rate for Q-value updates.
            maze (Maze): Maze object containing start and end positions.
            start_x (int): X-coordinate of the starting position.
            start_y (int): Y-coordinate of the starting position.
        """
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
        """
        Set up the reward matrix for the learning environment.

        This method configures rewards to encourage the agent to reach the goal:
        - Small negative reward (-0.1) for regular moves to encourage efficiency
        - Large positive reward (1000.0) for reaching the goal state
        """
        previous = get_possible_next_states(
            self.goal, self.R, self.n_states)[0]
        self.R = np.where(self.R == 1, -0.1, self.R)
        self.R[previous, self.goal] = 1000.0

    def train(self, f_matrix: np.array, epochs: int):
        """
        Train the agent using Q-learning algorithm.

        The agent learns by repeatedly exploring the environment and updating
        Q-values using the Bellman equation. Each training episode starts from
        a random state and continues until the goal is reached.

        Args:
            f_matrix (np.array): Feasibility matrix indicating valid state transitions.
            epochs (int): Number of training episodes to run.
        """
        for _ in range(epochs):
            # Select random initial state for exploration
            current_state = np.random.randint(0, self.n_states)

            while True:
                # Choose next state randomly from valid options
                next_state: int = get_random_next_state(
                    current_state, f_matrix, self.n_states)

                # Find the maximum Q-value for the next state (for Bellman equation)
                max_q: float = -99999.9
                for next_next_state in get_possible_next_states(next_state, f_matrix, self.n_states):
                    max_q = max(max_q, float(
                        self.Q[next_state][next_next_state]))

                # Update Q-value using Bellman equation:
                # Q(s,a) = (1-α)Q(s,a) + α[R(s,a) + γ·max(Q(s',a'))]
                self.Q[current_state][next_state] = (1 - self.lrn_rate) * self.Q[current_state][next_state] + (
                    self.lrn_rate * (self.R[current_state][next_state] + self.gamma * max_q))

                current_state = next_state
                if current_state == self.goal:
                    break

    def walk(self, maze, feasibility: Feasibility):
        """
        Execute the learned policy to find a path from start to goal.

        Uses the trained Q-values to greedily select the best action at each
        state, generating a path from the start to the goal position.

        Args:
            maze (Maze): The maze object (used for compatibility).
            feasibility (Feasibility): Feasibility matrix object (used for compatibility).
        """
        current_state = self.start
        self.path.append(current_state)

        while current_state != self.goal:
            print(str(current_state) + "->", end="")
            # Select action with highest Q-value (greedy policy)
            next_state = np.argmax(self.Q[current_state])

            # Check if agent is stuck (no progress possible)
            if next_state == current_state:
                self.path.append("break")
                print("Path not found")
                break

            self.path.append(next_state)
            current_state = next_state

        print("Done")
