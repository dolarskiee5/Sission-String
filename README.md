# Telegram Session String Generator

Tool sederhana untuk mendapatkan session string Telegram.

## Cara Pakai di VPS

```bash
# Install kebutuhan
apt update && apt upgrade
apt install python3 python3-pip git -y
pip3 install pyrogram tgcrypto
python3 -m venv venv
source venv/bin/activate

# Clone dan jalankan
git clone https://github.com/rusliC/Sission-String
cd Sission-String
python3 bot.py
```

## Catatan
- Masukkan nomor telepon dengan kode negara (+62xxx)
- Kode otp harus ( 1 2 3 4 5 6 ) menggunakan spasi
- Session string akan dikirim ke Saved Messages Telegram
- Jaga kerahasiaan session string Anda
