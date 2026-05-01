#!/usr/bin/env python3
"""
Dev Quote of the Day - CLI tool for fetching programming jokes and dev quotes
"""

import json
import os
import sys
import requests
from pathlib import Path
from datetime import datetime

# Path to store favorites
FAVORITES_FILE = Path.home() / ".quote_favorites.json"

# API endpoints for quotes
QUOTE_APIS = [
    "https://api.quotable.io/random",
    "https://programming-quotes-api.herokuapp.com/random",
]

def load_favorites():
    """Load favorites from local JSON file"""
    if FAVORITES_FILE.exists():
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    return {"quotes": []}

def save_favorites(data):
    """Save favorites to local JSON file"""
    with open(FAVORITES_FILE, "w") as f:
        json.dump(data, f, indent=2)

def fetch_quote():
    """Fetch a random quote from API"""
    for api in QUOTE_APIS:
        try:
            response = requests.get(api, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            if "content" in data:
                return {
                    "text": data.get("content"),
                    "author": data.get("author", "Unknown"),
                }
            elif "en" in data:
                return {
                    "text": data.get("en"),
                    "author": data.get("a", "Unknown"),
                }
        except (requests.RequestException, ValueError):
            continue
    
    return None

def display_quote(quote):
    """Pretty print a quote"""
    if not quote:
        print("❌ Could not fetch quote. Check your internet connection.")
        return
    
    print("\n" + "="*60)
    print(f"💡 {quote['text']}")
    print(f"\n   — {quote['author']}")
    print("="*60 + "\n")

def add_favorite(quote):
    """Add a quote to favorites"""
    favorites = load_favorites()
    
    if any(q["text"] == quote["text"] for q in favorites["quotes"]):
        print("✅ Already in favorites!")
        return
    
    favorites["quotes"].append({
        **quote,
        "saved_at": datetime.now().isoformat()
    })
    save_favorites(favorites)
    print("⭐ Added to favorites!")

def show_favorites():
    """Display all saved favorites"""
    favorites = load_favorites()
    
    if not favorites["quotes"]:
        print("📝 No favorites saved yet!")
        return
    
    print(f"\n📚 Your Favorite Quotes ({len(favorites['quotes'])}):\n")
    for idx, quote in enumerate(favorites["quotes"], 1):
        print(f"{idx}. {quote['text']}")
        print(f"   — {quote['author']}\n")

def remove_favorite(index):
    """Remove a favorite by index"""
    favorites = load_favorites()
    
    if index < 1 or index > len(favorites["quotes"]):
        print("❌ Invalid index!")
        return
    
    removed = favorites["quotes"].pop(index - 1)
    save_favorites(favorites)
    print(f"🗑️  Removed: {removed['text'][:50]}...")

def main():
    """Main CLI handler"""
    if len(sys.argv) < 2:
        quote = fetch_quote()
        display_quote(quote)
        
        if quote:
            save = input("💾 Save to favorites? (y/n): ").lower()
            if save == "y":
                add_favorite(quote)
    else:
        command = sys.argv[1].lower()
        
        if command == "quote":
            quote = fetch_quote()
            display_quote(quote)
            if quote:
                save = input("💾 Save to favorites? (y/n): ").lower()
                if save == "y":
                    add_favorite(quote)
        
        elif command == "favorites":
            show_favorites()
        
        elif command == "save":
            quote = fetch_quote()
            display_quote(quote)
            if quote:
                add_favorite(quote)
        
        elif command == "remove":
            show_favorites()
            if load_favorites()["quotes"]:
                try:
                    idx = int(input("Enter quote number to remove: "))
                    remove_favorite(idx)
                except ValueError:
                    print("❌ Please enter a valid number!")
        
        elif command == "clear":
            confirm = input("⚠️  Clear all favorites? (yes/no): ")
            if confirm == "yes":
                save_favorites({"quotes": []})
                print("✅ All favorites cleared!")
        
        elif command in ["-h", "--help", "help"]:
            print_help()
        
        else:
            print(f"❌ Unknown command: {command}")
            print_help()

def print_help():
    """Display help text"""
    help_text = """
╔════════════════════════════════════════════════════════╗
║     Dev Quote of the Day - CLI Tool                    ║
╚════════════════════════════════════════════════════════╝

USAGE:
  quote                   Get and display a random quote
  quote quote             Same as above
  quote favorites         Show all saved favorites
  quote save              Fetch and save a quote directly
  quote remove            Remove a quote from favorites
  quote clear             Clear all favorites
  quote help              Show this help message

EXAMPLES:
  $ quote
  $ quote favorites
  $ quote save
  $ quote clear

NOTES:
  • Favorites are saved locally in ~/.quote_favorites.json
  • Works offline to display saved quotes
  • No API key needed!
"""
    print(help_text)

if __name__ == "__main__":
    main()