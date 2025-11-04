# RL Maze Solver 🤖🧩

An intelligent maze solver built using **Reinforcement Learning** techniques. This project demonstrates the power of Q-learning algorithms to navigate complex mazes and find optimal paths from start to finish.

*Built as part of the **JetBrains Academy** course: "Reinforcement Learning: Building an AI Maze Solver"*

## 🎯 Features

- **Dynamic Maze Generation**: Creates random mazes using recursive backtracking algorithm
- **Q-Learning Agent**: Implements reinforcement learning to find optimal paths
- **Interactive Interface**: User-friendly command-line interface for maze configuration
- **Visual Output**: Generates both static maze images and animated solution paths
- **Feasibility Matrix**: Converts maze structure into mathematical representation for RL processing
- **Customizable Parameters**: Adjustable maze dimensions, learning rate, and discount factor

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd RL-maze-solver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Basic Maze Generation
```bash
python3 main.py
```
Follow the prompts to:
- Enter maze dimensions (e.g., `5 5`)
- Specify start coordinates (e.g., `0 0`)

#### Full RL Training and Pathfinding
```python
from maze import Maze
from convert import Feasibility
from learn import Agent
from draw import make_movie

# Create maze
maze = Maze(10, 10, [0, 0])

# Generate feasibility matrix
feasibility = Feasibility(maze)

# Train RL agent
agent = Agent(feasibility, gamma=0.8, lrn_rate=0.9, maze=maze, start_x=0, start_y=0)
agent.train(feasibility.F_matrix, epochs=1000)

# Find and visualize path
agent.walk(maze, feasibility)
make_movie(maze, feasibility, agent.path, "solution.gif")
```

## 📁 Project Structure

```
RL-maze-solver/
├── main.py              # Main application entry point
├── maze.py              # Maze generation using recursive backtracking
├── cell.py              # Cell class for maze structure
├── convert.py           # Maze to feasibility matrix conversion
├── learn.py             # Q-learning agent implementation
├── draw.py              # Visualization and rendering utilities
├── requirements.txt     # Python dependencies
├── test_full_functionality.py  # Comprehensive test suite
└── README.md           # Project documentation
```

## 🧠 How It Works

### 1. Maze Generation
- Uses **recursive backtracking** algorithm to create perfect mazes
- Ensures single path between any two points
- Randomly selects start and end positions

### 2. Reinforcement Learning
- Implements **Q-learning** algorithm
- Converts maze into state-action space
- Uses Bellman equation for value updates:
  ```
  Q(s,a) = (1-α)Q(s,a) + α[R(s,a) + γ·max(Q(s',a'))]
  ```

### 3. Pathfinding
- Agent explores maze using learned Q-values
- Selects actions with highest expected rewards
- Generates optimal path from start to goal

### 4. Visualization
- Static maze images with start/end markers
- Animated GIFs showing agent movement
- Grid numbering for debugging and analysis

## 🔧 Configuration

### Agent Parameters
- **Learning Rate (α)**: Controls how quickly the agent learns (default: 0.9)
- **Discount Factor (γ)**: Balances immediate vs future rewards (default: 0.8)
- **Training Epochs**: Number of learning iterations (recommended: 1000+)

### Maze Parameters
- **Dimensions**: Width and height of the maze grid
- **Start Position**: Initial agent coordinates (0-indexed)
- **End Position**: Automatically determined during generation

## 📊 Output Files

- `maze.png`: Static visualization of the generated maze
- `maze_path.gif`: Animated solution showing agent movement
- Console output: Step-by-step path coordinates

## 🧪 Testing

Run the comprehensive test suite:
```bash
python3 test_full_functionality.py
```

This validates:
- ✅ Maze generation
- ✅ Feasibility matrix creation
- ✅ Agent training
- ✅ Pathfinding accuracy
- ✅ Visualization rendering

## 📚 Dependencies

- **NumPy**: Numerical computations and matrix operations
- **Pandas**: Data manipulation and analysis
- **Pillow (PIL)**: Image processing and generation

## 🎓 Educational Context

This project was developed as part of the **JetBrains Academy** course "Reinforcement Learning: Building an AI Maze Solver". It demonstrates practical applications of:

- Markov Decision Processes (MDPs)
- Q-learning algorithms
- State-space representation
- Reward function design
- Exploration vs exploitation strategies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Algorithm improvements
- Additional visualization features
- Performance optimizations
- Documentation enhancements

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Happy maze solving! 🎉*
