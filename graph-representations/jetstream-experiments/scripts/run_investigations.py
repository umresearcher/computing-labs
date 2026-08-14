import subprocess
import sys

INVESTIGATIONS = [
    "scripts.investigations.investigate_degrees",
    "scripts.investigations.investigate_influencers",
    "scripts.investigations.investigate_central_nodes",
    "scripts.investigations.investigate_communities",
    "scripts.investigations.investigate_bridge_nodes",
    "scripts.investigations.investigate_small_world"
]

for investigation in INVESTIGATIONS:

    print()
    print("=" * 80)
    print(f"RUNNING {investigation}")
    print("=" * 80)

    subprocess.run(
        [sys.executable, "-m", investigation],
        check=True
    )

print()
print("All investigations completed.")
