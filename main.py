from vpn_analyzer.ip_check import run_ip_check
from vpn_analyzer.dns_check import run_dns_check
from vpn_analyzer.webrtc_check import run_webrtc_check

def main():
    print("🔍 VPN Exposure Analyzer")
    
    print("\n🌐 IP Check:")
    ip, details = run_ip_check()
    print(f"  Public IP: {ip}")
    print("  IP Details:")
    for key, value in details.items():
        print(f"    {key}: {value}")

    print("\n🧠 DNS Check:")
    dns_servers = run_dns_check()
    for server in dns_servers:
        print(f"  DNS Server: {server}")

    print("\n🕳️ WebRTC Leak Check:")
    webrtc_ips = run_webrtc_check()
    for ip in webrtc_ips:
        print(f"  Leaked IP: {ip}")

if __name__ == "__main__":
    main()