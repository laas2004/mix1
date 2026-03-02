# import subprocess
# import sys
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# INGEST_SCRIPT = os.path.join(
#     BASE_DIR,
#     "ingest",
#     "ingest_to_chroma.py"
# )

# def ingest_pdf(pdf_path: str):
#     """
#     Calls the existing ingest_to_chroma.py script
#     WITHOUT modifying it.
#     """

#     result = subprocess.run(
#         [sys.executable, INGEST_SCRIPT, pdf_path],
#         capture_output=True,
#         text=True
#     )

#     if result.returncode != 0:
#         raise RuntimeError(result.stderr)

#     return result.stdout

# v2
# import subprocess
# import os
# import sys

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# INGEST_DIR = os.path.join(BASE_DIR, "ingest")
# INGEST_SCRIPT = os.path.join(INGEST_DIR, "ingest_to_chroma.py")

# def ingest_pdf() -> str:
#     """
#     Runs ingest_to_chroma.py from inside the ingest folder
#     so relative paths like '../data/pdfs' work correctly.
#     """

#     result = subprocess.run(
#         [sys.executable, INGEST_SCRIPT],
#         cwd=INGEST_DIR,          # 🔥 THIS IS THE KEY FIX
#         capture_output=True,
#         text=True,
#         encoding="utf-8",
#         errors="replace"
#     )

#     if result.returncode != 0:
#         error_message = result.stderr or result.stdout or "Unknown ingestion error"
#         raise RuntimeError(error_message)

#     return result.stdout



import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
INGEST_DIR = os.path.join(BASE_DIR, "ingest")
INGEST_SCRIPT = os.path.join(INGEST_DIR, "ingest_to_chroma.py")

def ingest_pdf(status_callback=None) -> str:
    """
    Runs ingest_to_chroma.py and streams logs in real-time.
    status_callback(line) -> used to update pipeline status
    """

    process = subprocess.Popen(
        [sys.executable, INGEST_SCRIPT],
        cwd=INGEST_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    logs = []

    # Read output line by line
    for line in iter(process.stdout.readline, ''):
        line = line.strip()
        if line:
            print("[INGEST]", line)
            logs.append(line)

            # Send update to API server
            if status_callback:
                status_callback(line)

    process.wait()

    if process.returncode != 0:
        raise RuntimeError("\n".join(logs) or "Unknown ingestion error")

    return "\n".join(logs)
