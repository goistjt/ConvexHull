import oset

X_POS = 0
Y_POS = 1


def dist_squared(p0, p1):
    return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2


class BruteHull:
    def __init__(self, set_of_points):
        self.set_of_points = set_of_points

    def compute_hull(self):
        ext_pairs = oset.oset()
        for i in range(0, len(self.set_of_points)):
            p1 = self.set_of_points[i]
            for j in range(i + 1, len(self.set_of_points)):
                p2 = self.set_of_points[j]
                a = p2[Y_POS] - p1[Y_POS]
                b = p1[X_POS] - p2[X_POS]  # This may be the wrong order
                c = p1[X_POS] * p2[Y_POS] \
                    - p1[Y_POS] * p2[X_POS]
                dist = dist_squared(p1, p2)
                all_positive = True
                all_negative = True
                # same_line = set()
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
                        p3_1_dist = dist_squared(p1, p3)
                        p3_2_dist = dist_squared(p2, p3)
                        if p3_1_dist > dist:
                            dist = p3_1_dist
                            p2 = p3
                        elif p3_2_dist > dist:
                            dist = p3_2_dist
                            p1 = p3
                            # same_line.add(self.set_of_points[k])

                if all_positive ^ all_negative:
                    # lsl = len(same_line)
                    # if lsl > 2:
                    #     max_points = self.__get_furthest_pair(lsl, same_line)
                    #     ext_pairs.add((max_points[0], max_points[1]))
                    # else:
                    ext_pairs.add((p1, p2))
        return ext_pairs

    @staticmethod
    def __get_furthest_pair(lsl, same_line):
        x = []
        y = []
        for point in same_line:
            x.append(point[0])
            y.append(point[1])
        midpoint = (sum(x) / lsl, sum(y) / lsl)
        max_d = [0, 0]
        max_points = [None, None]
        for point in same_line:
            if max_d[0] < max_d[1]:
                to_compare = 0
            else:
                to_compare = 1
            p_dist = dist_squared(midpoint, point)
            if p_dist > max_d[to_compare]:
                max_d[to_compare] = p_dist
                max_points[to_compare] = point
        return max_points
