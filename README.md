# Learning Data Structures and Algorithms: Barnes-Hut Optimization for Physics Engine

Hello! This repository is my personal journey in understanding data structures and algorithms. My main focus is on implementing and understanding the Barnes-Hut algorithm to optimize the physics engine I'm building. This physics engine's core functionality is simulating particles that attract each other.

## Table of Contents

- [Background](#background)
- [Project Overview](#project-overview)
- [Barnes-Hut Algorithm](#barnes-hut-algorithm)
- [Installation and Usage](#installation-and-usage)
- [Contributions and Feedback](#contributions-and-feedback)
- [References and Resources](#references-and-resources)

## Background

The simulation of particles attracting each other is a classic problem in computational physics and has a wide range of applications. Efficiently simulating this without optimizations can be computationally expensive, especially when dealing with a large number of particles. 

## Project Overview

In this project, I am building a physics engine from scratch with the main aim of simulating particles' mutual attractions. As the number of particles increases, the computational complexity grows, which can lead to inefficient simulations. To tackle this challenge, I am exploring the Barnes-Hut algorithm, which offers a potential optimization to this problem.

## Barnes-Hut Algorithm

The Barnes-Hut algorithm is a near-linear complexity method to calculate the gravitational forces in a system of bodies. Instead of computing the force between each pair of particles, which has a complexity of O(n^2), the Barnes-Hut algorithm groups nearby particles and approximates them as a single point mass, reducing the complexity to O(n log n).

### Key Concepts:

- **Quadtree (or Octree in 3D):** The space is recursively divided into quadrants (or octants in 3D). Each quadrant can contain a single body or can be further subdivided.
  
- **Center of Mass:** Used to represent a group of bodies as a single body.
  
- **Theta Criterion:** Determines whether to use the center of mass to approximate the gravitational force or to further subdivide the quadrant.

I will be implementing and experimenting with this algorithm to observe its efficiency and accuracy in simulating particle attractions.

## Installation and Usage

```bash
# Clone this repository
git clone https://github.com/dIB59/physics-engine.git

# Navigate to the directory
cd physics-engine

# To run the simulation
python main.py
```

## Contributions and Feedback

Feel free to fork this repository and submit pull requests. Any contributions, feedback, or suggestions are more than welcome. Let's learn together!

## References and Resources

- Barnes, J., & Hut, P. (1986). A hierarchical O(N log N) force-calculation algorithm. Nature, 324(6096), 446-449.
- [Read this rather than the paper](https://anaroxanapop.github.io/behalf/#Nbody)
- [A good tutorial to get started on QuadTrees](https://katherinepully.com/quadtree-python/)

