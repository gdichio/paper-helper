#%%
import openai
from src.paper import pdf2txt
from src.openaiAPI import titles
#%%
path = "/Users/gianyrox1/Library/Mobile Documents/com~apple~CloudDocs/GDD School/Stevens'24/Research/Double Slit Papers/1103.0100.pdf"

text = pdf2txt(path)
print(text)

#%%
def openaiapi(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I read academic papers and find all the section titles. You prompt me with an academic paper and I output the title names. "},
            {"role": "user", "content": f"{prompt}"}
        ],
        max_tokens = 100,
        temperature = 0
    )
    return response.choices[0]["message"]["content"]
#%%
openai.api_key = "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"

response = openaiapi(text)
print(response)

#%%

from src.paper import pdfparser
