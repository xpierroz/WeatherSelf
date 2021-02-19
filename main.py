import requests 
import json

import discord 
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix="!", self_bot=True)

api_key = "Put your API Key here"
token = "Put your Discord Token here"
city = "Paris"

@tasks.loop(seconds=60)
async def weather_status():
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').json()
    value = int(r['main']['temp']) - int(273.15)
    r = str(value)
    weather_stream = discord.Streaming(
        name="Current Paris Temperature: " + r + "°C ☁️",
        url="https://www.youtube.com/watch?v=UfEiKK-iX70"
    )
    await bot.change_presence(activity=weather_stream)
    
@bot.event 
async def on_connect():
    weather_status.start()    
    
bot.run(token, bot=False)
