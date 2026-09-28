from client import IntervalDomain

i1 = IntervalDomain(2.0, 8.0)
i2 = IntervalDomain(-3.0, 5.0)

added = i1.add(i2)
multiplied = i1.multiply(i2)
joined = i1.join(i2)

print(f"Add: [{added.low}, {added.high}]")
print(f"Multiply: [{multiplied.low}, {multiplied.high}]")
print(f"Join: [{joined.low}, {joined.high}]")
