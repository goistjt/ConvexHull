X_POS = 0
Y_POS = 1


def dist_squared(p0, p1):
    return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2


class BruteHull:
    def __init__(self, set_of_points):
        self.set_of_points = set_of_points

    def compute_hull(self):
        ext_pairs = set()
        for i in range(0, len(self.set_of_points)):
            p1 = self.set_of_points[i]
            for j in range(i + 1, len(self.set_of_points)):
                p2 = self.set_of_points[j]
                a = p2[Y_POS] - p1[Y_POS]
                b = p1[X_POS] - p2[X_POS]  # This may be the wrong order
                c = p1[X_POS] * p2[Y_POS] \
                    - p1[Y_POS] * p2[X_POS]
                all_positive = True
                all_negative = True
                same_line = []
                for k in range(0, len(self.set_of_points)):
                    # Short circuit if both are false
                    if not (all_positive or all_negative):
                        break
                    p3 = self.set_of_points[k]
                    line_val = a * p3[X_POS] + b * p3[Y_POS]
                    # Determining if all points are on the same side. pos/neg is arbitrary.
                    if line_val > c:
                        all_negative = False
                    elif line_val < c:
                        all_positive = False
                    else:  # On the same line
                        same_line.append(p3)

                if all_positive ^ all_negative:
                    if len(same_line) > 2:
                        pair_1, pair_2 = self.__get_furthest_pair(same_line)
                        ext_pairs.add((pair_1, pair_2))
                    else:
                        ext_pairs.add((p1, p2))
        return ext_pairs

    @staticmethod
    def __get_furthest_pair(same_line):
        foo = sorted(same_line, key=lambda point: point)
        return foo[0], foo[-1]
