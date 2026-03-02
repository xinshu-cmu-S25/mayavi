#!/usr/bin/env python3
import os
import sys

def main():
    path = (
        os.environ.get("mapreduce_map_input_file")
        or os.environ.get("map_input_file")
        or "UNKNOWN_FILE"
    )

    data = sys.stdin.buffer.read()
    line_count = data.count(b"\n")

    sys.stdout.write(f"{path}\t{line_count}\n")

if __name__ == "__main__":
    main()
