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
git clone https://github.com/123tool/Wifi-Bulk-Password-Hack.git
cd Wifi-Bulk-Password-Hack
python3 spy-harvest.py
```
### Panduan Instalasi & Penggunaan (Step-by-Step)

​A. Di Windows (Paling Gampang)
​Salin kode spy-harvest.bat ke Notepad.
​Simpan dengan nama spy-harvest.bat.
​Klik kanan file tersebut, pilih Run as Administrator.
​Boom! Semua password muncul.

​B. Di Linux / Kali Linux
​Simpan kode Python sebagai spy-harvest.py.
​Buka terminal, ketik: sudo python3 spy-harvest.py.
​Tool akan membongkar folder /etc/NetworkManager/ dan menampilkan password-nya.

​C. Di Termux (Android Rooted)
​Karena Termux berbasis Linux, ia bisa membaca file sistem jika HP sudah Root.
​Install Python: pkg install python.
​Jalankan dengan akses root: tsu -c python spy-harvest.py.
