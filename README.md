# Ḥāris al-Qaṭīʿ Discord Bot

A friendly Discord bot to help you stay connected to Islam with reminders, random Qur’anic verses, and prayer times—right in your server.

---

## ✨ Features

- **Islamic Reminders:**  
  Get motivational reminders to boost your faith and daily practice.

- **Random Qur’an Verses:**  
  Instantly fetch a random ayah in Arabic and English (Hilali-Khan translation).

- **Prayer Times:**  
  Get today’s prayer times for any city, with country auto-detection.

- **Ayah Lookup:**  
  Type `Surah:Ayah` (e.g., `2:255`) in chat to get that verse.

- **Admin Say:**  
  make the bot say anything via webhook.

---

## 🚀 Getting Started

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/haris-al-qati-bot.git
    cd haris-al-qati-bot
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Add your Discord bot token**  
   Create a `.env` file in the project folder:
    ```
    TOKEN=your_discord_bot_token
    ```

4. **Run the bot**
    ```sh
    python bot.py
    ```

---

## 🕹️ Usage

- **Prefix Commands:**  
  - `!reminder` — Get a random Islamic reminder  
  - `!quran` — Get a random Qur’anic verse  
  - `!about` — Learn about the bot

- **Slash Commands:**  
  - `/reminder` — Random reminder  
  - `/quran` — Random Qur’anic verse  
  - `/prayer <city>` — Prayer times for a city  
  - `/about` — About the bot  
  - `/say <message>` — (Admin only) Make the bot say something

- **Ayah Lookup:**  
  - Type `Surah:Ayah` (e.g., `36:58`) in chat to get that verse.

---

## 🔗 APIs Used

- [AlQuran Cloud API](https://alquran.cloud/api) — Qur’an text & translation
- [Aladhan API](https://aladhan.com/prayer-times-api) — Prayer times
- [OpenStreetMap Nominatim](https://nominatim.openstreetmap.org/) — City geocoding

---

## 🙋 Feedback

Suggestions or feedback? Message @NotSoAzam on Discord.
