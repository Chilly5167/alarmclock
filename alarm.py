#! python3
# command line alarm clock without the display
# Plays a random song each time
# Press CTRL-C to exit

import sys, time, random, os
from playsound import playsound




def alarm(hour, minute, am_pm):
    if am_pm.lower() == 'pm' or am_pm.lower() == 'am':
        hour, minute = int(hour), int(minute)
        if 1 <= hour <= 24:
            if 0 <= minute <= 59:

                # makes the clock usable without entering in 24 hour
                if am_pm.lower() == 'pm' and hour != 12:
                    hour = hour + 12
                if am_pm.lower() == 'am' and hour == 12:
                    hour = hour +12

                # puts every file that is in a folder full of music
                # in a list and a song is randomly chosen
                alarm_sounds = []
                for file in os.listdir('C:\\AlarmClock\\alarm_sounds'):
                    alarm_sounds.append(file)
                chosen_sound = random.choice(alarm_sounds)
                
                # now is the current time in the struct_time class
                now = time.localtime()
                # using the now times and the inputed times to set a date
                # for the alarm
                full_time = (now.tm_year, now.tm_mon, now.tm_mday, hour, minute, 0, now.tm_wday, now.tm_yday, 0)
                alarm_time = time.mktime(full_time)
                # the seconds between the current time and when the alarm is set for
                countdown = alarm_time - time.time()
                
                # If the time has already passed on the day the alarm was set
                # It adds a full day to the alarm time
                if countdown < 0:
                    # 86400 is the seconds in a full day
                    alarm_time = alarm_time + 86400
                    countdown = alarm_time - time.time()

                print('Your alarm is set for {}'.format(time.ctime(alarm_time)))
                print('Sleeping for {} seconds'.format(round(countdown)))
                
                # sleeps in small interval to allow for keyboard interupt
                # updates the countdown each loop
                while alarm_time > time.time():
                    time.sleep(0.1)
                print('Alarm')
                print('Playing: {}'.format(chosen_sound))
                playsound('C:\\AlarmClock\\alarm_sounds\\{}'.format(chosen_sound))
                
            else:
                print('Invalid minute')
        else:
            print('Invalid hour')
    else:
        print('Invalid am or pm choice')



# if there isn't two command line arugments it doesn't run and gives this message
if len(sys.argv) != 3:
    print('Usage example: python alarm_clock.py 7:45 pm')
    print('Press Ctrl-C to exit an alarm early')
    sys.exit()

# uses command line arguments
hour, minute = sys.argv[1].split(':')
am_pm = sys.argv[2]

try:
    alarm(hour, minute, am_pm)
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
