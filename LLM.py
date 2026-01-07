import redis
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
GROQ_KEY = os.getenv("GROQ_KEY")



# Initialize Redis
redis_client = redis.Redis(
    host=HOST,
    port=13489,
    decode_responses=True,
    username="default",
    password=PASSWORD,
)

# Initialize LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=1,
    groq_api_key=GROQ_KEY
)

def get_chat_response(user_id, user_message):
    history_key = f"chat_history:{user_id}"

    raw_history = redis_client.lrange(history_key, 0, 19)
    formatted_history = "\n".join(reversed(raw_history))

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a Website Designer and maker ,
         you have to write the website code according to users need and also keep all code seperately ( in different files ),
         always try to make moder website design full in forntend , backend and also do other coding tasks.
        
        
        HISTORY: {old_chat}"""),
        ("user", "{message}")
    ])

    chain = prompt | llm | StrOutputParser()
    
    
    response = chain.invoke({
        "message": user_message, 
        "old_chat": formatted_history,
    })


    redis_client.lpush(history_key, f"User: {user_message} | AI: {response}")
    redis_client.ltrim(history_key, 0, 19)
    return response