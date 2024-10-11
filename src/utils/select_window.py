import pygetwindow as gw
import pyautogui
import time

def open_chrome_dev_tools(target_title):
    # Get a list of all open windows
    all_windows = gw.getAllWindows()
    target_window = None
    
    # Search for the Chrome window with a specific title part
    for window in all_windows:
        if "Chrome" in window.title and target_title in window.title:
            target_window = window
            break
    
    if target_window:
        # Focus on the found Chrome window
        target_window.activate()
        # Wait for the window to be active, then send F12
        time.sleep(1)
        pyautogui.press('f12')
        print("Developer Tools opened.")
    else:
        print(f"No Chrome window found with the title part '{target_title}'.")

# Example usage: specify part of the title that is unique to the desired window
# open_chrome_dev_tools("Facebook")  # Replace "Facebook" with the specific part of the title that identifies your window

def open_chrome_window(target_title):
    # Get a list of all open windows
    all_windows = gw.getAllWindows()
    target_window = None
    
    # Search for the Chrome window with a specific title part
    for window in all_windows:
        if "Chrome" in window.title and target_title in window.title:
            target_window = window
            break
    
    if target_window:
        # Focus on the found Chrome window
        target_window.activate()
        # Wait for the window to be active, then send F12
        time.sleep(1)
        print(f"Chrome window {target_window} opened.")
    else:
        print(f"No Chrome window found with the title part '{target_title}'.")

