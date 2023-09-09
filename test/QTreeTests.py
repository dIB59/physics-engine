import unittest

from particle.QTree import QTree, _find_children


class QTreeTests(unittest.TestCase):

    def test_instantiation(self):
        qt = QTree(4, 50)
        self.assertEqual(len(qt.get_points()), 50, f"Expected 50 points but got {len(qt.get_points())} points.")

    def test_add_point(self):
        qt = QTree(4, 50)
        qt.add_point(5,5)
        self.assertEqual(len(qt.get_points()), 51, f"Expected 51 points but got {len(qt.get_points())} points.")

    def test_subdivide(self):
        qt = QTree(4, 50)
        qt.subdivide()
        children = _find_children(qt.root)
        self.assertGreaterEqual(len(children), 1, f"Expected at least 1 segment but got {len(children)}.")


if __name__ == '__main__':
    unittest.main()
