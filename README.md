# Project 1 — In-Session Monitoring Loop (Concept 4)

Demonstrates Concept 4 from the Harness Engineering crash course: using an
in-session loop inside a Claude Code session to monitor a long-running
background task to completion.

## Purpose

Show the full lifecycle of an in-session monitoring loop:

1. Start a long-running task in the background.
2. Poll for its completion on a fixed interval, without blocking the session.
3. Detect completion and report it exactly once.
4. Stop the monitoring loop cleanly instead of polling forever.

## Files

- `task.py` — the long-running task. Sleeps for ~3 minutes, then writes
  `task_status.txt` containing `done`. This file is the completion signal
  the monitoring loop watches for.

There is no separate monitor script. The monitoring loop itself is not
application code — it's the Claude Code session polling on a timer
(`ScheduleWakeup`), checking for `task_status.txt` each time it wakes,
and stopping the loop as soon as the file appears.

## Workflow

1. **Start the task in the background:**
   ```
   python task.py
   ```
   (run as a background process so the session stays free to do other work)

2. **Monitor in-session:** the session schedules a wakeup ~60 seconds out,
   and each time it wakes it checks whether `task_status.txt` exists.
   - Not done yet → schedule the next 60-second check.
   - Done → report completion once, then stop the loop.

3. **Stop cleanly:** once completion is detected and reported, the loop is
   explicitly stopped (no further wakeups are scheduled) rather than left
   to keep polling a finished task.

## Running it

```
python task.py
```

Then, within a Claude Code session, ask it to start `task.py` in the
background and monitor it — it will handle the 60-second polling loop and
report back once, when `task_status.txt` appears.

`task_status.txt` is generated at runtime and is git-ignored.
