import discord
from discord.ext import commands
import os
import random
import requests
from dotenv import load_dotenv
import aiohttp
import re
import urllib.parse

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is online and ready!")
    try:
        await bot.tree.sync()  
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.command()
async def reminder(ctx):
    reminders = [
        "Remember to pray your Salah on time!",
        "Always say Bismillah before starting any task.",
        "Be kind and generous to others, as the Prophet Muhammad ﷺ was.",
        "Seek knowledge, for it is an obligation upon every Muslim.",
        "Go memorize 'Usool Ath Thalatha",
        "Stop playing games, you lazy sloth",
        "Learn Arabic, fr.",
        "Seek knowledge the old way, not through reels and shorts",
        "Make du'a often — Allah loves it when you call upon Him.",
        "Lower your gaze, it’s a shield for your heart.",
        "Guard your tongue from backbiting.",
        "Read a few ayahs of the Qur'an daily — don’t disconnect from it.",
        "Be consistent with Dhikr, even if it’s just saying SubhanAllah.",
        "Avoid idle talk. Use your time wisely.",
        "Reflect on your intentions — are they for Allah?",
        "Do something good today, even if it’s small.",
        "Speak kindly — words can heal or harm.",
        "Pray Tahajjud, even once a week. It's special.",
        "Stay humble — pride has no place in a believer’s heart.",
        "Don’t delay repentance — death doesn’t give warnings.",
        "Visit the sick, help the needy — serve the Ummah.",
        "Give sadaqah, even if it’s just a smile.",
        "Fast voluntary fasts — like Mondays and Thursdays.",
        "Revive the Sunnah in your home and habits.",
        "Choose friends who remind you of Allah.",
        "Delete that haram app. You know the one.",
        "The dunya is temporary — focus on your akhirah.",
        "Your heart needs Qur'an more than your phone needs charging.",
        "Remember Allah in secret — it purifies your soul.",
        "Start learning the 99 Names of Allah — build that connection.",
        "Don’t chase clout — seek Allah’s pleasure instead.",
        "Use social media wisely — what you post is your legacy.",
        "Stop comparing — Allah gave you your own path.",
        "Build a habit of shukr — gratitude is a powerful weapon.",
        "Avoid music and replace it with Qur’an or Islamic reminders.",
        "Make wudu before sleeping — it’s a shield till morning.",
        "Respect your parents — even a sigh can be a sin.",
        "Be patient. Allah’s help is always near.",
        "Don’t scroll past reminders. Act on them.",
    ]
    await ctx.send(random.choice(reminders))

@bot.command()
async def quran(ctx):
    try:
        ayah_number = random.randint(1, 6236)

        response_arabic = requests.get(f"https://api.alquran.cloud/v1/ayah/{ayah_number}/ar")
        response_english = requests.get(f"https://api.alquran.cloud/v1/ayah/{ayah_number}/en.hilali")

        if response_arabic.status_code == 200 and response_english.status_code == 200:
            data_arabic = response_arabic.json()
            data_english = response_english.json()

            arabic_text = data_arabic['data']['text']
            english_translation = data_english['data']['text']
            surah_name_arabic = data_arabic['data']['surah']['name']
            surah_name_english = data_english['data']['surah']['englishName']
            surah_number = data_english['data']['surah']['number']
            ayah_number_in_surah = data_english['data']['numberInSurah']

            await ctx.send(
                f"# Random Quranic Verse\n\n"
                f"**Surah:**\n{surah_name_arabic}\n"
                f"{surah_name_english} ({surah_number}:{ayah_number_in_surah})\n\n"
                f"**Arabic:**\n{arabic_text}\n\n"
                f"**Translation (Hilali-Khan):**\n{english_translation}"
            )
        else:
            print(f"Error fetching data from API. Status codes: {response_arabic.status_code}, {response_english.status_code}")
            await ctx.send("Sorry, I couldn't fetch a verse right now. Please try again later.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        await ctx.send("Sorry, there was an error processing the verse. Please try again later.")

@bot.command()
async def about(ctx):
    about_text = (
        "**About**\n"
        "السلام عليكم ورحمة الله وبركاته\n\n"
        "This tool shares authentic Islamic reminders and random Qur'anic verses to help you stay connected to the Deen.\n\n"
        "Suggestions or feedback? Message <@1107348715867480104>\n\n"
        "جزاكم الله خيرا"
    )
    await ctx.send(about_text)


@bot.tree.command(name="reminder", description="Get a random Islamic reminder")
async def reminder_slash(interaction: discord.Interaction):
    reminders = [
        "Remember to pray your Salah on time!",
        "Always say Bismillah before starting any task.",
        "Be kind and generous to others, as the Prophet Muhammad ﷺ was.",
        "Seek knowledge, for it is an obligation upon every Muslim.",
        "Go memorize 'Usool Ath Thalatha",
        "Stop playing games, you lazy sloth",
        "Learn Arabic, fr.",
        "Seek knowledge the old way, not through reels and shorts",
        "Make du'a often — Allah loves it when you call upon Him.",
        "Lower your gaze, it’s a shield for your heart.",
        "Guard your tongue from backbiting.",
        "Read a few ayahs of the Qur'an daily — don’t disconnect from it.",
        "Be consistent with Dhikr, even if it’s just saying SubhanAllah.",
        "Avoid idle talk. Use your time wisely.",
        "Reflect on your intentions — are they for Allah?",
        "Do something good today, even if it’s small.",
        "Speak kindly — words can heal or harm.",
        "Pray Tahajjud, even once a week. It's special.",
        "Stay humble — pride has no place in a believer’s heart.",
        "Don’t delay repentance — death doesn’t give warnings.",
        "Visit the sick, help the needy — serve the Ummah.",
        "Give sadaqah, even if it’s just a smile.",
        "Fast voluntary fasts — like Mondays and Thursdays.",
        "Revive the Sunnah in your home and habits.",
        "Choose friends who remind you of Allah.",
        "Delete that haram app. You know the one.",
        "The dunya is temporary — focus on your akhirah.",
        "Your heart needs Qur'an more than your phone needs charging.",
        "Remember Allah in secret — it purifies your soul.",
        "Start learning the 99 Names of Allah — build that connection.",
        "Don’t chase clout — seek Allah’s pleasure instead.",
        "Use social media wisely — what you post is your legacy.",
        "Stop comparing — Allah gave you your own path.",
        "Build a habit of shukr — gratitude is a powerful weapon.",
        "Avoid music and replace it with Qur’an or Islamic reminders.",
        "Make wudu before sleeping — it’s a shield till morning.",
        "Respect your parents — even a sigh can be a sin.",
        "Be patient. Allah’s help is always near.",
        "Don’t scroll past reminders. Act on them.",
    ]
    await interaction.response.send_message(random.choice(reminders))


@bot.tree.command(name="quran", description="Get a random Quranic verse with translation")
async def quran_slash(interaction: discord.Interaction):
    try:
        ayah_number = random.randint(1, 6236)

        response_arabic = requests.get(f"https://api.alquran.cloud/v1/ayah/{ayah_number}/ar")
        response_english = requests.get(f"https://api.alquran.cloud/v1/ayah/{ayah_number}/en.hilali")

        if response_arabic.status_code == 200 and response_english.status_code == 200:
            data_arabic = response_arabic.json()
            data_english = response_english.json()

            arabic_text = data_arabic['data']['text']
            english_translation = data_english['data']['text']
            surah_name_arabic = data_arabic['data']['surah']['name']
            surah_name_english = data_english['data']['surah']['englishName']
            surah_number = data_english['data']['surah']['number']
            ayah_number_in_surah = data_english['data']['numberInSurah']

            await interaction.response.send_message(
                f"# Random Quranic Verse\n\n"
                f"**Surah:**\n{surah_name_arabic}\n"
                f"{surah_name_english} ({surah_number}:{ayah_number_in_surah})\n\n"
                f"**Arabic:**\n{arabic_text}\n\n"
                f"**Translation (Hilali-Khan):**\n{english_translation}"
            )
        else:
            print(f"Error fetching data from API. Status codes: {response_arabic.status_code}, {response_english.status_code}")
            await interaction.response.send_message("Sorry, I couldn't fetch a verse right now. Please try again later.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        await interaction.response.send_message("Sorry, there was an error processing the verse. Please try again later.")

@bot.tree.command(name="about", description="Learn more about the bot")
async def about_slash(interaction: discord.Interaction):
    about_text = (
        "**About**\n"
        "السلام عليكم ورحمة الله وبركاته\n\n"
        "This tool shares authentic Islamic reminders and random Qur'anic verses to help you stay connected to the Deen.\n\n"
        "Suggestions or feedback? Message <@1107348715867480104>\n\n"
        "جزاكم الله خيرا"
    )
    await interaction.response.send_message(about_text)

@bot.tree.command(name="say", description="Make the bot say whatever you want")
async def say_slash(interaction: discord.Interaction, message: str):
    allowed_users = {1107348715867480104, 752787629451247617} 

    if interaction.user.id not in allowed_users:
        await interaction.response.send_message("You are not allowed to use this command.", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True) 
    channel = interaction.channel

    webhooks = await channel.webhooks()
    webhook = None
    for wh in webhooks:
        if wh.user == bot.user:
            webhook = wh
            break

    if webhook is None:
        webhook = await channel.create_webhook(name="Ḥāris al-Qaṭīʿ")

    await webhook.send(
        content=message,
        username=bot.user.display_name,
        avatar_url=bot.user.display_avatar.url,
    )

    await interaction.followup.send("Message sent!", ephemeral=True)



@bot.tree.command(name="prayer", description="Get today's prayer times for your city")
async def prayer_slash(interaction: discord.Interaction, city: str):
    """Get prayer times for a city, auto-detecting the country."""
    try:
        async with aiohttp.ClientSession() as session:
            geocode_url = f"https://nominatim.openstreetmap.org/search?city={urllib.parse.quote(city)}&format=json"
            async with session.get(geocode_url, headers={"User-Agent": "Mozilla/5.0"}) as geo_response:
                geo_data = await geo_response.json()
                if not geo_data:
                    await interaction.response.send_message("Could not find that city. Please check the spelling.", ephemeral=True)
                    return
                country = geo_data[0].get("display_name", "").split(",")[-1].strip()
                if not country:
                    await interaction.response.send_message("Could not detect the country for that city.", ephemeral=True)
                    return

            prayer_url = f"https://api.aladhan.com/v1/timingsByCity?city={urllib.parse.quote(city)}&country={urllib.parse.quote(country)}&method=2"
            async with session.get(prayer_url) as prayer_response:
                data = await prayer_response.json()
                if data["code"] == 200:
                    timings = data["data"]["timings"]
                    date = data["data"]["date"]["readable"]
                    msg = (
                        f"# Prayer Times\n\n"
                        f"**Location:** {city.title()}, {country}\n"
                        f"**Date:** {date}\n\n"
                        f"**Fajr:** {timings['Fajr']}\n"
                        f"**Dhuhr:** {timings['Dhuhr']}\n"
                        f"**Asr:** {timings['Asr']}\n"
                        f"**Maghrib:** {timings['Maghrib']}\n"
                        f"**Isha:** {timings['Isha']}\n"
                    )
                    await interaction.response.send_message(msg)
                else:
                    await interaction.response.send_message("Could not fetch prayer times. Please check your city.", ephemeral=True)
    except Exception as e:
        print(f"Prayer times error: {e}")
        await interaction.response.send_message("Error fetching prayer times.", ephemeral=True)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    match = re.match(r"^\s*(\d{1,3}):(\d{1,3})\s*$", message.content)
    if match:
        surah = int(match.group(1))
        ayah = int(match.group(2))
        url_ar = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/ar"
        url_en = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.hilali"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url_ar) as response_ar, session.get(url_en) as response_en:
                    if response_ar.status == 200 and response_en.status == 200:
                        data_ar = await response_ar.json()
                        data_en = await response_en.json()
                        arabic_text = data_ar['data']['text']
                        english_translation = data_en['data']['text']
                        surah_name_arabic = data_ar['data']['surah']['name']
                        surah_name_english = data_en['data']['surah']['englishName']
                        surah_number = data_en['data']['surah']['number']
                        ayah_number_in_surah = data_en['data']['numberInSurah']

                        msg = (
                            f"**Surah:**\n{surah_name_arabic}\n"
                            f"{surah_name_english} ({surah_number}:{ayah_number_in_surah})\n\n"
                            f"**Arabic:**\n{arabic_text}\n\n"
                            f"**Translation (Hilali-Khan):**\n{english_translation}"
                        )
                        await message.channel.send(msg)
                    else:
                        await message.channel.send("Ayah not found.")
        except Exception as e:
            print(f"Quran search error: {e}")
            await message.channel.send("Error searching Qur'an.")

    await bot.process_commands(message)



if TOKEN:
    bot.run(TOKEN)
else:
    print("Bot token not found! Please check your .env file.")