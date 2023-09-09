from particle.QTree import QTree

if __name__ == '__main__':
    # Create a QuadTree with a threshold of 4 and 50 initial points.
    qt = QTree(4, 100)

    # Optionally, add more points.
    qt.add_point(5, 5)

    # Subdivide the QuadTree based on the threshold.
    qt.subdivide()

    # Visualize the QuadTree.
    qt.graph()
