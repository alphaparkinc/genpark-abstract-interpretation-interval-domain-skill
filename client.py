class IntervalDomainAnalyzer:
    """Interval domain static analysis."""
    def analyze_binary_op(self, int1: tuple[float, float], int2: tuple[float, float], op: str) -> dict:
        l1, h1 = int1
        l2, h2 = int2
        if op == "+":
            res = (l1 + l2, h1 + h2)
        elif op == "*":
            products = [l1 * l2, l1 * h2, h1 * l2, h1 * h2]
            res = (min(products), max(products))
        elif op == "-":
            res = (l1 - h2, h1 - l2)
        else:
            res = (min(l1, l2), max(h1, h2))

        return {
            "interval_1": list(int1),
            "interval_2": list(int2),
            "op": op,
            "abstract_interval": [round(res[0], 4), round(res[1], 4)],
            "contains_zero": (res[0] <= 0 <= res[1])
        }
