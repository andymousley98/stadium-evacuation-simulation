# Stadium Evacuation Simulation

## Project Overview
A Python-based mathematical modelling project exploring how exit capacity and variability in evacuation conditions affect the time required to evacuate a stadium.

The project was developed in four stages, progressing from basic mathematical calculations to randomised simulations and results analysis.

## Objectives
- Calculate evacuation times based on population and exit capacity.
- Simulate the evacuation process over discrete time steps.
- Introduce randomness to represent variation in evacuation conditions.
- Analyse simulation results to identify typical outcomes and variation.

## Methodology

**Stage 1 – Basic Evacuation Calculation**

Developed a mathematical model to estimate evacuation time using stadium population, number of available exits and exit processing capacity.

**Stage 2 – Time-Based Simulation**

Expanded the model to simulate the evacuation process minute by minute, tracking the number of people remaining.

**Stage 3 – Randomised Simulation**

Introduced variability in evacuation capacity to explore how different conditions could affect total evacuation time.

**Stage 4 – Results Analysis**

Analysed outcomes across repeated simulations to understand the distribution and frequency of evacuation times.

## Example Results

In an illustrative scenario with 1,000 people and two exits capable of processing 60 people per minute each, the basic model estimated an evacuation time of approximately 8.33 minutes.

In a separate randomised simulation exercise, recorded results included:

| Metric | Result |
|---|---|
| Average evacuation time | 8.87 minutes |
| Fastest evacuation | 8 minutes |
| Slowest evacuation | 10 minutes |

Results depend on the assumptions and simulation parameters used.

## Skills Demonstrated
- Python programming
- Mathematical modelling
- Discrete-time simulation
- Randomised simulation
- Scenario analysis
- Quantitative results interpretation

## Limitations
This is an illustrative capacity-based simulation rather than a validated pedestrian movement model. It does not explicitly simulate individual walking routes, crowd density, physical geometry or complex human behaviour.

## Running the Project
The Python files are organised by development stage. Open and run each script in a Python environment such as Spyder.

Each stage illustrates an extension of the modelling approach.
