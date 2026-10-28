# Telegram Library Bot

A modular Telegram bot built with aiogram designed for managing and browsing a digital book library, managing reading states via FSM, and persisting library data with SQLite.

## Key Features

* FSM Workflows: Step-by-step state management for user interaction and book selection
* Library Catalog & Database: SQLite integration for storing book records, categories, and user history
* Modular Architecture: Clean separation of command handlers, database queries, and configuration settings

## Tech Stack

* Python 3
* aiogram
* SQLite3
* python-dotenv

## Getting Started

1. Clone the repository:
   git clone https://github.com/divarusa/telegram-library-bot.git
   cd telegram-library-bot

2. Setup virtual environment and dependencies:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Configure environment variables:
   Create a .env file and add your BOT_TOKEN=your_telegram_bot_token

4. Run the bot:
   python main.py
