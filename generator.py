import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

class Generator ():

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("Gemin api key not found")
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.5-flash"  # choose the model you want to use

    def generate ( self , question : str, context_chunks : list[str]) -> str:
        context = "\n" . join ( context_chunks)
        prompt = f"""
            Answer the question using only the context below , . 
            If the answer is not mentioned in the context, say the 'context is too narrow'    

            Context : 
            {context}

            Question : {question}
               
""" 
        response =  ""
        try:
            response = self.client.models.generate_content(model = self.model, contents=
                                                           prompt)
        except Exception as e:
            print (" Error encountered while feeding to llm :) ",e)

        return response.text.strip()