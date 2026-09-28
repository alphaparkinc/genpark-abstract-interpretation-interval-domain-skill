import sys
import json
from client import IntervalDomain

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "interval_arithmetic",
                        "description": "Perform abstract interval arithmetic (add, multiply, join, widen)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "op": {"type": "string", "enum": ["add", "multiply", "join", "widen"]},
                                "i1": {"type": "array", "items": {"type": "number"}},
                                "i2": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["op", "i1", "i2"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "interval_arithmetic":
            op = args["op"]
            int1 = IntervalDomain(args["i1"][0], args["i1"][1])
            int2 = IntervalDomain(args["i2"][0], args["i2"][1])
            if op == "add": res = int1.add(int2)
            elif op == "multiply": res = int1.multiply(int2)
            elif op == "join": res = int1.join(int2)
            elif op == "widen": res = int1.widen(int2)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"result": res.to_dict()})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
