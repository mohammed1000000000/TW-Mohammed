# 🛡️ InstaIntelX v3.5
# Developed by: Mohammed
# GitHub: https://github.com/YOUR_USERNAME

import datetime

def verify_account():
    print("\n----------------------------")
    print("🔍 VERIFY ACCOUNT (تحليل حساب مشبوه)")
    print("----------------------------\n")

    url = input("🔗 أدخل رابط حساب إنستجرام:\n>> ").strip()
    username = url.split("/")[-1].split("?")[0].strip()

    if not username:
        print("❌ الرابط غير صالح.")
        return

    print(f"\n🔎 يتم الآن تحليل الحساب: @{username} ...\n")

    # اسم الملف
    report_name = f"report_{username}.txt"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # محتوى التقرير
    report = f"""
==========================================
🔎 تقرير فحص حساب إنستجرام
==========================================

👤 الحساب: @{username}
📅 التاريخ: {now}
⚠️ الحالة: مشتبه به
🔒 مستوى الخطورة: مرتفع

📌 تم إنشاء هذا التقرير باستخدام أداة InstaIntelX v3.5
🧠 تم تطوير الأداة بواسطة Mohammed لحماية المستخدمين.

------------------------------------------
⚠️ ملاحظات:
- قد يحتوي الحساب على محتوى مكرر أو مسروق
- النشاط غير طبيعي أو مشبوه
- يُفضل عدم التفاعل مع الحساب
------------------------------------------
    """

    # حفظ التقرير
    with open(report_name, "w") as f:
        f.write(report.strip())

    print("✅ تم إنشاء التقرير بنجاح.")
    print(f"📁 اسم الملف: {report_name}")
    print("📄 يمكنك قراءته باستخدام: nano أو cat\n")
