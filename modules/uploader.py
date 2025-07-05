# 🛡️ InstaIntelX v3.5
# Developed by: Mohammed
# GitHub: https://github.com/YOUR_USERNAME

import requests
import os

def upload_report(file_path):
    filename = os.path.basename(file_path)
    try:
        with open(file_path, 'rb') as f:
            print("⏳ Uploading report...")
            response = requests.put(f'https://transfer.sh/{filename}', data=f)
        
        if response.status_code == 200:
            print("✅ Report uploaded successfully.")
            return response.text.strip()
        else:
            print("❌ Upload failed:", response.status_code)
            return None
    except Exception as e:
        print("⚠️ Error while uploading:", e)
        return None
