# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def fast_count_segments(starts, ends, points):
    # segments.sort(key= lambda x : x.end)

    cnt = [0] * len(points)

    starts.sort()
    ends.sort()

    points.sort()

    upper_segment = []
    lower_segment = []

    for point in points:
        for start in starts:
            if point < start:
                break
            elif point >= start:
                upper_segment.append(point)

    for point in points:
        for end in ends:
            if point > end:
                break
            elif point <= end:
                lower_segment.append(point)
    print(lower_segment)
    print(upper_segment)

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[2:2 * n + 2:2], data[3:2 * n + 2:2])))
    ends = data[3:2 * n + 2:2]
    starts = data[2:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
