import discord
import os
from openai import OpenAI

chat = ""

ai_client = OpenAI(api_key="...")
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logges on as {self.user}')

    async def on_message(self, message):
        global chat
        chat += f"Message from {message.author}: {message.content} "
        print(f"Message from {message.author}: {message.content}")
        print(message.mentions)

        if message.author == self.user:
            return

        if self.user in message.mentions:
            channel = message.channel
            print(f"{chat}\n")

            try:
                prompt = f"{chat} \nPRANJAL_BOT : ",
                response = ai_client.responses.create(
                    model="gpt-5",
                    input=prompt
                )

                message_to_send = response.output_text

                await channel.send(message_to_send)

            except Exception as e:
                print(e)
                await channel.send("Sorry, I couldn't generate a response.")



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)
client.run('...')