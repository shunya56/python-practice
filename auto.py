import pyautogui
import time
import datetime


def auto_move():
    start = datetime.datetime.now()
    end = start + datetime.timedelta(minutes=120)
    print(start)
    print(end)

    while True:
        time.sleep(3)
        pyautogui.moveTo(500, 500, duration=3)
        pyautogui.moveTo(100, 100, duration=3)

        if datetime.datetime.now() >= end:
            print("stopped by timeout")
            break


if __name__ == '__main__':
    auto_move()