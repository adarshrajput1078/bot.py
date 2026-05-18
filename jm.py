import telebot
import os
import json

# 🎫 Aapka Telegram Bot Token
BOT_TOKEN = '8928404549:AAEIDWFYDQ76v388cbUB42xjtgepejWLqYE'  
bot = telebot.TeleBot(BOT_TOKEN)

# 👑 Aapki Asli Admin Numeric ID
ADMIN_ID = 8663479853  

# Data save karne ke liye file ka naam
USERS_FILE = 'users.json'

# --- 💾 USERS KO SAVE KARNE KA SYSTEM ---
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            try:
                return set(json.load(f))
            except json.JSONDecodeError:
                return set()
    return set()

def save_user(user_id):
    users = load_users()
    if user_id not in users:
        users.add(user_id)
        with open(USERS_FILE, 'w') as f:
            json.dump(list(users), f)
# ----------------------------------------

# 🔄 RASTA 1: JAB KOI NAYA BANDA CHANNEL JOIN REQUEST BHEJEGA (Osko Naya Message + Voice jayega)
@bot.chat_join_request_handler()
def handle_join_request(message):
    user_id = message.from_user.id
    save_user(user_id) 
    print(f"💾 Naya user (Join Request) save hua: {user_id}")
    
    # Aapka Naya Exact Message
    time_text = """🤝🤝LIVE PREDICTION TIME ✍️

VC TIME 10:00 AM 🤩🌟

VC TIME 12:00 PM 🤩💻

VC TIME 02:00 PM 🤩🌟

VC TIME 04:00 PM 🤩🌟

VC TIME 09:00 PM 🤩🌟
🤩🤩🔗
http://www.sikkimgg.vip/#/register?invitationCode=481415207260

🌟New platform 😃🔗
https://13lwin3.com/register?inviteCode=XDPAC8N&from=web

Support ✍️ @Ns_Rocky"""

    try:
        # Pehle text message bhejega
        bot.send_message(user_id, time_text, disable_web_page_preview=True)
        print(f"✅ Text message sent to Join Request: {user_id}")
        
        # Phir voice note bhejega
        voice_file_path = 'voice.ogg'
        if os.path.exists(voice_file_path):
            with open(voice_file_path, 'rb') as voice:
                bot.send_voice(user_id, voice)
            print(f"🎙️ Voice note sent to Join Request: {user_id}")
        else:
            print(f"⚠️ Warning: '{voice_file_path}' file nahi mili!")
            
    except Exception as e:
        print(f"❌ Error aayi Join Request me: {e}")


# 🔄 RASTA 2: JAB CHANNEL WALE MEMBERS BOT KO /start KARENGE (Data Collect + Thanks)
@bot.message_handler(commands=['start'])
def handle_start_command(message):
    user_id = message.from_user.id
    save_user(user_id) 
    print(f"💾 Purana member (Start Button) data collect hua: {user_id}")
    
    thanks_text = "✨ <b>Thanks! System mein aapka data successfully register kar liya hai.</b> 👍"
    
    try:
        bot.send_message(user_id, thanks_text, parse_mode="HTML")
    except Exception as e:
        print(f"❌ Error aayi Start command me: {e}")


# 📢 BROADCAST FEATURE
@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ Aapke paas ye command use karne ki permission nahi hai!")
        return
    
    text_to_send = message.text.replace('/broadcast', '').strip()
    
    if not text_to_send:
        bot.reply_to(message, "⚠️ Bhai, message bhi toh likho!\n\n*Aise use karo:*\n`/broadcast Aaj ki VIP prediction ready hai!`")
        return

    users = load_users()
    if not users:
        bot.reply_to(message, "⚠️ Abhi tak koi user database mein nahi hai.")
        return

    bot.reply_to(message, f"🚀 Broadcast start ho gaya! Total {len(users)} users ko bhej raha hoon... ⏳")

    success = 0
    failed = 0

    for uid in users:
        try:
            bot.send_message(uid, text_to_send)
            success += 1
        except Exception as e:
            failed += 1
    
    bot.reply_to(message, f"✅ **Broadcast Complete!**\n\n🎯 Successful: {success}\n❌ Failed (Blocked): {failed}")

print("🚀 Bot is running... Naya Message, Voice aur Broadcast ekdum ready hai! 🔥")
bot.infinity_polling()
                
