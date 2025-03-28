#!/bin/bash

echo "[+] Instalacja Pi Dashboard (Shell Edition)"
INSTALL_DIR="/opt/pi-dashboard"
PORT=5000

echo "[+] Tworzenie katalogu docelowego..."
sudo mkdir -p $INSTALL_DIR
sudo chown $USER:$USER $INSTALL_DIR

echo "[+] Pobieranie i rozpakowywanie archiwum..."
cd /tmp
curl -L -o dashboard.zip https://your-download-link/pi-dashboard-shell.zip
unzip dashboard.zip -d $INSTALL_DIR

echo "[+] Instalacja zależności..."
sudo apt update
sudo apt install -y python3 python3-pip nmap shellinabox
pip3 install flask psutil

echo "[+] Tworzenie usługi systemd..."
SERVICE_FILE=/etc/systemd/system/pi-dashboard.service
sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=Pi Dashboard Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 $INSTALL_DIR/backend/api.py
WorkingDirectory=$INSTALL_DIR/backend
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOL

echo "[+] Uruchamianie i włączanie usługi..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable pi-dashboard
sudo systemctl start pi-dashboard

echo "[+] Gotowe! Dashboard dostępny pod: http://<Twoje_IP>:$PORT"
echo "[i] Terminal SSH przez ShellInABox: http://<Twoje_IP>:4200"
