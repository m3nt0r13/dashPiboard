# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, send_from_directory
import subprocess, psutil

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route("/api/system")
def system():
    return jsonify({
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "temp": get_temp(),
        "vpn_status": get_vpn(),
        "disks": get_disks(),
        "updates": get_updates()
    })

@app.route("/api/nmap")
def nmap():
    target = request.args.get("target")
    if not target: return jsonify({"error": "Brak celu"}), 400
    try:
        out = subprocess.check_output(["nmap", "-F", target], timeout=10).decode()
        return jsonify({"output": out})
    except Exception as e:
        return jsonify({"error": str(e)})

def get_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return round(int(f.read()) / 1000.0, 1)
    except: return None

def get_vpn():
    try:
        out = subprocess.check_output(["ip", "link", "show", "wg0"])
        return "online" if b"UP" in out else "offline"
    except: return "offline"

def get_disks():
    usage = {}
    for p in psutil.disk_partitions():
        if p.mountpoint.startswith("/"):
            try: usage[p.mountpoint] = psutil.disk_usage(p.mountpoint).percent
            except: usage[p.mountpoint] = None
    return usage

def get_updates():
    try:
        out = subprocess.check_output("apt list --upgradable 2>/dev/null | grep -v Listing | wc -l", shell=True)
        return int(out.decode().strip())
    except: return 0

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
