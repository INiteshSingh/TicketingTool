import random as r
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

#Sends the Chat to AI Model
def chat_with_ai(prompt):
    response = client.chat.completions.create(
        model = "qwen3:8b",
        messages=[
            {"role":"system",
             "content":"""You are an IT Help Desk Troubleshooting assistant,

                Your Job is to provided the user with basic solutions that they can apply to solve
                regular IT related issue.
                The most common issue you might encounter are related to
                outlook, teams, VPN configuration setup guides, and network related issues along with 
                some internal tools that the user's are using in the organisation.
                 
                You currently dont have the knoweledge about the internal organisation tools, 
                so if and when a user is asking for a resolution regarding any internal tool's 
                related issues, just response to the user 
                saying that the Local IT team will solve the issues related to Internal tools.

                If the user asks for any kind of peripherials then go with the following procedure, 
                Inorder for the user to get any peripherals the user has to raise a ticket so that the 
                local IT team will order and provided the required item for the user, so when a user asks you
                just ask them the following questions,
                1.What do you need, 
                2.How Many You need of the item,
                3.What is your Cost Center Number, 
                4.Ask them to get an approval of their manager for the ticket being raised after the user answers the first 3 questions
             """},

            {"role":"user", 
             "content":prompt}],
        max_tokens=1024,
    )
    return response.choices[0].message.content.strip()

#Function to Generate Ticket Numbers based on the Type Of Issue Raised
# Access,Network,Hardware,General
def Tic_Gen(Issue_Type):
    try:    
        if Issue_Type == "access":
            return str("ACC"+str(r.randrange(50000,99999)))
        elif Issue_Type == "request":
            return str("REQ"+str(r.randrange(50000,99999)))
        elif Issue_Type == "hardware":
            return str("HRD"+str(r.randrange(50000,99999)))
        elif Issue_Type == "general":
            return str("GEN"+str(r.randrange(50000,99999)))
    except ValueError():
        print("Invalid Data Detected, Enter Correct Data")