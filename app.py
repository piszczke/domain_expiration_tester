import json
import whois
from datetime import datetime, timedelta
from colorama import Fore, Style, init

# Initialize colorama
init()

def load_domains(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def check_expiration(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info.expiration_date
    except Exception as e:
        print(f"{Fore.RED}Error fetching WHOIS data for {domain}: {e}{Style.RESET_ALL}")
        return None

def colorize_expiration_date(expiration_date):
    if not expiration_date:
        return f"{Fore.RED}Unknown{Style.RESET_ALL}"

    if isinstance(expiration_date, list):
        expiration_date = expiration_date[0]

    days_left = (expiration_date - datetime.now()).days

    if days_left <= 0:
        return f"{Fore.RED}{expiration_date} (Expired){Style.RESET_ALL}"
    elif days_left <= 30:
        return f"{Fore.YELLOW}{expiration_date} (Expiring Soon){Style.RESET_ALL}"
    else:
        return f"{Fore.GREEN}{expiration_date} (Valid){Style.RESET_ALL}"

def main(json_file):
    domains = load_domains(json_file)

    print("Domain Expiration Check\n" + "="*25)

    for domain in domains:
        expiration_date = check_expiration(domain)
        colored_date = colorize_expiration_date(expiration_date)
        print(f"Domain: {domain}\nExpiration Date: {colored_date}\n")

if __name__ == "__main__":
    json_file = 'domains.json'  # Path to your JSON file
    main(json_file)