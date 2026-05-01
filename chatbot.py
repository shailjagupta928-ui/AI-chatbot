from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatMistralAI(model="mistral-small-2506",temperature=0.7)

print("choose your ai mode")
print("press1 for funny chatbot")
print("press2 for angry chatbot")
print("press3 for sad chatbot")

choice = int(input("tell your response:- "))p
if choice == 1:
    mode = "you are a funny ai chatbot"
elif choice == 2:
    mode = "you are an angry ai chatbot"  
elif choice == 3:   
     mode = "you are a sad ai chatbot"
messages = [
    SystemMessage(content=mode)
    

]
print("-------------welcome type 0 to exit------------------")
while True:
    
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))   
    messages.append( prompt)
    if prompt == "0":
        
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("bot: ",response.content)

    print(messages)