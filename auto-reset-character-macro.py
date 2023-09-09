import pyautogui
import keyboard
import threading
import time
#import subprocess (part of old code)

# Func for pressing keys
def press_da_keys(list_of_keys):
    for key in list_of_keys:
        keyboard.press_and_release(key)
        time.sleep(0.25)

# Func for getting mouse coords autoclicker style
def get_mouse_position(default_x=1569, default_y=90):
    while True:
        if keyboard.is_pressed('esc'): # SET
            return pyautogui.position()
        elif keyboard.is_pressed('`'): # DEFAULT
            return default_x, default_y

def pause_or_exit():
    global paused
    global quit_program
    while True:
        if keyboard.is_pressed('alt'):
            paused = not paused
            print(f'Program {"paused" if paused else "resumed"}')
            time.sleep(0.5)
        if keyboard.is_pressed('q'):
            print('\nPROGRAM STOPPING!!!')
            quit_program = True
            

header = {
    'Disclaimer': 'Part of this code was written by AI but I have made it my own code. I know how to code but I just wanna use my imagination and NOT dig around in the library docs.',
    'creation_date': '2023-09-07 1:00 AM',
    'last_updated': '2023-09-08 9:56 PM',
    'version': '0.0.1.1',
    'purpose': 'This serves as a F**K you to the people who play "Survive and Kill the Killers in Area 51 !!!" (155382109) unfairly and abusing the raygun item',
    'defaultCoords': [1569, 90], # In order of: x, y
    'code_editor': 'Visual Studio Code'
}

defX = header["defaultCoords"][0]
defY = header["defaultCoords"][1]
pausing_key = 'alt'
quit_key = 'q'

# User interface
print(f'----- Starting reset character macro -----\nVersion {header["version"]}\n\n\n')
# Ask the user to set the pixel to detect on the Roblox window, defaults are for using power toys.
print('Setting detection area: put mouse on the pixel to delect\nPress [ESC] to SET | [ESC] to take DEFAUL\nDefault coords:', f'Xpos={defX} Ypos={defY}')
mousePOS = get_mouse_position(defX, defY)
print(f'Sucess! Your detection area has been set to Xpos={defX if mousePOS[0] == defX else mousePOS[0]} Ypos={defY if mousePOS[1] == defY else mousePOS[1]} | type = {"default" if (mousePOS[0] == defX) and mousePOS[1] == defY else "set_by_user"}\n\n')

# Define the RGB value of the red color in the health bar
death = (230, 137, 7)

# Let the user quit, and pause the program when wants to play with low-health
pause_or_exit_thread = threading.Thread(target=pause_or_exit).start()

# The rest of your code
time.sleep(2)

global paused, quit_program
quit_program, paused = False, False
while True:
    if quit_program:
        quit()
    while not paused:
        # Check the color of the pixel at (x, y)
        pixel_color = pyautogui.pixel(mousePOS[0], mousePOS[1])
        print(f'detecting health bar status, press {pausing_key} to pause and {quit_key} to exit')
        time.sleep(.25)
        # If the color is red or close to red, reset the character
        if pyautogui.pixelMatchesColor(mousePOS[0], mousePOS[1], death, tolerance=50):
            print('resetting character')
            press_da_keys(['esc', 'r', 'enter'])
            # subprocess.call("C:\Users\doe\Downloads\reset-character.ahk".replace('\\', '\\\\'), shell=True)
            time.sleep(.25)
