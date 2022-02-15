from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}
Bot For help You to Create Session.
[➼](https://telegra.ph/file/1e994ca7282f6190b727d.jpg) So What U Waiting For Generat STRING Session
───────────────────────

If you don't trust this bot, 
1) stop reading this message
2) delete this chat
───────────────────────
Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: [Starz bots!](https://t.me/starz_Bots)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("💟 Start Generating Session 💟", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🎉 Start Generating Session 🎉", callback_data="generate")],
        [InlineKeyboardButton("💕 Bot Status and More Bots 💕", url="https://t.me/starz_bots/2")],
        [
            InlineKeyboardButton("How to Use 🤭❔", callback_data="help"),
            InlineKeyboardButton("😏 About 😏", callback_data="about")
        ],
        [InlineKeyboardButton("🥱 More Amazing bots 🥱", url="https://t.me/Starz_Bots")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to Manage group and generate pyrogram and telethon string session by @TeamDeeCode

Owner : [Click Here](https:t.me/rockstar_xdd)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Starz_bots
    """
