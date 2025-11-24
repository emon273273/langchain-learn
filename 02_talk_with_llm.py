import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())

from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_groq import ChatGroq



llmModel=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.9
    
)

#chat completion model

#template

# template=ChatPromptTemplate.from_messages([
#     ("system","You are a friendly, helpful, and concise assistant specializing in task breakdowns and motivation. Respond in a friendly, encouraging tone."),
#     ("human", "Hello, my name is {name}. Can you give me a simple three-step plan for the following task: {task}"),
    
# ])



# #response

# message=template.format_messages(name="emon",
#                                  task="learn langchain")


# response=llmModel.invoke(message)

# print(response.content,end="")


#example like user give any english sentence and response it into spanish 




example=[
    {"input":"hi","output":"hola"},
    {"input":"bye","output":"adiós"}
]



example_prompt=ChatPromptTemplate.from_messages(
    [
        ("human","{input}"),
        ("ai","{output}")
    ]
)


few_short_prompt=FewShotChatMessagePromptTemplate(
    examples=example,
   example_prompt= example_prompt,
   input_variables=["input"]
    
)


final_prompt=ChatPromptTemplate.from_messages([
    ("system","YOu are an English-spanish translator"),
    few_short_prompt,
    ("human","{input}")
])


#chains



chain=final_prompt|llmModel

res=chain.invoke({"input":"love"})

print(res.content)





