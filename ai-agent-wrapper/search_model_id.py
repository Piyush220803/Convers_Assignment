from retell import Retell

client = Retell(api_key="key_aa3f852d528b7e9d451db22c1d1a")

print("Available Voices:")
print(client.voice.list())

print("Available LLMs:")
print(client.llm.list())
