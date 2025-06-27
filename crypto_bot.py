# crypto_bot.py

print("👋 Hey, I’m CryptoBuddy — your chill crypto sidekick!")
print("Ask about trending coins, sustainability, or profitability! Type 'exit' to quit.\n")

crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3/10},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6/10},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8/10}
}

while True:
    user_query = input("You: ").lower()
    if user_query == "exit":
        print("CryptoBuddy: Catch you later! 🚀 DYOR always!")
        break
    elif "sustainable" in user_query:
        best = max(crypto_db, key=lambda c: crypto_db[c]["sustainability_score"])
        print(f"CryptoBuddy: 🌱 Try {best}! Highest sustainability score.")
    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"CryptoBuddy: 📈 Trending up: {', '.join(trending)}")
    elif "profitable" in user_query or "growth" in user_query:
        profitable = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
        if profitable:
            print(f"CryptoBuddy: 💸 Long-term profit pick: {', '.join(profitable)}")
        else:
            print("CryptoBuddy: 🤔 No high cap coins rising now.")
    else:
        print("CryptoBuddy: Hmm... Ask about trending, sustainable, or profitable coins.")

print("\n⚠️ This is not financial advice. Always research before investing.")
