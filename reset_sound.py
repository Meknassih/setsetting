import pyautogui
import sys
import time

sysTrayIconCoords = {'x': 21, 'y': 931}
soundsMenuCoords = {'x': 161, 'y': 880}
dvdQualityOffset = {'x': 0, 'y': 30}
studioQualityOffset = {'x': 0, 'y': 44}
okWarningCoords = {'x': 1051, 'y': 623}
okDeviceCoords = {'x': 400, 'y': 612}
okPlaybackCoords = {'x': 365, 'y': 540}
ACTION_TIME_SEC = .8

# Open Sounds panel
pyautogui.rightClick(sysTrayIconCoords['x'], sysTrayIconCoords['y'])
pyautogui.leftClick(soundsMenuCoords['x'], soundsMenuCoords['y'])

# Go to Playback devices tab
playbackTabCoords = pyautogui.locateCenterOnScreen('playback_tab.png')
while (playbackTabCoords == None):
    playbackTabCoords = pyautogui.locateCenterOnScreen('playback_tab.png')
    # print('Could not find Playback tab, exit...')
    # sys.exit(1)
pyautogui.leftClick(playbackTabCoords[0], playbackTabCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Open Speakers device
deviceCoords = pyautogui.locateCenterOnScreen('audio_device.png')
while (deviceCoords == None):
    deviceCoords = pyautogui.locateCenterOnScreen('audio_device.png')
    # print('Could not find Device entry, exit...')
    # sys.exit(1)
pyautogui.doubleClick(deviceCoords[0], deviceCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Go to Advanced settings tab
advancedTabCoords = pyautogui.locateCenterOnScreen('advanced_tab.png')
while (advancedTabCoords == None):
    advancedTabCoords = pyautogui.locateCenterOnScreen('advanced_tab.png')
    # print('Could not find Advanced tab, exit...')
    # sys.exit(1)
pyautogui.leftClick(advancedTabCoords[0], advancedTabCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Click on audio format dropdown
formatDropdownCoords = pyautogui.locateCenterOnScreen('dropdown.png')
while (formatDropdownCoords == None):
    formatDropdownCoords = pyautogui.locateCenterOnScreen('dropdown.png')
    # print('Could not find Format dropdown, exit...')
    # sys.exit(1)
pyautogui.leftClick(formatDropdownCoords[0], formatDropdownCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Select Studio quality format
pyautogui.moveRel(studioQualityOffset['x'], studioQualityOffset['y'])
pyautogui.leftClick()

# Test the audio
testButtonCoords = pyautogui.locateCenterOnScreen('test_button.png')
while (testButtonCoords == None):
    testButtonCoords = pyautogui.locateCenterOnScreen('test_button.png')
    # print('Could not find Test button, exit...')
    # sys.exit(1)
pyautogui.leftClick(testButtonCoords[0], testButtonCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Close warning dialog if it pops up
time.sleep(ACTION_TIME_SEC/2)
warningYesCoords = pyautogui.locateCenterOnScreen('warning_yes.png')
if (warningYesCoords == None):
    print('Could not find Warning "yes" button, continue...')
else:
    pyautogui.leftClick(warningYesCoords[0], warningYesCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Stop the audio test
# stopButtonCoords = pyautogui.locateCenterOnScreen('stop_button.png')
pyautogui.leftClick(testButtonCoords[0], testButtonCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Click on audio format dropdown
pyautogui.leftClick(formatDropdownCoords[0], formatDropdownCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Select DVD quality format
pyautogui.moveRel(dvdQualityOffset['x'], dvdQualityOffset['y'])
pyautogui.leftClick()

# Close second panel
okButtonCoords = pyautogui.locateCenterOnScreen('ok_button.png')
while (okButtonCoords == None):
    okButtonCoords = pyautogui.locateCenterOnScreen('ok_button.png')
    # print('Could not find OK button, exit...')
    # sys.exit(1)
pyautogui.leftClick(okButtonCoords[0], okButtonCoords[1])

# DEBUG
# input("Press Enter to continue...")

# Close first panel
okButtonCoords = pyautogui.locateCenterOnScreen('ok_button.png')
while (okButtonCoords == None):
    okButtonCoords = pyautogui.locateCenterOnScreen('ok_button.png')
    # print('Could not find OK button, exit...')
    # sys.exit(1)
pyautogui.leftClick(okButtonCoords[0], okButtonCoords[1])

print('Done resetting sound format.')
