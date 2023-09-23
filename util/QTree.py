import random

from util.Node import Node
from particle.ParticleBuilder import ParticleBuilder
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class QTree:
    def __init__(self, k, n, width: int, height: int):
        self.threshold = k
        self.points = [ParticleBuilder(random.uniform(0, 800), random.uniform(0, 800)).build() for x in range(n)]
        self.root = Node(0, 0, width, height, self.points)

    def get_width(self):
        return self.root.width

    def get_height(self):
        return self.root.height

    def insert_point(self, x, y):
        self.points.append(ParticleBuilder(x, y))

    def get_points(self):
        return self.points

    def subdivide(self):
        _recursive_subdivide(self.root, self.threshold)

    def graph(self):
        fig = plt.figure(figsize=(8, 8))
        plt.title("Quadtree")
        ax = fig.add_subplot(111)
        c = find_children(self.root)

        areas = set()
        for el in c:
            areas.add(el.width * el.height)

        for n in c:
            ax.add_patch(patches.Rectangle((n.x0, n.y0), n.width, n.height, fill=False))
        x = [point.x for point in self.points]
        y = [point.y for point in self.points]
        plt.plot(x, y, 'ro')
        plt.show()
        return


def find_children(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children(child))
    return children


def _recursive_subdivide(node, k):
    if len(node.points) <= k:
        return

    w_ = float(node.width / 2)
    h_ = float(node.height / 2)

    p = _contains(node.x0, node.y0, w_, h_, node.points)
    x1 = Node(node.x0, node.y0, w_, h_, p)
    _recursive_subdivide(x1, k)

    p = _contains(node.x0, node.y0 + h_, w_, h_, node.points)
    x2 = Node(node.x0, node.y0 + h_, w_, h_, p)
    _recursive_subdivide(x2, k)

    p = _contains(node.x0 + w_, node.y0, w_, h_, node.points)
    x3 = Node(node.x0 + w_, node.y0, w_, h_, p)
    _recursive_subdivide(x3, k)

    p = _contains(node.x0 + w_, node.y0 + h_, w_, h_, node.points)
    x4 = Node(node.x0 + w_, node.y0 + h_, w_, h_, p)
    _recursive_subdivide(x4, k)

    node.children = [x1, x2, x3, x4]


def _contains(x, y, w, h, points):
    pts = []
    for point in points:
        if x <= point.x <= x + w and y <= point.y <= y + h:
            pts.append(point)
    return pts
