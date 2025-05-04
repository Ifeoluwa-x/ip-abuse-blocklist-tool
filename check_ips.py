import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

INPUT_FILE = 'ips.txt'
BLOCKLIST_FILE = 'blocklist.txt'
THRESHOLD = 70  # Abuse Confidence Score threshold to block

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()['data']
        return data['abuseConfidenceScore']
    except Exception as e:
        print(f"Error checking IP {ip}: {e}")
        return None

def main():
    if not API_KEY:
        print("❌ API key not found. Make sure .env file is configured.")
        return

    start_time = time.time()  # Start timer

    with open(INPUT_FILE, 'r') as file:
        ips = [line.strip() for line in file if line.strip()]

    flagged_ips = []

    for ip in ips:
        print(f"\nChecking {ip}...")
        score = check_ip(ip)
        if score is not None:
            print(f" → Score: {score}")
            if score >= THRESHOLD:
                print(f"   🚩 Flagged: {ip} (Score: {score})")
                flagged_ips.append(ip)
        time.sleep(1)  

    with open(BLOCKLIST_FILE, 'w') as file:
        for ip in flagged_ips:
            file.write(f"{ip}\n")

    elapsed_time = time.time() - start_time
    print(f"\n✅ Done. Flagged {len(flagged_ips)} suspicious IPs.")
    print(f" Total runtime: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
