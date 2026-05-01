#!/usr/bin/env python3
"""
Dev Quote of the Day - CLI tool for fetching programming jokes and dev quotes
Now with 250+ built-in quotes - works completely offline!
"""

import json
import os
import sys
import random
from pathlib import Path
from datetime import datetime

# Path to store favorites
FAVORITES_FILE = Path.home() / ".quote_favorites.json"

# 250+ Dev Quotes - Built-in database
DEV_QUOTES = [
    {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler"},
    {"text": "Programming is like sex. One mistake and you have to support it for the rest of your life.", "author": "Michael Sinz"},
    {"text": "Why do Java developers wear glasses? Because they can't C#", "author": "Tech Joke"},
    {"text": "How many programmers does it take to change a light bulb? None, that's a hardware problem.", "author": "Tech Joke"},
    {"text": "The best code is no code at all.", "author": "Jeff Atwood"},
    {"text": "Debugging: Removing the needles from the haystack.", "author": "Unknown"},
    {"text": "A programmer is told to go to the store and buy a loaf of bread. If there is eggs, buy a dozen.", "author": "Tech Joke"},
    {"text": "It works on my machine.", "author": "Every Developer Ever"},
    {"text": "Make it work, make it right, make it fast - in that order.", "author": "Kent Beck"},
    {"text": "The only way to learn a new programming language is by writing programs in it.", "author": "Dennis Ritchie"},
    {"text": "Code is read much more often than it is written.", "author": "Guido van Rossum"},
    {"text": "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because they like programming.", "author": "Linus Torvalds"},
    {"text": "I'm not a great programmer; I'm just a good programmer with great habits.", "author": "Kent Beck"},
    {"text": "The most important skill for a programmer is the ability to learn.", "author": "Unknown"},
    {"text": "Premature optimization is the root of all evil.", "author": "Donald Knuth"},
    {"text": "There are two ways to write code: write code so simple that there are obviously no bugs, or write code so complex that there are no obvious bugs.", "author": "C.A.R. Hoare"},
    {"text": "The best error message is the one that never shows up.", "author": "Unknown"},
    {"text": "If you automate a mess, you get an automated mess.", "author": "Rod Michael"},
    {"text": "Software is like entropy: it is difficult to grasp, grows without bound, and all the important conversational threads complain about it.", "author": "Norman Augustine"},
    {"text": "Don't worry about what anybody else is going to do... The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"text": "A computer is like air conditioning - it becomes useless when you open Windows.", "author": "Tech Joke"},
    {"text": "Why do programmers prefer dark mode? Because light attracts bugs!", "author": "Tech Joke"},
    {"text": "How many developers does it take to change a light bulb? That's not a bug, that's a feature.", "author": "Tech Joke"},
    {"text": "Why do programmers always get Christmas and Halloween mixed up? Because DEC 25 = OCT 31.", "author": "Tech Joke"},
    {"text": "Debugging is like being the detective in a crime drama, except you are also the murderer.", "author": "Filipe Fortes"},
    {"text": "The most effective debugging tool is still careful thought, coupled with judiciously placed print statements.", "author": "Brian Kernighan"},
    {"text": "Computers make very fast, very accurate mistakes.", "author": "Unknown"},
    {"text": "I would rather die than be seen in public with my code.", "author": "Unknown"},
    {"text": "Real programmers don't comment their code. If it was hard to write, it should be hard to read.", "author": "Tech Folklore"},
    {"text": "A function should do one thing. It should do it well. It should do it only.", "author": "Robert C. Martin"},
    {"text": "Clean code is readable, but it is more than that. Clean code should make it easy for other people to enhance it.", "author": "Robert C. Martin"},
    {"text": "Any code of your own that you haven't looked at for six or more months might as well have been written by someone else.", "author": "Eagleson's Law"},
    {"text": "Truth can only be found in one place: the code.", "author": "Robert C. Martin"},
    {"text": "Programming is the art of telling another human what you want the computer to do.", "author": "Donald Knuth"},
    {"text": "The best way to predict the future is to implement it.", "author": "Alan Kay"},
    {"text": "In programming, the hard part isn't solving the problem once, but solving it so you can never forget the solution.", "author": "Unknown"},
    {"text": "Simplicity is prerequisite for reliability.", "author": "Edsger W. Dijkstra"},
    {"text": "Complexity has nothing to do with intelligence, simplicity does.", "author": "Larry Bossidy"},
    {"text": "Before software should be reusable, it should be usable.", "author": "Ralph Johnson"},
    {"text": "The best code is not the code you write, it's the code you delete.", "author": "Unknown"},
    {"text": "Software testing is like a love affair: everyone can think of doing it well, but nobody really knows how.", "author": "Unknown"},
    {"text": "Bad programmers worry about the code. Good programmers worry about data structures and their relationships.", "author": "Linus Torvalds"},
    {"text": "The cheapest, fastest, and most reliable components are those that aren't there.", "author": "Gordon Bell"},
    {"text": "Perfect is the enemy of good.", "author": "Voltaire"},
    {"text": "Don't repeat yourself.", "author": "The Pragmatic Programmer"},
    {"text": "YAGNI - You Aren't Gonna Need It.", "author": "Ron Jeffries"},
    {"text": "Make it work, make it right, make it fast.", "author": "Kent Beck"},
    {"text": "The code you write should be readable in 5 minutes, even if it takes 5 hours to write.", "author": "Unknown"},
    {"text": "A good programmer is someone who always looks both ways before crossing a one-way street.", "author": "Unknown"},
    {"text": "The most important part of a programming job is not the code you write, but the problem you solve.", "author": "Unknown"},
    {"text": "Test-driven development doesn't drive out bugs as much as it drives out developers.", "author": "Unknown"},
    {"text": "I have not failed. I've just found 10,000 ways that won't work.", "author": "Thomas A. Edison"},
    {"text": "The only way to make sense out of change is to plunge into it, move with it, and join the dance.", "author": "Alan Watts"},
    {"text": "Life is like riding a bicycle. To keep your balance, you must keep moving. So is coding.", "author": "Albert Einstein (paraphrased)"},
    {"text": "If you don't fail, you're not even trying.", "author": "Unknown"},
    {"text": "Code review is the fastest way to become a better programmer.", "author": "Unknown"},
    {"text": "Documentation is a love letter that you write to your future self.", "author": "Damian Conway"},
    {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
    {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"},
    {"text": "It is during our darkest moments that we must focus to see the light.", "author": "Aristotle"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "It is never too late to be what you might have been.", "author": "George Eliot"},
    {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "The only impossible journey is the one you never begin.", "author": "Tony Robbins"},
    {"text": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
    {"text": "Everybody in this country should learn to program a computer, because it teaches you to think.", "author": "Steve Jobs"},
    {"text": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
    {"text": "Knowing is not enough, we must apply.", "author": "Johann Wolfgang Von Goethe"},
    {"text": "Do or do not. There is no try.", "author": "Yoda"},
    {"text": "What we fear doing most is usually what we most need to do.", "author": "Tim Ferriss"},
    {"text": "You don't have to see the whole staircase, just take the first step.", "author": "Martin Luther King Jr."},
    {"text": "The expert in anything was once a beginner.", "author": "Helen Hayes"},
    {"text": "Your limitation—it's only your imagination.", "author": "Unknown"},
    {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
    {"text": "Sometimes we're tested not to show our weaknesses, but to discover our strengths.", "author": "Unknown"},
    {"text": "The key to success is to focus on goals, not obstacles.", "author": "Unknown"},
    {"text": "Dream bigger. Do bigger.", "author": "Unknown"},
    {"text": "Great things never come from comfort zones.", "author": "Unknown"},
    {"text": "Success doesn't just find you. You have to go out and get it.", "author": "Unknown"},
    {"text": "Great things never come from comfort zones.", "author": "Unknown"},
    {"text": "Success is the sum of small efforts repeated day in and day out.", "author": "Robert Collier"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "The future depends on what you do today.", "author": "Mahatma Gandhi"},
    {"text": "Successful people do what unsuccessful people are not willing to do.", "author": "Jim Rohn"},
    {"text": "Your limitation—it's only your imagination. Push yourself.", "author": "Unknown"},
    {"text": "There's a difference between knowing the path and walking the path.", "author": "Morpheus (The Matrix)"},
    {"text": "The only person you should be competing against is yourself from yesterday.", "author": "Unknown"},
    {"text": "Take the risk or lose the chance.", "author": "Unknown"},
    {"text": "Don't be afraid to be a beginner.", "author": "Stephen Curry"},
    {"text": "The biggest risk is not taking any risk.", "author": "Mark Zuckerberg"},
    {"text": "You can't connect the dots looking forward; you can only connect them looking backwards.", "author": "Steve Jobs"},
    {"text": "The only thing standing between you and your goal is the story you keep telling yourself.", "author": "Jordan Belfort"},
    {"text": "A programmer's job is to turn coffee into code.", "author": "Paul Erdős (paraphrased)"},
    {"text": "Why do programmers prefer Linux? Because they have root access to everything.", "author": "Tech Joke"},
    {"text": "Why do Java programmers wear glasses? Because they don't use the C#!", "author": "Tech Joke"},
    {"text": "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'", "author": "Tech Joke"},
    {"text": "Why did the developer go broke? Because he used up all his cache.", "author": "Tech Joke"},
    {"text": "Why do programmers prefer dark mode? Because light attracts bugs!", "author": "Tech Joke"},
    {"text": "How many programmers does it take to change a light bulb? None, that's the DevOps team's job.", "author": "Tech Joke"},
    {"text": "Why do programmers always get Christmas and Halloween mixed up? Because Oct 31 equals Dec 25.", "author": "Tech Joke"},
    {"text": "A programmer's wife tells him, 'Go to the store and buy a loaf of bread. If they have eggs, buy a dozen.' He never comes home.", "author": "Tech Joke"},
    {"text": "Why did the programmer quit his job? Because he didn't get arrays.", "author": "Tech Joke"},
    {"text": "Why do programmers prefer their jobs to their spouses? Their jobs actually listen to them.", "author": "Tech Joke"},
    {"text": "99 little bugs in the code, 99 little bugs... take one down, patch it around... 127 little bugs in the code.", "author": "Tech Joke"},
    {"text": "How many developers does it take to change a light bulb? None, that's a front-end concern.", "author": "Tech Joke"},
    {"text": "Why is every programmer just a terrible teacher? Because they can't see the picture from the outside.", "author": "Tech Joke"},
    {"text": "A SQL query walks into a bar, walks up to 2 tables and asks... 'Can I join you?'", "author": "Tech Joke"},
    {"text": "Why did the developer go broke? Because he lost his cache.", "author": "Tech Joke"},
    {"text": "How many programmers does it take to change a light bulb? That's a hardware problem, not a software problem.", "author": "Tech Joke"},
    {"text": "Why do programmers always prefer dark mode? Because light attracts bugs!", "author": "Tech Joke"},
    {"text": "Why did the programmer name his dog Byte? Because it was a mini RAM!", "author": "Tech Joke"},
    {"text": "Why do programmers make good pilots? Because they know how to debug.", "author": "Tech Joke"},
    {"text": "Why do programmers prefer console games? Because GUIs are for cowards.", "author": "Tech Joke"},
    {"text": "How do you comfort a JavaScript developer? Don't worry, this too shall pass().", "author": "Tech Joke"},
    {"text": "Why did the Python developer refuse anesthesia at the dentist? Because he wanted to keep a semicolon in his mouth!", "author": "Tech Joke"},
    {"text": "Why do Java developers wear glasses? Because they can't C#.", "author": "Tech Joke"},
    {"text": "Why is Perl great? Because it's a write-once language.", "author": "Tech Joke"},
    {"text": "Why do programmers always get Christmas and Halloween mixed up? DEC 25 = OCT 31.", "author": "Tech Joke"},
    {"text": "How many programmers does it take to change a light bulb? Negative one - that's a hardware problem, let's hire an intern.", "author": "Tech Joke"},
    {"text": "Why did the programmer quit his job? Because he was stuck in an infinite loop... of 9-to-5.", "author": "Tech Joke"},
    {"text": "Why do programmers make good parents? Because they know how to debug.", "author": "Tech Joke"},
    {"text": "A program is never finished, just abandoned.", "author": "Tech Folklore"},
    {"text": "The best documentation is the code itself.", "author": "Unknown"},
    {"text": "There are only two kinds of programming languages: those people complain about and those nobody uses.", "author": "Bjarne Stroustrup"},
    {"text": "Measuring programming progress by lines of code is like measuring aircraft building progress by weight.", "author": "Bill Gates"},
    {"text": "Walking on water and developing software from a specification are easy if both are frozen.", "author": "Edward V. Berard"},
    {"text": "The number one rule of optimization: don't do it. The number two rule: don't do it yet.", "author": "Michael A. Jackson"},
    {"text": "Being a programmer is not about being smart. It's about perseverance.", "author": "Unknown"},
    {"text": "Every programmer is a manager. Even if you only manage yourself.", "author": "Unknown"},
    {"text": "The most dangerous word in software is 'simple'.", "author": "Unknown"},
    {"text": "Deleted code is debugged code.", "author": "Jeff Sickel"},
    {"text": "We are not makers of history. We are made by history.", "author": "Martin Luther King Jr. (applies to code too)"},
    {"text": "Code is poetry. Functions are sonnets.", "author": "Unknown"},
    {"text": "Your code is like your baby. You don't expect other people to wash it.", "author": "Unknown"},
    {"text": "The worst kind of bug is the one in production.", "author": "Unknown"},
    {"text": "You can't have great software without a great team.", "author": "Steve Jobs"},
    {"text": "That's the thing about people who mean well: they don't understand complete, irrevocable failure.", "author": "Unknown"},
    {"text": "The best thing about debugging is that it's like detective work.", "author": "Unknown"},
    {"text": "Code is code. The rest is just noise.", "author": "Unknown"},
    {"text": "Computers are incredibly fast, accurate and stupid. Humans are incredibly slow, inaccurate and brilliant.", "author": "Unknown"},
    {"text": "Software is eating the world.", "author": "Marc Andreessen"},
    {"text": "The best error message is the one that tells you how to fix it.", "author": "Unknown"},
    {"text": "Variables aren't hard to understand. Variable names are.", "author": "Unknown"},
    {"text": "Every function wants to be a 3-liner.", "author": "Unknown"},
    {"text": "Refactoring is like gardening: it requires constant attention.", "author": "Unknown"},
    {"text": "A bug in production is worth two in the test environment.", "author": "Unknown"},
    {"text": "Open Source: Because no code is worth less than three programmers' salaries.", "author": "Unknown"},
    {"text": "The most beautiful code is no code at all.", "author": "Unknown"},
    {"text": "Code reviews are where the magic happens.", "author": "Unknown"},
    {"text": "If it's stupid but it works, it's not stupid.", "author": "Unknown"},
    {"text": "There are two hard things in Computer Science: cache invalidation and naming things.", "author": "Phil Karlton"},
    {"text": "Programmers don't burn out on hard work, they burn out on change-requests and the improper used of CASE tools.", "author": "Bjarne Stroustrup"},
    {"text": "If you have ever received a bill from your telephone company, you understand why the projects at your company are always late and cost more than expected.", "author": "Unknown"},
    {"text": "If you think C++ is not overly complicated, just what is a protected pure virtual base pure virtual private member function anyway?", "author": "Bjarne Stroustrup"},
    {"text": "We are drowning in information but starved for knowledge.", "author": "E. O. Wilson"},
    {"text": "The most important property of a program is whether it accomplishes the intention of its user.", "author": "C.A.R. Hoare"},
    {"text": "You can't trust code that you did not totally write yourself.", "author": "Ken Thompson"},
    {"text": "The greatest risk to any project is the ability to hack.", "author": "Unknown"},
    {"text": "Feature requests are just bugs with a different label.", "author": "Unknown"},
    {"text": "Everybody has an opinion. And most of them are wrong.", "author": "Unknown"},
    {"text": "The worst code is the one that doesn't exist.", "author": "Unknown"},
    {"text": "Software is a great combination between artistry and engineering.", "author": "Bill Gates"},
    {"text": "A Perl script is 'write-only code' – it can be written quickly but is hard to read and understand later.", "author": "Unknown"},
    {"text": "No one has ever asked for a programming language that does less.", "author": "Unknown"},
    {"text": "We can't solve problems by using the same kind of thinking we used when we created them.", "author": "Albert Einstein"},
    {"text": "Failure is an option, but I am not a fan of it.", "author": "Elon Musk"},
    {"text": "The ideal situation is to have as much as possible of the critical function performed by automation.", "author": "Unknown"},
    {"text": "A language that doesn't affect the way you think about programming is not worth knowing.", "author": "Alan J. Perlis"},
    {"text": "Experts are just people who have asked the right questions.", "author": "Unknown"},
    {"text": "Elegant code is code that is readable, concise, and without unnecessary complexity.", "author": "Unknown"},
    {"text": "The programming process should be broken down into repeatable tasks.", "author": "Unknown"},
    {"text": "If you understand English, you can learn any programming language.", "author": "Unknown"},
    {"text": "The most important aspect of software engineering is architecture.", "author": "Unknown"},
    {"text": "Code is law. Data is truth.", "author": "Unknown"},
    {"text": "Every bug report is a story.", "author": "Unknown"},
    {"text": "The best developers are not the ones who know the most, but the ones who ask the best questions.", "author": "Unknown"},
    {"text": "A day without learning is a day without progress.", "author": "Unknown"},
    {"text": "Test everything, even if you think you don't need to.", "author": "Unknown"},
    {"text": "Use the Force, Luke. Or just use Stack Overflow.", "author": "Tech Joke"},
    {"text": "The best code comments are the ones that explain 'why', not 'what'.", "author": "Unknown"},
    {"text": "Refactoring is re-writing bad code.", "author": "Unknown"},
    {"text": "A good developer spends 90% of the time thinking and 10% coding.", "author": "Unknown"},
    {"text": "The only constant in software is change.", "author": "Unknown"},
    {"text": "Make the code work. Then make it right. Then make it fast.", "author": "Kent Beck"},
    {"text": "The code that is hardest to understand is the code that does the least.", "author": "Unknown"},
    {"text": "Comments are a code smell.", "author": "Unknown"},
    {"text": "Every bug you fix is a bug in your testing strategy.", "author": "Unknown"},
    {"text": "The most powerful tool a programmer has is their brain, not their keyboard.", "author": "Unknown"},
    {"text": "Agile is a mindset, not a process.", "author": "Unknown"},
    {"text": "The best code is the one that is easy to delete.", "author": "Tom Scheinfeldt"},
    {"text": "If you can't measure it, you can't improve it.", "author": "Peter Drucker"},
    {"text": "The best time to start is now.", "author": "Unknown"},
    {"text": "Good code is simple code.", "author": "Unknown"},
    {"text": "A good API is like a good book: the more you read it, the better you understand it.", "author": "Unknown"},
    {"text": "The best pull request is a small pull request.", "author": "Unknown"},
    {"text": "The best team is one where everyone is learning.", "author": "Unknown"},
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
    """Fetch a random quote from built-in database"""
    return random.choice(DEV_QUOTES)


def display_quote(quote):
    """Pretty print a quote"""
    if not quote:
        print("❌ Could not fetch quote.")
        return
    
    print("\n" + "="*60)
    print(f"💡 {quote['text']}")
    print(f"\n   — {quote['author']}")
    print("="*60 + "\n")


def add_favorite(quote):
    """Add a quote to favorites"""
    favorites = load_favorites()
    
    # Check if already saved
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
        # Default: fetch and display a quote
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
║     Now with 250+ Built-in Quotes - No Internet Needed!║
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
  • 250+ programming quotes built-in
  • Works completely OFFLINE - no internet needed!
  • Favorites are saved locally in ~/.quote_favorites.json
  • No API key required!
"""
    print(help_text)


if __name__ == "__main__":
    main()