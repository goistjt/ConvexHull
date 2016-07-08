from src.BruteHull import BruteHull
from src.QuickHull import QuickHull
from src.graphics import *


def collect_points(path):
    try:
        with open(path, "r") as point_file:
            lines = point_file.read().split('\n')
            if lines[-1] == '':
                lines = lines[:-1]  # Removing the extra line
            set_of_points = []
            for line in lines:
                tuples = line.split(', ')
                for pair in tuples:
                    x_y = pair.replace('(', '').replace(')', '').split(',')
                    set_of_points.append(tuple(map(int, x_y)))
            return set_of_points
    except IOError:
        print("An error occurred while reading the text file. Aborting.")
        exit()


def render_brute_hull(ext_pairs, int_points):
    window = GraphWin("Brute Force Convex Hull", width=1920, height=1080)
    for point in int_points:
        draw_point(point, window)
    for i in range(0, len(ext_pairs)):
        p1, p2 = ext_pairs[i]
        draw_point_line(p1, p2, window)
    window.wait_window()


def render_quick_hull(ext_points, int_points):
    window = GraphWin("Quick Convex Hull", width=1920, height=1080)
    draw_point_line(ext_points[0], ext_points[-1], window)
    for point in int_points:
        draw_point(point, window)
    for i in range(1, len(ext_points)):
        p1 = ext_points[i-1]
        p2 = ext_points[i]
        draw_point_line(p1, p2, window)
    window.wait_window()


def draw_point(point, window):
    p = Point(point[0], point[1])
    c = Circle(p, 2)
    c.setFill("black")
    c.draw(window)


def draw_point_line(p1, p2, window):
    point_1 = Point(p1[0], p1[1])
    point_2 = Point(p2[0], p2[1])
    c1 = Circle(point_1, 4)
    c1.setFill("red")
    c1.setOutline("red")
    c2 = Circle(point_2, 4)
    c2.setFill("red")
    c2.setOutline("red")
    line = Line(point_1, point_2)
    line.setWidth(3)
    line.setFill("red")
    c1.draw(window)
    c2.draw(window)
    line.draw(window)


def main():
    filepath = input("Please input a filepath: ")
    algo = input("Which algorithm would you like to use? (BRUTE/QUICK): ")
    print("Collecting points from file")
    start = time.time()
    points = collect_points(filepath)
    print("Finished collecting {} points".format(len(points)))
    print("Time to collect: {} seconds".format(time.time() - start))
    if algo == 'BRUTE':
        start = time.time()
        ext_points = BruteHull(points).compute_hull()
        print("Brute Hull Computed in: {} seconds".format(time.time() - start))
        render_brute_hull(ext_points, points)
    elif algo == 'QUICK':
        start = time.time()
        points = sorted(points, key=lambda point: point)
        # This sorts the elements first by x, then by y (ascending)
        # From the documentation in Python implementation - "adaptive, stable, natural mergesort" -> O(n log n)
        ext_points = QuickHull(points).compute_hull()
        print("Quick Hull Computed in: {} seconds".format(time.time() - start))
        render_quick_hull(ext_points, points)
    else:
        print("Incorrect algorithm input. Aborting.")
        exit()


if __name__ == '__main__':
    main()
