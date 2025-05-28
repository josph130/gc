from datetime import datetime
import os

# Dosya üretimi
#file_name = f"output_{datetime.now().strftime('%Y%m%d')}.txt"
file_name = f"file.txt"
file_path = f"outputs/{file_name}"  # outputs klasörüne kaydedeceğiz
os.makedirs("outputs", exist_ok=True)  # Klasörü oluştur (varsa hata verme)

with open(file_path, 'w') as f:
    f.write(f"Bu dosya {datetime.now()} tarihinde GitHub Actions tarafından üretildi.")

print(f"{file_name} üretildi.")
