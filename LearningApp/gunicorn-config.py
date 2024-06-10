from pathlib import Path

LOG_DIR = Path("/var/log/learningapp")
SOCKET = Path("/run/learningapp.sock")

bind = "localhost:8000"
workers = 3
worker_class = "gthread"
accesslog = str(LOG_DIR / "access.log")
errorlog = str(LOG_DIR / "error.log")
proc_name = "learningapp"
threads = 4
