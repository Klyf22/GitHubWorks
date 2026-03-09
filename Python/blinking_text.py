import time
import os

# Function to clear the screen
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# The text to display
text = "my heart blinks for you"

# Main loop to make the text blink
while True:
    clear_screen()
    print(text)
    time.sleep(0.5)
    clear_screen()
    time.sleep(0.5)