# Uses python3
import sys


class Item:
    value = 0.
    weight = 0.
    vw_ratio = 0.

    def __init__(self, value, weight, vw_ratio):
        self.value = value
        self.weight = weight
        self.vw_ratio = vw_ratio


def get_items(values, weights):
    return [Item(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]


def get_optimal_value(capacity, weights, values):
    value = 0.
    items = get_items(values, weights)
    items.sort(key=lambda obj: obj.vw_ratio)

    while capacity > 0 and len(items) != 0:
        item = items.pop()
        weight = min(item.weight, capacity)
        value += weight * (item.vw_ratio)
        item.weight -= weight
        capacity -= weight

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
