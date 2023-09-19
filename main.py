import render.PygameRender
from util.QTree import QTree

if __name__ == '__main__':
    # Create a QuadTree with a threshold of 4 and 50 initial points.
    qt = QTree(4, 25, 800, 800)
    # Optionally, add more points.
    qt.add_point(5, 5)
    # Subdivide the QuadTree based on the threshold.
    qt.subdivide()
    # Visualize the QuadTree.
    qt.graph()
    render.PygameRender.render(qt)
    qt.graph()


