import sys

for line in sys.stdin:
    path = line.strip()
    if not path:
        continue
    try:
        with open(path, 'r', errors='ignore') as f:
            c = 0
            for _ in f:
                c += 1
        print(f"\"{path}\":\t{c}")
    except Exception:
        pass