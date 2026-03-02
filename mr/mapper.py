#!/usr/bin/env python3
import subprocess
import sys

def count_lines_hdfs(path: str) -> int:
    p = subprocess.Popen(
        ["hdfs", "dfs", "-cat", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    data = p.stdout.read() if p.stdout else b""
    return data.count(b"\n")

def main():
    for line in sys.stdin:
        hdfs_path = line.strip()
        if not hdfs_path:
            continue
        n = count_lines_hdfs(hdfs_path)
        sys.stdout.write(f"{hdfs_path}\t{n}\n")

if __name__ == "__main__":
    main()