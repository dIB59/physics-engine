from custompygameclasses.PygameRender import render
from util.QTree import QTree

if __name__ == '__main__':
    # Create a QuadTree with a threshold of 4 and 50 initial points.
    qt = QTree(4, 25, 800, 800)
    # Subdivide the QuadTree based on the threshold.
    qt.subdivide()
    # Visualize the QuadTree.
    qt.create_graph()
    render(qt)
    qt.create_graph()


