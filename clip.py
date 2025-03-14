import pyperclip
import keyboard
import queue
import os
import time

# Get clipboard content and split into unique items
clipboard_content = pyperclip.paste().strip()  # Trim unnecessary spaces
items = list(dict.fromkeys(clipboard_content.split("\n")))  # Remove duplicates while keeping order

# Store items in a queue
que_to_clipboard = queue.Queue()

msg = ('''
📂 Math & Number Theory  
📂 Strings & Text Processing  
📂 Arrays & Lists  
📂 Loops & Iteration  
📂 Recursion & Functional Programming  
📂 Algorithms (Basic to Intermediate)  
📂 Special Cases & Edge Cases
        
COPY THE QUEUE IN THIS FORM!!!
 ''')



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def copy_que():
    global items  # Ensure we're updating items each time
    clipboard_content = pyperclip.paste().strip()  # Get fresh clipboard content
    items = list(dict.fromkeys(clipboard_content.split("\n")))  # Update items

    pyperclip.copy("")
    que_to_clipboard.queue.clear()  # Clear previous queue items

    for item in items:
        if item.strip():  # Ignore empty lines
            que_to_clipboard.put(item)

    print(clipboard_content)
    print("------------------------------------")
    print("Press ALT GR for the next clipboard")
    print("")
    # ✅ Press ALT GR only once at the start
    keyboard.wait("alt gr")  
    #print(f"✅ Clipboard: {items[0]}")  # Print first item before pressing ALT GR

    while not que_to_clipboard.empty():
        next_item = que_to_clipboard.get()
        pyperclip.copy(next_item)  # Copy next item to clipboard
        print(f"✅ Clipboard: {next_item}")

        # ✅ Only wait for ALT GR before moving to the next item
        if not que_to_clipboard.empty():
            keyboard.wait("alt gr")
    
    keyboard.wait("alt gr")
    pyperclip.copy("")
    print("🎉 Done! No more items in queue.")
    time.sleep(3)


clear_screen()
while True:
    print(msg)
    print("First COPY your list to your clipboard, then press ALT GR to start the queue")
    keyboard.wait("alt gr")
    clear_screen()
    time.sleep(0.3)
    copy_que()
    clear_screen()