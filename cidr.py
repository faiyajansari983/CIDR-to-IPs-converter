import sys
import ipaddress

def cidr_to_ips(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        return "Invalid CIDR range."

def main():
    if len(sys.argv) != 2:
        print("Usage: python cidr_to_ips.py <CIDR>")
        sys.exit(1)

    cidr = sys.argv[1]
    ips = cidr_to_ips(cidr)

    if isinstance(ips, list):
        for ip in ips:
            print(ip)
    else:
        print(ips)  # Prints error message if CIDR is invalid

if __name__ == "__main__":
    main()
