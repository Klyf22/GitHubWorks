import time
import os

# Function to clear the screen
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# The text to display
text = "my heart blinks for you"
text1 = "so what"

# Main loop to make the text blink
while True:
    clear_screen()
    print(text)
    time.sleep(0.5)
    print(text1)
    time.sleep(0.25)
    clear_screen()
    time.sleep(0.50)
