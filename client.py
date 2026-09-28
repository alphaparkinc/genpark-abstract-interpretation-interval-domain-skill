"""Abstract Interpretation over Interval Domain Engine.
100% Python Standard Library.
"""

class IntervalDomain:
    """Abstract interpretation interval domain [low, high] with widening."""
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def add(self, other):
        return IntervalDomain(self.low + other.low, self.high + other.high)

    def multiply(self, other):
        prods = [
            self.low * other.low, self.low * other.high,
            self.high * other.low, self.high * other.high
        ]
        return IntervalDomain(min(prods), max(prods))

    def join(self, other):
        return IntervalDomain(min(self.low, other.low), max(self.high, other.high))

    def widen(self, other):
        new_low = -float("inf") if other.low < self.low else self.low
        new_high = float("inf") if other.high > self.high else self.high
        return IntervalDomain(new_low, new_high)

    def to_dict(self):
        return {"low": self.low, "high": self.high}
