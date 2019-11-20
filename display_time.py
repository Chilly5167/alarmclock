#! python3
# Displays time

import time, sys

try:
    while True:
        # Takes the current time
        lt = time.localtime()

        # If the hour is in the pm then it removes 12 hours
        # this is to display non-24 hour time.
        if lt.tm_hour > 12:
            lt_hour = lt.tm_hour - 12
        else:
            lt_hour = lt.tm_hour

        # If the minute is not double digits it adds a 0 in front
        if lt.tm_min <= 9:
            lt_min = '0{}'.format(lt.tm_min)
        else:
            lt_min = lt.tm_min

        # Saves the message in a variable which is printed without
        # a new line and then erases the last message
        time_now = '{}:{}'.format(lt_hour, lt.tm_min)
        print(time_now, end='')
        print('\b' * len(time_now), end='', flush=True)
        time.sleep(1)
    
# CTRL-c to exit
except KeyboardInterrupt:
    print('Exiting')
    sys.exit()
