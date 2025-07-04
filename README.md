# Optimal Control Design for a Mass-Spring-Damper System using LQR

This project focuses on modeling, analyzing, and designing an optimal state-feedback controller for a **mass-spring-damper (MSD)** system using **Linear Quadratic Regulator (LQR)** methods. It includes system simulation, controllability analysis, gain synthesis using the Riccati equation, and performance comparison with the uncontrolled system.

## Project Goals

- Model a second-order mass-spring-damper system in state-space form
- Simulate its natural (uncontrolled) behavior
- Design a state-feedback controller using LQR
- Analyze system controllability
- Compare the controlled vs. uncontrolled response through visualization

## Files and Descriptions

### `Desain LQR.py`
Computes the optimal gain matrix `K` using the continuous-time algebraic Riccati equation (CARE) for a given state-space model. This script focuses on:
- Defining matrices `A`, `B`
- Choosing LQR weights `Q`, `R`
- Calculating the gain matrix `K`
- Computing the closed-loop system matrix `Acl = A - BK`

### `Simulasi non-linear MSD.py`
Simulates the response of the system without any control input (`u = 0`). It uses numerical integration to observe:
- Natural oscillations and damping
- Evolution of position and velocity over time
- Visual plots of both states

### `Sintesis Kontrol Optimal LQR MSD.py`
Performs a complete design and simulation of an LQR-controlled MSD system. Key steps:
- State-space system creation
- Controllability check
- Optimal gain synthesis using `ctrl.lqr()`
- Closed-loop simulation using `forced_response()`
- Comparison of state behavior (position and velocity) over time

## System Model

The standard form of the mass-spring-damper system is given by:
```
m * x'' + b * x' + k * x = u
```

Converted into state-space form with:

- State vector: `x = [position, velocity]`
- Input: `u` (force)
- Output: `y = position`

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib
- Python Control Systems Library (`control`)

Install dependencies:
```bash
pip install numpy scipy matplotlib control
