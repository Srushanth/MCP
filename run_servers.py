import subprocess
import sys
import os
import time
from threading import Thread

# List of servers: (name, project_path, script_path)
SERVERS = [
    ("bandit", "mcp-server-bandit", "mcp-server-bandit/src/main.py"),
    ("black", "mcp-server-black-formatter", "mcp-server-black-formatter/src/main.py"),
    ("directory", "mcp-server-directry-management", "mcp-server-directry-management/src/main.py"),
    ("pyright", "mcp-server-pyright", "mcp-server-pyright/src/main.py"),
    ("pytest", "mcp-server-pytest", "mcp-server-pytest/src/main.py"),
    ("radon", "mcp-server-radon", "mcp-server-radon/src/main.py"),
    ("ruff", "mcp-server-ruff", "mcp-server-ruff/src/main.py"),
    ("secret-scan", "mcp-server-secret-scan", "mcp-server-secret-scan/src/main.py"),
]

processes = []

def log_output(name, process):
    # Read output and print it with prefix
    while True:
        line = process.stdout.readline()
        if not line:
            break
        sys.stdout.write(f"[{name}] {line.decode('utf-8', errors='replace')}")

def log_error(name, process):
    # Read stderr and print it with prefix
    while True:
        line = process.stderr.readline()
        if not line:
            break
        sys.stderr.write(f"[{name}] {line.decode('utf-8', errors='replace')}")

def main():
    print("Starting all MCP servers concurrently...")
    for name, proj, script in SERVERS:
        # Start server in a subprocess
        p = subprocess.Popen(
            ["uv", "run", "--project", proj, script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
        )
        processes.append((name, p))
        
        # Start threads to read stdout and stderr asynchronously
        t_out = Thread(target=log_output, args=(name, p), daemon=True)
        t_err = Thread(target=log_error, args=(name, p), daemon=True)
        t_out.start()
        t_err.start()
        print(f"  -> Started {name} server process.")
        time.sleep(0.3)  # Brief delay to prevent console logging collision

    print("\nAll servers started. Press Ctrl+C to terminate all of them.\n")
    
    try:
        while True:
            time.sleep(1)
            # Check if any process has exited unexpectedly
            for name, p in processes:
                exit_code = p.poll()
                if exit_code is not None:
                    print(f"\n[!] Server '{name}' exited unexpectedly with code {exit_code}")
                    sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n[!] Ctrl+C detected. Shutting down all servers...")
    finally:
        # Terminate all processes
        for name, p in processes:
            if p.poll() is None:
                print(f"Stopping '{name}'...")
                p.terminate()
        
        # Wait for all processes to close, force kill if they don't exit in 3s
        for name, p in processes:
            try:
                p.wait(timeout=3)
            except subprocess.TimeoutExpired:
                print(f"Force-killing '{name}'...")
                p.kill()
        print("All servers stopped successfully.")

if __name__ == "__main__":
    main()
