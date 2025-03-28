# Raspberry Pi Dashboard (Shell Edition)

Minimalistyczny dashboard dla Raspberry Pi z:
- Statystykami systemowymi (CPU, RAM, Temp, dyski)
- Status VPN (wg0)
- Ping do usług: Google, Cloudflare, OpenDNS
- Skanerem Nmap
- Terminalem SSH przez przeglądarkę (ShellInABox)

## 📦 Instalacja

```bash
chmod +x install-pi-dashboard.sh
./install-pi-dashboard.sh
```

## 📁 Struktura
- `frontend/` – statyczny dashboard (HTML/CSS/JS)
- `backend/` – API oparte na Flasku (`api.py`)
- `install-pi-dashboard.sh` – skrypt instalacyjny

## 🌐 Dostęp
- Dashboard: `http://<IP>:5000`
- Terminal: `http://<IP>:4200`

## ✅ Wymagania
- Python 3
- Flask, psutil
- nmap, shellinabox
