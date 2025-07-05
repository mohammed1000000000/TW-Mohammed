# 🛡️ InstaIntelX v3.5
# Developed by: Mohammed
# GitHub: https://github.com/YOUR_USERNAME

from modules.girl_protect import girl_protection
from modules.analyzer import verify_account

def main():
    print("==============================================")
    print("🛡️ InstaIntelX v3.5 - Instagram Risk Analyzer")
    print("==============================================\n")
    print("[1] 👩 Girl Protection")
    print("[2] 🔍 Verify Suspicious Account\n")

    choice = input("📎 Enter your choice: ").strip()

    if choice == "1":
        girl_protection()
    elif choice == "2":
        verify_account()
    else:
        print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
