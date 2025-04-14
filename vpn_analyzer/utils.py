import requests

def send_discord_alert(webhook_url, message):
    if not webhook_url:
        print("⚠️ No Discord webhook URL provided.")
        return

    data = {
        "content": message
    }

    try:
        res = requests.post(webhook_url, json=data)
        if res.status_code == 204:
            print("✅ Discord alert sent.")
        else:
            print(f"⚠️ Failed to send Discord alert. Status code: {res.status_code}")
    except Exception as e:
        print(f"❌ Exception during Discord alert: {e}")