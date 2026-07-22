import psutil
import socket
import time

while True:

    print("="*40)

    print(
        f"Node : {socket.gethostname()}"
    )

    print(
        f"CPU : {psutil.cpu_percent()}%"
    )

    print(
        f"Memory : {psutil.virtual_memory().percent}%"
    )

    print("="*40)

    time.sleep(30)