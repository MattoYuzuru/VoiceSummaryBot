import os

import dotenv
from gigachat import GigaChat


dotenv.load_dotenv()
KEY = os.getenv("GIGACHAT_API_KEY")
print(KEY)

model = GigaChat(
    credentials=KEY,
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
)

# response = model.chat("Расскажи о себе в двух словах?")
#
# print(response.choices[0].message.content)

response = model.get_models()

print(response)