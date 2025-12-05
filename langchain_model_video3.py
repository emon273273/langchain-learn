from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

from langchain_core.messages import HumanMessage, SystemMessage

from langchain_google_genai import ChatGoogleGenerativeAI


#make chat model using groq

# llm =ChatGroq(model="llama-3.3-70b-versatile",
#               temperature=0.7)


# #define message

message=[
    SystemMessage(content="you are a programmer "),
    HumanMessage(content="give me palindome example in rust  ")
]


# response=llm.invoke(message)

# print(response.content)


#make the chat model using gemini


#----------geminin------------------

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

response=llm.invoke(message)

print(response.content)


