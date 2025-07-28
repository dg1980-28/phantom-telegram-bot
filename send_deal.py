import requests

# CONFIGURE THESE
BOT_TOKEN = "8221917763:AAGGzoTtDPmgdo4etyNkbpg-7RtzC2rq0pI"
CHANNEL_ID = "@phantommetrics"  # Must be public or bot must be admin

def send_telegram_message(title, url, price=None):
    message = f"🔥 New Deal Spotted!\n📦 Item: {title}"
    if price:
        message += f"\n💸 Price: {price}"
    message += f"\n🔗 [View Deal]({url})"

    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={{
            "chat_id": CHANNEL_ID,
            "text": message,
            "parse_mode": "Markdown"
        }}
    )
    return response.json()

# EXAMPLE
if __name__ == "__main__":
    title = "LEGO Star Wars AT-AT"
    url = "https://example.com/deal"
    price = "£42.99"
    result = send_telegram_message(title, url, price)
    print("Telegram response:", result)
