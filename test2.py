import uiautomation as auto
import pyautogui
from ahk import AHK
import asyncio
import pythoncom

# ahk hotkey to trigger test() function
ahk = AHK()

async def show_popup(message):
    pyautogui.alert(text=message, title='Value Pattern', button='OK')

async def test():
    pythoncom.CoInitialize()                        # type: ignore
    await asyncio.sleep(1)
    element = auto.GetFocusedControl()
    #element.SendKeys("lol this is great", 0.02, charMode=False)

    try: 
        msg = element.GetValuePattern().Value       # type: ignore
    except AttributeError as e:
        msg = element.HelpText                      # type: ignore
        print("1", e)
    print(msg)
    await show_popup(msg)
    
    try:
        element.GetValuePattern().SetValue('Hello') # type: ignore
    except AttributeError as e:
        print(e)
        element.SetFocus() # type: ignore
        element.SendKeys("Hello", 0.02)             # type: ignore

def sync_test():
    asyncio.run(test())

def stop_ahk_block():
    print("Stopping AHK block")
    global stop
    stop = True
    ahk.stop_hotkeys()


async def ahk_hotkey_task():
    ahk.add_hotkey("^t", callback=sync_test)
    ahk.add_hotkey("^c", callback=stop_ahk_block)
    
    ahk.start_hotkeys()
    while stop is False:
        await asyncio.sleep(1)  # Simulates `block_forever()` but non-blocking

async def main():
    global stop
    stop = False
    await asyncio.gather(
        ahk_hotkey_task(),
    )
    
# Run the async event loop
asyncio.run(main())