import replicate
from dotenv import load_dotenv

load_dotenv()

prompt = "Mevsimler nasıl oluşur?"
system_prompt = "Sen yardımsever bir asistansın."

#Llama 2 70 B Chat

AI_Response = replicate.run(
    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input = {
        "temperature":0.5,
        "max_new_tokens": 256,
        "system_prompt": system_prompt,
        "prompt": prompt,
        "debug": False
    }
)

AI_Response = "".join(AI_Response)

print(AI_Response)
print("*"*100)

AI_Response = replicate.run(
    "mistralai/mixtral-8x7b-instruct-v0.1:7b3212fbaf88310cfef07a061ce94224e82efc8403c26fc67e8f6c065de51f21",
        input = {
        "temperature":0.7,
        "max_new_tokens": 300,
        "prompt": prompt,
        "debug": False
    }

)

AI_Response = "".join(AI_Response)

print(AI_Response)
