# 🦅 SPY WIFI PASS
> **Universal WiFi Credential Recovery & Auditing Framework**

![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20Termux-red.svg)
![Brand](https://img.shields.io/badge/Brand-SPY--E%20%26%20123Tool-blue.svg)

**Tool penetrasi dan pemulihan kredensial WiFi yang bekerja secara lintas platform. Tool ini mengekstraksi seluruh SSID dan Password yang tersimpan di dalam sistem target dalam hitungan detik.**

### 🔥 Features
- **Auto-OS Detection:** Mendeteksi otomatis apakah user menggunakan Windows, Linux, atau Termux.
- **Bulk Extraction:** Menarik semua password tanpa perlu input manual satu per satu.
- **Root/Admin Checker:** Memastikan hak akses cukup untuk mendekripsi database password.
- **Clean Output:** Hasil rapi dengan format `SSID | PASSWORD`.

## 📦 Installation & Usage

### 💻 Windows (CMD/PowerShell)
Cukup jalankan file `spy-harvest.bat` sebagai **Administrator**.

### 🐧 Linux & 📱 Termux (Root)
```bash
git clone [https://github.com/SPY-E/spy-wifi-harvester.git](https://github.com/SPY-E/spy-wifi-harvester.git)
cd spy-wifi-harvester
python3 spy-harvest.py
