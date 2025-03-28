
async function fetchData() {
  const r = await fetch("/api/system"); const d = await r.json();
  document.getElementById("cpu").textContent = d.cpu + "%";
  document.getElementById("ram").textContent = d.ram + "%";
  document.getElementById("temp").textContent = d.temp + "°C";
  document.getElementById("vpn").textContent = d.vpn_status;
  document.getElementById("updates").textContent = d.updates || "-";
  let diskKey = Object.keys(d.disks)[0]; document.getElementById("disk").textContent = d.disks[diskKey] + "%";
}
async function scanNmap() {
  let host = document.getElementById("nmapHost").value;
  let r = await fetch("/api/nmap?target=" + host); let d = await r.json();
  document.getElementById("nmapResult").textContent = d.output || d.error || "Brak danych";
}
fetchData(); setInterval(fetchData, 10000);
