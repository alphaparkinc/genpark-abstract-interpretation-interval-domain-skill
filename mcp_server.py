import sys
import json
from client import IntervalDomainAnalyzer

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "analyze":
        analyzer = IntervalDomainAnalyzer()
        return analyzer.analyze_binary_op(tuple(params.get("int1", (0, 1))), tuple(params.get("int2", (1, 2))), params.get("op", "+"))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
