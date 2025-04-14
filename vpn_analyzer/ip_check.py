import requests

def get_public_ip():
    try:
        res = requests.get("https://api.ipify.org?format=json", timeout=5)
        res.raise_for_status()
        return res.json().get("ip")
    except requests.RequestException:
        return "Could not fetch IP"

def get_ip_details(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        res.raise_for_status()
        return res.json()
    except requests.RequestException:
        return {"error": "Could not fetch IP details"}

def run_ip_check():
    ip = get_public_ip()
    details = get_ip_details(ip)
    return ip, details