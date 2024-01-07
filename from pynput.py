from pynput.mouse import Listener
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def on_move(x, y):
    global last_time, last_print_time, total_polling_rate, count
    current_time = time.time()
    if last_time is not None:
        interval = current_time - last_time
        if interval > 0:
            polling_rate = 1 / interval
            total_polling_rate += polling_rate
            count += 1
            if current_time - last_print_time >= print_interval:
                clear_screen()
                average_polling_rate = total_polling_rate / count
                print(f"Current Polling Rate: {polling_rate:.2f} Hz")
                print(f"Average Polling Rate: {average_polling_rate:.2f} Hz")
                last_print_time = current_time
    last_time = current_time

last_time = None
last_print_time = 0
total_polling_rate = 0
count = 0
print_interval = 0.1  # Adjust the interval as needed

with Listener(on_move=on_move) as listener:
    listener.join()
