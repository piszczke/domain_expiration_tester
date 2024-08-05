import json
import whois


def load_domains(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def check_expiration(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info.expiration_date
    except Exception as e:
        print(f"Error fetching WHOIS data for {domain}: {e}")
        return None

def main(json_file):
    domains = load_domains(json_file)

    print("Domain Expiration Check\n" + "="*25)

    for domain in domains:
        expiration_date = check_expiration(domain)
        print(f"Domain: {domain}\nExpiration Date: {expiration_date}\n")

if __name__ == "__main__":
    json_file = 'domains.json'  # Path to your JSON file
    main(json_file)