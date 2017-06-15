array = """43
42
42
"""
test = [s.strip() for s in array.splitlines()]

for item in test:
    T2 = [map(int, x) for x in T1]
