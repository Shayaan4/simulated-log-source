**Simulated Log Source Onboarding (MSSP-style)**

A Python-based project that simulates onboarding a log source to a central collector for cybersecurity practice. Perfect for learning basic log handling and SIEM concepts without needing VMs or root access.

**What It Does**

\-Simulates a host sending JSON logs over UDP.

\-Collects and displays logs in a central listener (“mock SIEM”).

\-No VMs, WSL, or root access required — just Python.

**Files**

**Purpose:**

```log_source.py```	Simulates a log-emitting host, sending events like login successes/failures and file accesses.

```collector.py```	Receives logs and prints them like a SIEM would.

**How to Run**

Open **terminal 1** and start the collector:

```python collector.py```


Open **terminal 2** and start the log source:

```python log_source.py```



You will see logs being sent every 2 seconds from the log source to the collector.

**Skills Demonstrated**

\-Python programming and networking basics.

\-Understanding of log source onboarding to a SIEM.

\-Simulating real-time log generation and collection.
