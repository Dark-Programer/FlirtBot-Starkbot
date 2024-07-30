# Bot Name: v1_404_Starkbot

import telegram.ext
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

with open("Projects/Telegram Bot/token.txt", 'r') as f:
    token = f.read()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi there! 😘 What's cooking, good looking?")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Need to chat? 📞 You can contact me anytime, darling! 😘")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    🌟 Here's how I can assist you, gorgeous:
    /start -> A warm welcome just for you!
    /help -> All the help you need, my dear.
    /contact -> Get in touch with me, lovely!
    /about -> Learn more about me, your charming bot.
    /funfact -> Get a fun fact to brighten your day! 😉
    /pickup -> Need a flirty line? I've got you covered! 💘
    /quote -> Get an inspiring quote to uplift your spirits! 🌟
    """)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm v1_404_Starkbot, your charming assistant bot! 🤖✨ Always here to make your day brighter!")


async def funfact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fun_facts = [
        "Did you know? Honey never spoils. You could feasibly eat 3000-year-old honey. 🍯",
        "Bananas are berries, but strawberries aren't! 🍌🍓",
        "Octopuses have three hearts! 💓💓💓",
        "A group of flamingos is called a 'flamboyance.' 🌸",
        "There's a species of jellyfish that is immortal. 🌊",
        "A single strand of spaghetti is called a 'spaghetto.' 🍝",
        "A group of cats is called a 'clowder.' 🐱",
        "The Eiffel Tower can be 15 cm taller during the summer. 🌞",
        "Honeybees can recognize human faces. 🐝",
        "A day on Venus is longer than a year on Venus. 🌌",
        "Wombat poop is cube-shaped. 🐾",
        "Koalas have fingerprints that are almost identical to human fingerprints. 🐨",
        "Sea otters hold hands while sleeping to avoid drifting apart. 🦦",
        "A snail can sleep for three years. 🐌",
        "The shortest war in history lasted 38 to 45 minutes. ⏳",
        "Cows have best friends and get stressed when they are separated. 🐄",
        "Polar bear skin is black, and their fur is actually transparent. 🐻‍❄️",
        "Turtles can breathe through their butts. 🐢",
        "An apple, potato, and onion all taste the same if you eat them with your nose plugged. 🍎🥔🧅",
        "A crocodile cannot stick its tongue out. 🐊",
        "There are more stars in the universe than grains of sand on all the world's beaches. 🌠",
        "A blue whale's heart is the size of a small car. 🐋",
        "Humans share 60% of their DNA with bananas. 🍌",
        "It's impossible to hum while holding your nose. Try it! 🎶",
        "A bolt of lightning contains enough energy to toast 100,000 slices of bread. ⚡🍞",
        "Bubble wrap was originally intended to be wallpaper. 🛋️",
        "Dragonflies have a lifespan of only a few months. 🐉",
        "The inventor of the Pringles can is now buried in one. 🥔",
        "Humans and giraffes have the same number of neck vertebrae. 🦒"
    ]

    await update.message.reply_text(random.choice(fun_facts))


async def pickup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pickup_lines = [
        "Are you a magician? Because whenever I look at you, everyone else disappears. 🪄",
        "Do you have a map? I keep getting lost in your eyes. 🗺️",
        "Do you have a name, or can I call you mine? 😏",
        "Are you a time traveler? Because I see you in my future. ⏳",
        "Do you have a Band-Aid? Because I just scraped my knee falling for you. 🩹",
        "If you were a vegetable, you'd be a cute-cumber. 🥒",
        "Do you have a pencil? Because I want to erase your past and write our future. ✏️",
        "Is your name Google? Because you have everything I've been searching for. 🔍",
        "Are you French? Because Eiffel for you. 🗼",
        "Do you believe in love at first sight, or should I walk by again? 🚶",
        "Are you a campfire? Because you bring warmth to my heart. 🔥",
        "Do you have a sunburn, or are you always this hot? ☀️",
        "If you were a triangle, you'd be acute one. 🔺",
        "Is your name Wi-Fi? Because I'm feeling a connection. 📶",
        "Do you have a mirror in your pocket? Because I can see myself in your pants. 👖",
        "Are you a parking ticket? Because you've got 'FINE' written all over you. 🚗",
        "Is your dad an artist? Because you're a masterpiece. 🎨",
        "Do you have a compass? Because I keep getting lost in your eyes. 🧭",
        "Is your name Chapstick? Because you’re da balm. 💄",
        "Are you a keyboard? Because you're my type. ⌨️",
        "Do you have a name, or can I call you mine? 😏",
        "If beauty were a crime, you'd be serving a life sentence. 👩‍⚖️",
        "Are you a snowflake? Because I've fallen for you. ❄️",
        "Do you like Star Wars? Because Yoda one for me. 🌌",
        "Are you an alien? Because you’ve just abducted my heart. 👽"
    ]

    await update.message.reply_text(random.choice(pickup_lines))


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "The best way to predict the future is to invent it. – Alan Kay",
        "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
        "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "The purpose of our lives is to be happy. – Dalai Lama"
    ]
    await update.message.reply_text(random.choice(quotes))


# Use ApplicationBuilder instead of Updater
application = ApplicationBuilder().token(token).build()

# Add handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("contact", contact))
application.add_handler(CommandHandler("help", help))
application.add_handler(CommandHandler("about", about))
application.add_handler(CommandHandler("funfact", funfact))
application.add_handler(CommandHandler("pickup", pickup))
application.add_handler(CommandHandler("quote", quote))

# Start the bot
application.run_polling()
