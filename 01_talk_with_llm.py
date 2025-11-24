
#import the model 
import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
from langchain_groq import ChatGroq



##################completation model####################
#chat with the model 
llmModel=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.9
    
)

# call llm
# response=llmModel.invoke("hi")

# print(a)

#chunk wise for stream

# for chunk in llmModel.stream(
#     "Tell me fun fact about sunny leone"
# ):
#     print(chunk.content,end="")


###################chat model ###########

messages=[
    ("system","you are a computer science teacher . your task is when user tell something about computer related then try to learn simple way . if other domain type question that is not related to the computer science then not answer that question and  tell him/her to sorry you can't provide the answer because you are not expert  "),
    ("give me a c++ code to find palindome ")

]


for chunk in llmModel.stream(messages): 
    print(chunk.content,end="")


