from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def run_webrtc_check():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://browserleaks.com/webrtc")

    time.sleep(5)  # Give the page some time to load

    page_source = driver.page_source
    driver.quit()

    # Extract internal IPs shown in the WebRTC section
    ip_pattern = re.compile(r"(\d{1,3}(?:\.\d{1,3}){3})")
    found_ips = ip_pattern.findall(page_source)
    unique_ips = list(set(found_ips))

    return unique_ips

if __name__ == "__main__":
    print("🌐 WebRTC Leak Check")
    leaks = run_webrtc_check()
    for ip in leaks:
        print(f"🕳️ Leaked IP: {ip}")