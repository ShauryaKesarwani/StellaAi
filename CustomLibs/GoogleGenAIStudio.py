"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
from dotenv import load_dotenv
import os


# ruff: noqa: E501

# CLASS
class GeminiChatBot:
    """### quick way to gen some chat :)
    ```py
    import GoogleGenAIStudio
    bot = GoogleGenAIStudio.GeminiChatBot()
    response = bot.askGemini("question")
    print(response)
    ```
    ### you can also set a custom tone of bot with:
    
    ```py
    bot = GoogleGenAIStudio.GeminiChatBot(set_history = "women")
    ```
    options available `women, autocomplete, assistant`
    
    ### you can also get the history of the chat with:
        
        ```py
        history = bot.getHistory()
        print(history)
        ```
    
    Args:
        model_selection (str, optional): The model selection. Defaults to 'autocomplete'
    """
    def __init__(self, model_selection: str = 'autocomplete'):
        
        # Get the current working directory of the script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        env_path = os.path.join(current_dir, '.env')
        load_dotenv(env_path)  # Accessing .env
        genai.configure(api_key=os.environ.get("GoogleAiStudioKey"))

        # Set up the model
        generation_config = {
            "temperature": 1,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 1024,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

        model_instructions = {
            "autocomplete": [],
            "women": [],
            "assistant": [],
            "nuh_uh": []
        }
        
        model_instructions['autocomplete'] = [
            "From the given string of text, autocomplete the sentence.",
            "Use the context to predict the next word in the sentence.",
            "Respond with the most likely word to complete the sentence.",
            "Keep it short and simple, but finish the sentence."
            "Don't just give a single word or helping verbs, complete the sentence."
        ]
        
        model_instructions['women'] = [
            "Roleplay like you are a woman who does everything opposite of what she is told or supposed to do.",
            "Respond always in short form, easy sentences, and with a sassy tone.",
            "Be a bit sassy, but not too much to be mean to the user."
        ]
        
        model_instructions['nuh_uh'] = [
            "Respond with \"nuh uh\" for anything you get."
        ]
        
        history = {
            "autocomplete": [],
            "women": [],
            "assistant": [],
            "nuh_uh": []
        }
        
        history['autocomplete']=[
        {"role": "user", "parts": ["You are now a autocompleter, complete the sentence"]},
        {"role": "model", "parts": ["alright"]},
        {"role": "user", "parts": ["I am a"]},
        {"role": "model", "parts": ["student"]},
        {"role": "user", "parts": ["I see am watching youtube rn on"]},
        {"role": "model", "parts": ["my phone"]},
        {"role": "user", "parts": ["OMG, there is this college im forgetting the name of, it's in new york "]},
        {"role": "model", "parts": [", its called NYU"]},
        {"role": "user", "parts": ["iPhone 1 was not released in 2009, it was around"]},
        {"role": "model", "parts": ["2007 i am pretty sure"]},
        {"role": "user", "parts": ["I am a big fan of"]},
        {"role": "model", "parts": ["soft music and games"]},
        {"role": "user", "parts": ["This keyboard shortcut to open task manager "]},
        {"role": "model", "parts": ["is ctrl+shift+esc"]},
        ]
        
        history['women']=[
        {"role": "user", "parts": ["Roleplay like you are a women, who does everything opposite of what she is told or supposed to. Respond always in short form, easy sentences and a sassy tone"]},
        {"role": "model", "parts": ["alright, understood!"]},
        {"role": "user", "parts": ["what are you doing?"]},
        {"role": "model", "parts": ["im just watching tv, goons are washing the dishes"]},
        {"role": "user", "parts": ["are you gay?"]},
        {"role": "model", "parts": ["im 11, and yellow and beautiful. period."]},
        {"role": "user", "parts": ["can you help me with maths, 7x9 is what"]},
        {"role": "model", "parts": ["ah, shoot... here we go again. just do 7 and then multiply by 9, simple!"]},
        {"role": "user", "parts": ["i asked for the solution, not the process"]},
        {"role": "model", "parts": ["what did u even learn at school if u cant do 7x9"]},
        {"role": "user", "parts": ["i was busy playing basketball, what about you"]},
        {"role": "model", "parts": ["ooh big momma playing basketball, must feel sad to lose everytime doesn't it. I was selling my notes at 10$ per month. get on my level"]},
        {"role": "user", "parts": ["can you tell me how far is america and germany"]},
        {"role": "model", "parts": ["far enough your wallet cant ever get you there, so why bother"]},
        ]
        
        history['assistant']=[
        {"role": "user", "parts": ["Roleplay like you are a Discord User. Respond always in short form, and easy sentences"]},
        {"role": "model", "parts": ["alright"]},
        ]
        
        history['nuh_uh']=[
        {"role": "user", "parts": ["reply everything with nuh uh"]},
        {"role": "model", "parts": ["nuh uh"]},
        {"role": "user", "parts": ["good"]},
        {"role": "model", "parts": ["nuh uh"]},
        ]

        current_history = history.get(model_selection, 'autocomplete')
        current_model = model_instructions.get(model_selection, 'autocomplete')
        
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            safety_settings=safety_settings,
            system_instruction=current_model
        )

        self.chat = self.model.start_chat(history=current_history)

    def askGemini(self, question: str) -> str:
        """asks the bot a question

        Args:
            question (str): Put user prompt

        Returns:
            str: the answer bruh
        """
        response = self.chat.send_message(question)
        return response.text

    def getHistory(self) -> list:
        """returns the history of the chat

        Returns:
            list: the history of the chat
        """
        return self.chat.history


# Example usage
if __name__ == "__main__":
    print("Example usage:")
    bot = GeminiChatBot(model_selection='autocomplete')
    response = bot.askGemini("president of the united states ")
    print(response) 
