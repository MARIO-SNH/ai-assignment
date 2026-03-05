AI Assignment – Simple Reflex Agent and Uninformed Search

This repository contains the implementation of the Artificial Intelligence assignment.

The assignment consists of three parts:

1. Designing the architecture for Turing Test and CAPTCHA
2. Developing a simple reflex agent that reads environmental parameters and determines AQI
3. Implementing uninformed search algorithms such as BFS and DFS and applying them to a problem

Part 1 – Architecture Design

The design architecture for both the Turing Test and CAPTCHA systems is explained in the documentation file inside the docs folder. The document describes the components involved and the general working process of each system.

Part 2 – AQI Simple Reflex Agent

A simple reflex agent was developed in Python. The agent reads environmental data such as PM2.5 and PM10 values from a CSV file and calculates the Air Quality Index (AQI) based on predefined ranges.

Files related to the AQI agent are located in the aqi_agent folder.

aqi_agent.py – Program that reads the sensor data and calculates AQI  
sample_sensor_data.csv – Sample input file containing environmental data

To run the AQI agent:

python aqi_agent/aqi_agent.py --file aqi_agent/sample_sensor_data.csv


Part 3 – Uninformed Search Algorithms

Breadth First Search (BFS) and Depth First Search (DFS) algorithms were implemented and applied to the Eight Queens problem.

Eight Queens Problem

The objective of the Eight Queens problem is to place eight queens on a chessboard such that no two queens attack each other. This means that no two queens can share the same row, column, or diagonal.

The search algorithm explores possible placements of queens and checks whether the configuration is valid.

Files related to the search implementation are located in the following folders:

search/ – contains the BFS and DFS implementations  
problems/ – contains the Eight Queens problem definition

To run the program:

python search/run_compare.py

The program prints information such as:

nodes expanded  
maximum frontier size  
time taken  
solution depth  

These values are used to compare the performance of the search algorithms.

Programming Language

The programs in this repository were implemented using Python 3. No external libraries were required.

Repository Structure

ai-assignment  
README.md  
requirements.txt  
docs  
aqi_agent  
search  
problems

This assignment demonstrates basic AI concepts including reflex agents and uninformed search techniques.