# AI Lab Tasks

A collection of small Python programs for exploring core Artificial Intelligence ideas and algorithms. Each script is a self-contained lab example that uses a small graph, rule set, game tree, or sample dataset.

## Programs

| File | Topic | What it demonstrates |
| --- | --- | --- |
| **StateSpace2.py** | State-space representation | Displays states and their successor states. |
| **Best_First_Search.py** | Greedy best-first search | Uses a heuristic to choose which graph node to explore next. |
| **A-Star_Search.py** | A* search | Combines path cost and a heuristic to find a path through a weighted graph. |
| **PEAS_Agent.py** | Intelligent agents and PEAS | Shows performance measure, environment, actuators, and sensors in a simple rule-based demo. |
| **Forward_Chaining.py** | Rule-based reasoning | Derives new facts from known facts and rules until no more can be inferred. |
| **Hill_Climbing-Algorithm.py** | Local search | Repeatedly moves to a better neighboring value in a sample objective function. |
| **Minimax_Algorithm.py** | Game-tree search | Applies minimax to choose moves in a fixed-depth, two-player game tree. |
| **Decision_Tree_Algorithm.py** | Supervised learning | Trains a decision-tree classifier on a small sample dataset. |
| **K-Nearest_Neighbor.py** | Supervised learning | Classifies a sample point using its nearest neighbors. |
| **K-Means_Clustering.py** | Unsupervised learning | Groups sample points into clusters and prints their labels and centroids. |

## Requirements

- Python 3
- scikit-learn for the decision tree, K-nearest neighbors, and K-means examples

Install the additional dependency with:

    python -m pip install scikit-learn

The search, reasoning, hill-climbing, and minimax programs use Python's standard library.

## Running a program

Run commands from the repository directory. For example:

    python StateSpace2.py
    python A-Star_Search.py
    python Decision_Tree_Algorithm.py

Replace the filename with any program from the table above. Most scripts print a result immediately; PEAS_Agent.py asks for sample symptom inputs.

## Notes

These are educational demonstrations with compact, hard-coded examples rather than general-purpose packages. The medical diagnosis agent is a simplified rule-based exercise and is not intended for clinical use.
