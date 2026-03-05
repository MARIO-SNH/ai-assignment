# AI Assignment – Simple Reflex Agent and Uninformed Search

This repository contains the implementation for the Artificial Intelligence assignment.

Architecture Design

The architecture design for the Turing Test and CAPTCHA systems is explained in the file:
docs/architecture.md


Simple Reflex Agent (AQI Agent)

A simple reflex agent is implemented that reads environmental sensor data from a file and determines the Air Quality Index (AQI) of the region.

Files used:
aqi_agent/aqi_agent.py
aqi_agent/sample_sensor_data.csv

To run the program:
python aqi_agent/aqi_agent.py --file aqi_agent/sample_sensor_data.csv


Uninformed Search Algorithms

The following search algorithms are implemented:
Breadth First Search (BFS)
Depth First Search (DFS)
Depth Limited Search
Iterative Deepening DFS

The implementation is in:
search/core.py


Example Problem

The search problem implemented is the Eight Queens problem.

File:
eight_queens/eight_queens.py

To run the comparison:
python search/run_compare.py


This repository includes the architecture design, reflex agent implementation, search algorithms, and the example problem required for the assignment.
