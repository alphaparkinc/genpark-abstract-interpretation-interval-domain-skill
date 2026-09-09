from client import IntervalDomainAnalyzer

def main():
    print("=== Abstract Interpretation Interval Domain ===")
    analyzer = IntervalDomainAnalyzer()
    res = analyzer.analyze_binary_op((1.0, 3.0), (2.0, 5.0), "+")
    print("Analysis Result:", res)
    assert res["abstract_interval"] == [3.0, 8.0]
    assert res["contains_zero"] is False

    print("Interval Domain Analyzer verified successfully!")

if __name__ == "__main__":
    main()
