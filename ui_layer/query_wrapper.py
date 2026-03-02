import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INGEST_DIR = os.path.join(BASE_DIR, "ingest")

QUERY_SCRIPT = os.path.join(INGEST_DIR, "query.py")

def ask_question(question: str) -> str:
    """
    Calls existing query.py exactly the same way
    as running: cd ingest && python query.py
    """

    process = subprocess.Popen(
        [sys.executable, QUERY_SCRIPT],
        cwd=INGEST_DIR,              # 🔑 THIS IS THE FIX
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    stdout, stderr = process.communicate(question + "\nexit\n")

    if process.returncode != 0:
        raise RuntimeError(stderr)

    return stdout
