# 🛡️ InstaIntelX v3.5
# Developed by: Mohammed
# GitHub: https://github.com/YOUR_USERNAME

import webbrowser
from modules.telegram_alert import send_telegram_alert
from modules.analyzer import verify_account

def girl_protection():
    print("====================================================")
    print("🔒 Girl Protection Mode - لحماية الفتيات من الابتزاز")
    print("====================================================")
    print("⚠️ هذا الوضع يتطلب رمز حماية خاص.")

    password = input("💬 أدخلي كلمة السر:\n\n>> ").strip()

    if password != "mypass@2025":
        print("\n❌ كلمة السر غير صحيحة.")
        return

    print("\n✅ تم التحقق.")

    phone = input("📱 من فضلك أدخلي رقم هاتفك للتواصل والحماية:\n>> ").strip()
    print("\n✅ Done. Verified.")
    print("📞 Contact the programmer for personal help...")

    send_telegram_alert(phone=phone)

    whatsapp_link = "https://wa.me/201120946946?text=اريد طلب المساعدة، تم دخولي من حماية فتاة في InstaIntelX."
    webbrowser.open(whatsapp_link)

    verify_account()
