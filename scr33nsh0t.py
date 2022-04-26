import os
import sys
import time
import datetime

import autopy
import pyautogui


def scr33nsh0t(file_path):
    pyautogui.screenshot().save(file_path)


if __name__ == '__main__':

    STEP_COUNT = 10
    # Criterion of stop
    if len(sys.argv) < 2:
        print("Must be run as: python3 scr33nsh0t.py <step_count>")
        print("\t", "Example: python3 scr33nsh0t.py 100")
        print("\t", "Example unlimit: python3 scr33nsh0t.py 0")
        print("")
        print("Setup <step_count> to default: 10")
    elif len(sys.argv) > 3:
        print("Must be run as: python3 scr33nsh0t.py <step_count>")
        exit(1)
    else:
        STEP_COUNT = int(sys.argv[1])

    # Path with screenshot
    BASE_REPORT_DIR = 'report'
    # Path with current task screenshots
    DATED_REPORT_DIR = datetime.datetime.now().strftime("%Y.%m.%d-%H_%M_%S")
    DATED_REPORT_DIR_FULL_PATH = os.path.join(BASE_REPORT_DIR, DATED_REPORT_DIR)
    # Formatting template
    R_JUST_LEN = 10
    R_JUST_CHR = '0'
    # Wait time for first focus setup
    FOCUS_SLEEP = 10
    # Wait time between screening
    STEP_BY_STEP_SLEEP = 1

    if not os.path.exists(DATED_REPORT_DIR_FULL_PATH):
        os.makedirs(DATED_REPORT_DIR_FULL_PATH)

    j = 0
    while FOCUS_SLEEP - j:
        print(f'Wait fo mouse focus {FOCUS_SLEEP - j} seconds')
        j += 1
        time.sleep(1)

    print(f'Let\'s go.')
    i = 0
    while not STEP_COUNT or i < STEP_COUNT:
        autopy.mouse.click()
        i += 1
        file_name = f'scr33nsh0t_{str(i).rjust(R_JUST_LEN, R_JUST_CHR)}.png'
        full_file_path = os.path.join(DATED_REPORT_DIR_FULL_PATH, file_name)
        scr33nsh0t(full_file_path)
        print(f'{full_file_path} was saved.')
        autopy.key.tap(autopy.key.Code.PAGE_DOWN)
        time.sleep(STEP_BY_STEP_SLEEP)
