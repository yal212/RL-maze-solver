# Contributing to RL Maze Solver

Thank you for your interest in contributing to the RL Maze Solver project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. **Check existing issues** first to avoid duplicates
2. **Create a detailed issue** with:
   - Clear description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment details (Python version, OS, etc.)
   - Screenshots or code snippets if relevant

### Submitting Changes

1. **Fork the repository** and create a new branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

## 🛠️ Development Setup

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/RL-maze-solver.git
cd RL-maze-solver

# Install dependencies
pip install -r requirements.txt

# Run tests to verify setup
python3 test_full_functionality.py
```

## 📝 Coding Standards

### Python Style

- Follow **PEP 8** style guidelines
- Use **meaningful variable and function names**
- Add **docstrings** for all classes and functions (Google/NumPy style)
- Keep functions focused and reasonably sized
- Use type hints where appropriate

### Documentation

- Update docstrings when modifying functions
- Add comments for complex algorithms or logic
- Update README.md if adding new features
- Include examples for new functionality

### Testing

- Test your changes with different maze sizes
- Verify both maze generation and RL training work correctly
- Check that visualizations render properly
- Run the full test suite: `python3 test_full_functionality.py`

## 🎯 Areas for Contribution

### Algorithm Improvements

- **Enhanced Q-learning**: Implement Double Q-learning, Dueling DQN, or other variants
- **Alternative RL algorithms**: Add SARSA, Actor-Critic, or Policy Gradient methods
- **Exploration strategies**: Implement ε-greedy, UCB, or other exploration techniques
- **Performance optimization**: Improve training speed or convergence

### Maze Generation

- **Alternative algorithms**: Implement Kruskal's, Prim's, or other maze generation methods
- **Maze types**: Add support for braided mazes, weighted graphs, or 3D mazes
- **Obstacles**: Add support for dynamic obstacles or multiple goal states

### Visualization

- **Interactive visualization**: Add real-time training visualization
- **Better graphics**: Improve maze rendering with textures or 3D effects
- **Analysis tools**: Add Q-value heatmaps, training progress plots
- **Web interface**: Create a web-based interface for the maze solver

### Code Quality

- **Error handling**: Improve robustness and error messages
- **Performance profiling**: Add benchmarking and optimization
- **Code organization**: Refactor for better modularity
- **Configuration**: Add config files for hyperparameters

## 🧪 Testing Guidelines

### Manual Testing

1. **Basic functionality**: Generate mazes of various sizes (3x3 to 15x15)
2. **Edge cases**: Test with minimum size (2x2) and unusual dimensions
3. **Training**: Verify agent learns and finds paths consistently
4. **Visualization**: Check that images and GIFs generate correctly

### Automated Testing

- Add unit tests for new functions
- Ensure existing tests pass
- Test with different Python versions if possible

## 📋 Pull Request Checklist

Before submitting your PR, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] All functions have appropriate docstrings
- [ ] Changes are tested and working
- [ ] Documentation is updated if needed
- [ ] Commit messages are clear and descriptive
- [ ] No unnecessary files are included (check .gitignore)

## 🎓 Educational Context

This project was created as part of the **JetBrains Academy** course "Reinforcement Learning: Building an AI Maze Solver". When contributing, please keep in mind:

- **Educational value**: Changes should help others learn RL concepts
- **Code clarity**: Prioritize readability and understanding over optimization
- **Documentation**: Explain the "why" behind algorithmic choices
- **Examples**: Provide clear examples of new features

## 📞 Getting Help

- **Issues**: Use GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Code review**: Maintainers will provide feedback on pull requests

## 🏆 Recognition

Contributors will be acknowledged in the project documentation. Significant contributions may be highlighted in the README.

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for helping make RL Maze Solver better! 🎉
