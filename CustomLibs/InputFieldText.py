import uiautomation as auto
import pyautogui
import asyncio
import pythoncom

class InputFieldText:
    """
    A class to interact with input fields using UI automation and display popups.
    """
    def __init__(self):
        """
        Initializes the InputFieldText class.
        """
        pythoncom.CoInitialize()                        # type: ignore
        pass

    async def show_popup(self, message):
        """
        Displays a popup with the given message.

        Args:
            message (str): The message to display in the popup.
        """
        pyautogui.alert(text=message, title='Value Pattern', button='OK')

    async def get_input_text(self, show_popup=False) -> str:
        """
        Retrieves the text from the currently focused input field and displays it in a popup.
        If the input field supports the ValuePattern, it retrieves the value.
        Otherwise, it retrieves the help text.
        
        Args:
            show_popup (bool): If True, displays the retrieved text in a popup.
        Returns:
            str: The text from the currently focused input field.
        """
        
        await asyncio.sleep(0.1)
        self.element = auto.GetFocusedControl()

        try: 
            self.msg = self.element.GetValuePattern().Value       # type: ignore
        except AttributeError as e:
            self.msg = self.element.HelpText                      # type: ignore
            print("debug1", e)
        print(self.msg)
        
        # Popup showcase
        await self.show_popup(self.msg) if show_popup else None
        
        return self.msg
    
    async def type_message(self, message):
        """
        Asynchronously types a message into the input field.
        This method attempts to set the value of the input field using the GetValuePattern.
        If an AttributeError occurs, it sets focus to the element and sends the keys one by one.
        Args:
            message (str): The message to be typed into the input field.
        Raises:
            AttributeError: If the element does not support the GetValuePattern.
        """
        
        # Try to set the value of the input field
        try:
            self.element.GetValuePattern().SetValue(self.msg + message) # type: ignore
        except AttributeError as e:
            print("debug2", e)
            self.element.SetFocus() # type: ignore
            self.element.SendKeys(message, 0.02)             # type: ignore

    def sync_test(self):
        asyncio.run(self.test())

    async def main(self):
        #await asyncio.gather()
        pass
        
    # Run the async event loop