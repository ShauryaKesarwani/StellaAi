# Description: This is the main file that will be used to run the program.
# Py version 3.10.5
# flake8: noqa E501
# ruff : noqa: E501

# My Libraries
from CustomLibs.InputFieldText import InputFieldText
import CustomLibs.GoogleGenAIStudio as GoogleGenAIStudio
# External Libraries
import asyncio
from ahk import AHK
import pythoncom

ift = InputFieldText()
aibot = GoogleGenAIStudio.GeminiChatBot(model_selection='discord')
ahk = AHK()

async def autocomplete():
    pythoncom.CoInitialize()
    text = await ift.get_input_text()
    bot = GoogleGenAIStudio.GeminiChatBot()
    response = bot.askGemini(text)
    print(response)
    await ift.type_message(response)

def stop_ahk_block():
    print("Stopping AHK block")
    global stop
    stop = True
    ahk.stop_hotkeys()
    
def sync_autocomplete():
    asyncio.run(autocomplete())

async def ahk_hotkey_task():
    ahk.add_hotkey("^t", callback=sync_autocomplete)
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