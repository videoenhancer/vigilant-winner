import time
import os

# A simple spinning "Claude" asterisk logo for your terminal / GitHub profile gif
frames = [
    """
       *
      ***
     *****
    ███████
     *****
      ***
       *
    """,
    """
      \\|/
     --*--
      /|\\
    """,
    """
       +
      +++
     +++++
    +++++++
     +++++
      +++
       +
    """,
    """
      \\○/
     --*--
      /○\\
    """,
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    for i in range(20):
        clear()
        print("       C L A U D E")
        print(frames[i % len(frames)])
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
