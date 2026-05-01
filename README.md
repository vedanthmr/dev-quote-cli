# Dev Quote of the Day 💡

A lightweight CLI tool to fetch inspiring programming quotes and dev jokes. Save your favorites locally and access them offline!

## Features ✨

- 🎲 Fetch random programming quotes and dev humor
- ⭐ Save favorite quotes locally in JSON format
- 📚 View all saved quotes anytime
- 🗑️ Remove specific quotes or clear all favorites
- 🌐 Works offline with saved quotes
- 💻 Simple, easy-to-use command-line interface
- 🚀 No API key required

## Installation

### Option 1: Install from PyPI (Recommended)
```bash
pip install dev-quote-cli
```

Then use:
```bash
quote
```

### Option 2: Install from source
```bash
git clone https://github.com/vedanthmr/dev-quote-cli.git
cd dev-quote-cli
pip install -e .
```

### Option 3: Run directly (no installation)
```bash
python quote_cli.py
```

## Usage

```bash
# Get a random quote
quote

# View all saved quotes
quote favorites

# Fetch and automatically save a quote
quote save

# Remove a specific quote from favorites
quote remove

# Clear all favorites
quote clear

# Show help
quote help
```

## How It Works

1. **Fetches quotes** from free APIs (Quotable.io and Programming Quotes API)
2. **Stores favorites** in `~/.quote_favorites.json` on your computer
3. **Works offline** — display saved quotes without internet
4. **No authentication** — no API keys needed!

## Example