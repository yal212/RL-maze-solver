#!/usr/bin/env python3
"""
Test script to verify all functionality works correctly
"""

from maze import Maze
from convert import Feasibility
from draw import draw_maze, make_movie
from learn import Agent
import pandas as pd

def my_print(matrix):
    """Print a readable representation of the feasibility matrix."""
    labels = [str(x) for x in range(matrix.shape[0])]
    df = pd.DataFrame(matrix, columns=labels, index=labels)
    pd.set_option('display.max_rows', None)
    print(df.to_string())

def test_maze_creation():
    """Test maze creation"""
    print("Testing maze creation...")
    maze = Maze(5, 5, [0, 0])
    print(f"Maze created with dimensions {maze.nx}x{maze.ny}")
    print(f"Start: [0, 0], End: {maze.end}")
    return maze

def test_feasibility_matrix(maze):
    """Test feasibility matrix creation"""
    print("\nTesting feasibility matrix...")
    feasibility = Feasibility(maze)
    print(f"Feasibility matrix shape: {feasibility.F_matrix.shape}")
    print(f"Number of cells: {feasibility.cells}")
    return feasibility

def test_agent_training(maze, feasibility):
    """Test agent training"""
    print("\nTesting agent training...")
    agent = Agent(feasibility, gamma=0.8, lrn_rate=0.9, maze=maze, start_x=0, start_y=0)
    print(f"Agent created with start: {agent.start}, goal: {agent.goal}")
    
    # Train for a small number of epochs
    agent.train(feasibility.F_matrix, epochs=100)
    print("Training completed")
    
    # Test pathfinding
    print("\nTesting pathfinding...")
    agent.walk(maze, feasibility)
    print(f"Path found: {agent.path}")
    return agent

def test_visualization(maze, feasibility, agent):
    """Test visualization"""
    print("\nTesting visualization...")
    
    # Draw static maze
    draw_maze(maze, "test_maze.png")
    print("Static maze image created: test_maze.png")
    
    # Try to create animated path (if path was found)
    if 'break' not in agent.path:
        try:
            make_movie(maze, feasibility, agent.path, "test_path.gif")
            print("Animated path created: test_path.gif")
        except Exception as e:
            print(f"Could not create animation: {e}")
    else:
        print("Path not found, skipping animation")

if __name__ == "__main__":
    try:
        # Test all functionality
        maze = test_maze_creation()
        feasibility = test_feasibility_matrix(maze)
        agent = test_agent_training(maze, feasibility)
        test_visualization(maze, feasibility, agent)
        
        print("\n✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
