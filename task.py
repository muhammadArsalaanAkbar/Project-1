"""Long-running demo task for the Concept 4 in-session loop exercise.

Simulates ~3 minutes of work, then writes a status file marking completion.
Run in the background so an in-session monitoring loop can poll for it.
"""

import time

DURATION_SECONDS = 180
STATUS_FILE = "task_status.txt"

time.sleep(DURATION_SECONDS)

with open(STATUS_FILE, "w") as f:
    f.write("done\n")
