# Create user-defined class named Stats 

"""
stats.py

User-defined module containing the Stats class.
Provides mean, median, and mode calculations.
"""


class Stats:
    """Provides basic statistical methods: mean, median, and mode."""

    def mean(self, data: list) -> str:
        result = sum(data) // len(data)
        return f"mean: {result}"

    def median(self, data: list) -> str:
        sorted_data = sorted(data)
        mid = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            result = (sorted_data[mid - 1] + sorted_data[mid]) // 2
        else:
            result = sorted_data[mid]
        return f"median: {result}"

    def mode(self, data: list) -> str:
        result = max(set(data), key=data.count)
        return f"mode: {result}"
    
    """Provides additional common statistical methods"""
    def minimum(self, data: list) -> str:
        result = min(data)
        return f"min: {result}"

    def maximum(self, data: list) -> str:
        result = max(data)
        return f"max: {result}"

    def data_range(self, data: list) -> str:
        result = max(data) - min(data)
        return f"range: {result}"

    def count(self, data: list) -> str:
        result = len(data)
        return f"count: {result}"

    def variance(self, data: list) -> str:
        avg = sum(data) / len(data)
        result = round(sum((x - avg) ** 2 for x in data) / len(data), 2)
        return f"variance: {result}"

    def std_dev(self, data: list) -> str:
        avg = sum(data) / len(data)
        result = round((sum((x - avg) ** 2 for x in data) / len(data)) ** 0.5, 2)
        return f"std_dev: {result}"

    def linear_regression(self, x: list, y: list) -> str:
        n = len(x)
        slope = (n * sum(xi * yi for xi, yi in zip(x, y)) - sum(x) * sum(y)) / \
                (n * sum(xi ** 2 for xi in x) - sum(x) ** 2)
        intercept = (sum(y) - slope * sum(x)) / n
        return f"linear_regression: y = {round(slope, 2)}x + {round(intercept, 2)}"

    def r_squared(self, x: list, y: list) -> str:
        n = len(x)
        slope = (n * sum(xi * yi for xi, yi in zip(x, y)) - sum(x) * sum(y)) / \
                (n * sum(xi ** 2 for xi in x) - sum(x) ** 2)
        intercept = (sum(y) - slope * sum(x)) / n
        y_mean = sum(y) / n
        ss_res = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
        ss_tot = sum((yi - y_mean) ** 2 for yi in y)
        return f"r_squared: {round(1 - ss_res / ss_tot, 4)}"

    def predict(self, x: list, y: list, x_new: float) -> str:
        n = len(x)
        slope = (n * sum(xi * yi for xi, yi in zip(x, y)) - sum(x) * sum(y)) / \
                (n * sum(xi ** 2 for xi in x) - sum(x) ** 2)
        intercept = (sum(y) - slope * sum(x)) / n
        result = round(slope * x_new + intercept, 2)
        return f"predict({x_new}): {result}"
