import subprocess
import sys

BENCHMARKS = [
    "scripts.benchmarks.benchmark_neighbors",
    "scripts.benchmarks.benchmark_common_neighbors",
    "scripts.benchmarks.benchmark_connected_to_all",
    "scripts.benchmarks.benchmark_reachability"
]

for benchmark in BENCHMARKS:

    print()
    print("=" * 80)
    print(f"RUNNING {benchmark}")
    print("=" * 80)

    subprocess.run(
        [sys.executable, "-m", benchmark],
        check=True
    )

print()
print("All benchmarks completed.")
