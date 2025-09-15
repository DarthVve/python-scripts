import pyautogui
import random
import time
import threading

# Scribble motion duration in seconds (30 minutes = 1800 seconds)
duration = 20 * 60
end_time = time.time() + duration
stop_script = False

# Function to stop the script when 'q' is pressed
def check_for_stop():
    global stop_script
    input("Press Enter to stop the script...")
    stop_script = True

# Start the stop-checking thread
threading.Thread(target=check_for_stop).start()

# Screen dimensions (adjust if needed)
screen_width, screen_height = pyautogui.size()

# Parameters for the scribble motion
scribble_size = 100  # Size of the scribble in pixels

while time.time() < end_time and not stop_script:
    # Generate random positions within a box for the scribble effect
    x = random.randint(0, screen_width - scribble_size)
    y = random.randint(0, screen_height - scribble_size)

    # Move the mouse to the random position in a quick motion
    pyautogui.moveTo(x, y, duration=0.1)

    # Add a short sleep to make the motion more human-like
    time.sleep(0.5)

if stop_script:
    print("Scribble motion stopped by user!")
else:
    print("Scribble motion completed!")