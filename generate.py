import openai
import re

def extract_code(input_string):
    pattern = r"```.*?\n(.*?)```"
    match = re.search(pattern, input_string, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return input_string

def messages(data):
    messages = []
    for msg in data:
        role = "user"
        if msg[0] == "!":
            role = "system"
            msg = msg[1:]
        elif msg[0] == "@":
            role = "assistant"
            msg = msg[1:]
        entry = { 
            "role": role, 
            "content": msg,
        }
        messages.append(entry)
    return messages

def ask(hist, msg):
    query = messages(hist + [msg])
    #print(query)
    r = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages = query)
    content = r.choices[0].message.content
    code = extract_code(content)
    print(code)
