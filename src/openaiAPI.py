#%%

import openai

openai.api_key = "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"


def titles(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I read academic papers and find all the section titles. You prompt me with an academic paper and I output the title names. "},
            {"role": "user", "content": f"{prompt}"},
        ]
    )
    return response.choices[0]["message"]["content"]

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
