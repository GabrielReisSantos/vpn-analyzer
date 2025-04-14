# 🔍 VPN Exposure Analyzer

**Created by Gabriel Reis**

This tool helps you detect if your VPN setup is **truly protecting your privacy** by scanning for:

- 🌐 Public IP exposure
- 🧠 DNS leak detection
- 🕳️ WebRTC IP leaks
- 📢 Discord alert support

---

## 💡 Why I Built This

As part of building my **home SOC lab**, I wanted a tool that could verify if my VPN or proxy was leaking any private information — especially during malware analysis, browser fingerprinting, or traffic routing simulations. This tool will grow into a larger suite to ensure **endpoint anonymity and secure configurations** across my lab devices.

---

## 🛠️ How to Use

### 1. Clone and Install

```bash
git clone https://github.com/yourusername/vpn-exposure-analyzer.git
cd vpn-exposure-analyzer
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure

Open the file `config/settings.yaml` and add your **Discord webhook URL** (optional):

```yaml
discord_webhook: "https://discord.com/api/webhooks/..."
```

### 3. Run the Analyzer

```bash
python main.py
```

You’ll see a full breakdown in your terminal and (optionally) receive a report in Discord.

---

## 🔭 What’s Next

- Add support for:
  - IPv6 leak detection
  - GeoIP-based alert thresholds
  - Export logs as JSON/CSV
  - Integration with my SOC tools (Wazuh, TheHive, Shuffle)
- Create `.deb` and `.exe` installers for fast deployment
- Build a Flask web UI for remote control

---

## 🤝 Contributing

Feel free to fork the project and suggest improvements — this is just the beginning of a broader **home lab privacy & security toolkit**.

---

## 📄 License

MIT License