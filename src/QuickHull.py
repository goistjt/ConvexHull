X_POS = 0
Y_POS = 1


def tri_area(left, right, point):
    return left[X_POS] * right[Y_POS] + point[X_POS] * left[Y_POS] + right[X_POS] * point[Y_POS] \
           - point[X_POS] * right[Y_POS] - right[X_POS] * left[Y_POS] - left[X_POS] * point[Y_POS]


def find_furthest_point(left, right, set_of_points):
    max_area = 0
    max_point = None
    for point in set_of_points:
        area = tri_area(left, right, point)
        if area > max_area:
            max_area = area
            max_point = point
    return max_point


def get_left_right_points(left, right, points):
    left_line = set()
    right_line = set()
    # This divides the points into two disjoint sets - left & right of line
    for point in points:
        area = tri_area(left, right, point)
        if area > 0:
            left_line.add(point)
        elif area < 0:
            right_line.add(point)
    return left_line, right_line


class QuickHull:
    def __init__(self, set_of_points):
        self.set_of_points = set_of_points
        self.ext_points = []

    def compute_hull(self):
        left = self.set_of_points[0]
        right = self.set_of_points[-1]
        self.ext_points.append(left)
        self.ext_points.append(right)

        #  Left of the line direction is considered UP
        upper, lower = get_left_right_points(left, right, self.set_of_points)
        self.__find_hull(left=upper, P=left, Q=right)
        self.__find_hull(left=lower, P=right, Q=left)
        return self.ext_points

    def __find_hull(self, left, P, Q):
        if len(left) == 0:
            return
        C = find_furthest_point(P, Q, left)
        self.ext_points.insert(self.ext_points.index(Q), C)

        s1, foo = get_left_right_points(P, C, left)
        s2, foo = get_left_right_points(C, Q, left)
        self.__find_hull(s1, P, C)
        self.__find_hull(s2, C, Q)
