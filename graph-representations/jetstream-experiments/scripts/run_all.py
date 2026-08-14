import subprocess
import sys

TASKS = [
    "scripts.run_benchmarks",
    "scripts.run_investigations"
]

for task in TASKS:

    print()
    print("=" * 80)
    print(f"RUNNING {task}")
    print("=" * 80)

    subprocess.run(
        [sys.executable, "-m", task],
        check=True
    )

print()
print("All benchmarks and investigations completed.")
