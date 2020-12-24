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
time.sleep(ACTION_TIME_SEC)
playbackTabCoords = pyautogui.locateCenterOnScreen('playback_tab.png')
if (playbackTabCoords == None):
    print('Could not find Playback tab, exit...')
    sys.exit(1)
pyautogui.leftClick(playbackTabCoords[0], playbackTabCoords[1])

# Open Speakers device
deviceCoords = pyautogui.locateCenterOnScreen('audio_device.png')
if (deviceCoords == None):
    print('Could not find Device entry, exit...')
    sys.exit(1)
pyautogui.doubleClick(deviceCoords[0], deviceCoords[1])

# Go to Advanced settings tab
time.sleep(ACTION_TIME_SEC)
advancedTabCoords = pyautogui.locateCenterOnScreen('advanced_tab.png')
if (advancedTabCoords == None):
    print('Could not find Advanced tab, exit...')
    sys.exit(1)
pyautogui.leftClick(advancedTabCoords[0], advancedTabCoords[1])

# Click on audio format dropdown
formatDropdownCoords = pyautogui.locateCenterOnScreen('dropdown.png')
if (formatDropdownCoords == None):
    print('Could not find Format dropdown, exit...')
    sys.exit(1)
pyautogui.leftClick(formatDropdownCoords[0], formatDropdownCoords[1])

# Select Studio quality format
pyautogui.moveRel(studioQualityOffset['x'], studioQualityOffset['y'], .2)
pyautogui.leftClick()

# Test the audio
testButtonCoords = pyautogui.locateCenterOnScreen('test_button.png')
if (testButtonCoords == None):
    print('Could not find Test button, exit...')
    sys.exit(1)
pyautogui.leftClick(testButtonCoords[0], testButtonCoords[1])

# Close warning dialog if it pops up
time.sleep(ACTION_TIME_SEC/2)
warningYesCoords = pyautogui.locateCenterOnScreen('warning_yes.png')
if (warningYesCoords == None):
    print('Could not find Warning "yes" button, continue...')
else:
    pyautogui.leftClick(warningYesCoords[0], warningYesCoords[1])

# Stop the audio test
# stopButtonCoords = pyautogui.locateCenterOnScreen('stop_button.png')
pyautogui.leftClick(testButtonCoords[0], testButtonCoords[1])

# Click on audio format dropdown
pyautogui.leftClick(formatDropdownCoords[0], formatDropdownCoords[1], 0, .5)

# Select DVD quality format
pyautogui.moveRel(dvdQualityOffset['x'], dvdQualityOffset['y'], .2)
pyautogui.leftClick()

# Close second panel
okButtonCoords = pyautogui.locateCenterOnScreen('ok_button.png')
if (okButtonCoords == None):
    print('Could not find OK button, exit...')
    sys.exit(1)
pyautogui.leftClick(okButtonCoords[0], okButtonCoords[1])

# Close first panel
time.sleep(ACTION_TIME_SEC/2)
okButtonCoords = pyautogui.locateCenterOnScreen('ok_button.png')
if (okButtonCoords == None):
    print('Could not find OK button, exit...')
    sys.exit(1)
pyautogui.leftClick(okButtonCoords[0], okButtonCoords[1])

print('Done resetting sound format.')
