import dns.resolver

def get_dns_servers():
    # List current system DNS resolvers
    return dns.resolver.Resolver().nameservers

def run_dns_check():
    servers = get_dns_servers()
    return servers

if __name__ == "__main__":
    print("🔎 DNS Leak Check")
    servers = run_dns_check()
    for server in servers:
        print(f"🧠 DNS Server: {server}")