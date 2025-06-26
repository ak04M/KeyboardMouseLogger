from pynput.mouse import Listener, Button
from datetime import datetime

# Log file path
log_file = "mouse_log.txt"
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write session start
with open(log_file, "a") as f:
    f.write(f"\n\n=== Mouse Logging Started: {start_time} ===\n")

# Mouse movement handler
def on_move(x, y):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - Moved to ({x}, {y})\n")

# Mouse click handler
def on_click(x, y, button, pressed):
    with open(log_file, "a") as f:
        if pressed:
            f.write(f"{datetime.now()} - {button} Pressed at ({x}, {y})\n")
        else:
            f.write(f"{datetime.now()} - {button} Released at ({x}, {y})\n")

    # Exit when Middle Click is pressed
    if pressed and button == Button.middle:
        print("[+] Middle click detected. Stopping mouse logger.")
        return False  # Stops the listener

# Mouse scroll handler
def on_scroll(x, y, dx, dy):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - Scrolled at ({x}, {y}) by ({dx}, {dy})\n")

# Start mouse listener
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
