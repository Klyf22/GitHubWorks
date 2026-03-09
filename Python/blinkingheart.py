import time
import os

# Function to clear the screen
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Heart ASCII art with filled and empty hearts
heart_filled = """
   ♥♥♥   ♥♥♥
  ♥   ♥ ♥   ♥
  ♥     ♥     ♥
   ♥   ♥   ♥
    ♥ ♥   ♥ ♥
     ♥     ♥
      ♥   ♥
       ♥ ♥
        ♥
"""

heart_empty = """
   ♡♡♡   ♡♡♡
  ♡   ♡ ♡   ♡
  ♡     ♡     ♡
   ♡   ♡   ♡
    ♡ ♡   ♡ ♡
     ♡     ♡
      ♡   ♡
       ♡ ♡
        ♡
"""

# Main loop to make the heart blink
while True:
    clear_screen()
    print(heart_filled)
    time.sleep(0.5)
    clear_screen()
    print(heart_empty)
    time.sleep(0.5)