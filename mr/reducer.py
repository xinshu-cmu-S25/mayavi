#!/usr/bin/env python3
import sys

def main():
    current_key = None
    total = 0

    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue

        try:
            key, value = line.split("\t", 1)
            value = int(value)
        except Exception:
            continue

        if current_key is None:
            current_key = key

        if key != current_key:
            print(f"{current_key}\t{total}")
            current_key = key
            total = 0

        total += value

    if current_key is not None:
        print(f"{current_key}\t{total}")

if __name__ == "__main__":
    main()