#! python3

# Updates my music list to a txt file for alarm clock program.
# Turns out it didnt really help my project but this might be useful later
# Who knows

import os

# Checks if there are any alarm sounds in the txt that are not in the folder
# if there is it sets a variable to true to be used later
def overwrite(alarm_list):
    for alarm in alarm_list:
        if alarm not in os.listdir('C:\\AlarmClock\\alarm_sounds'):
            if alarm != '':
                missing_file = True
                return missing_file
                break
    missing_file = False
    return missing_file


# Makes the txt file if it doesn't exist.
try:
    file_creation = open('C:\\AlarmClock\\alarms.txt', 'x')
    file_creation.close()
except FileExistsError:
    pass

# Opens the file to read its contents and puts
# it in a variable before closing.
alarm_txt = open('C:\\AlarmClock\\alarms.txt', 'r')
alarm_txt_contents = alarm_txt.read()
alarm_txt.close()

# Message to show what was already in the txt.
print('Alarms already in txt: \n{}'.format(alarm_txt_contents))

# Makes an empty list and then puts each file
# in seperated by new lines.
alarm_sounds = []
alarm_sounds = alarm_txt_contents.split('\n')

# opens the list in append mode
alarm_txt = open('C:\\AlarmClock\\alarms.txt', 'a')

# Iterates through the files in my music folder and
# if it is not in the list it adds it to the txt
# with a new line for spacing.
print('Adding:\n')
for file in os.listdir('C:\\AlarmClock\\alarm_sounds'):
    if file not in alarm_sounds:
        alarm_sounds.append(file)
        file = file + '\n'
        alarm_txt.write(file)
        print(file)
alarm_txt.close()

# using the alarm_sounds list determines if an overwrite is necessary
overwrite_decision = overwrite(alarm_sounds)

# If it needs to overwrites it clears the txt and only rewrites the ones
# that are still in the folder
if overwrite_decision == True:
    print('The txt file will now overwrite')

    alarm_txt = open('C:\\AlarmClock\\alarms.txt', 'w')
    for alarm in alarm_sounds:
        if alarm not in os.listdir('C:\\AlarmClock\\alarm_sounds'):
            if alarm != '':
                print('This file is no longer in your folder: {}'.format(alarm))

        elif alarm in os.listdir('C:\\AlarmClock\\alarm_sounds'):
            alarm = alarm + '\n'
            alarm_txt.write(alarm)
    alarm_txt.close()

