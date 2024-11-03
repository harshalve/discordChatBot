import discord
import os
import openai

openai.api_key = os.getenv("KEY")
openai.base_url = os.getenv("BASE_URL")

token = os.getenv("TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(f'Author {self}')
        if self.user in message.mentions :
            channel = message.channel
            content = message.content.replace(f'<@{self.user.id}>', '')
            # Generate a response
            print(content)
            completion = openai.chat.completions.create(
                model="pai-001",
                messages=[
                    {"role": "user", "content": content},
                ],
            )
            messageToSend = completion.choices[0].message.content
            await channel.send(messageToSend)
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
