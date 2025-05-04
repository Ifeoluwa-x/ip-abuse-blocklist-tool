```markdown
# IP Abuse Blocklist Tool

This is a **mini SOC Analyst tool** I built to help flag and block abusive IPs based on real-time data from the [AbuseIPDB](https://abuseipdb.com) API. It automates the process of checking IPs for abuse reports and generates a blocklist for suspicious ones.

## 🔧 Features

- Reads IPs from a file (`ips.txt`)
- Queries AbuseIPDB for each IP address
- Flags IPs with an abuse confidence score of 70 or higher
- Writes flagged IPs to `blocklist.txt`
- Displays real-time scores for each IP
- Measures total runtime for the entire check

## 🧪 Example

```bash
$ python check_ips.py
Checking 178.62.21.86...
 → Score: 88
   🚩 Flagged: 178.62.21.86
...
✅ Done. Flagged 10 suspicious IPs.
⏱️ Total runtime: 19.2 seconds
```

## 🚀 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ip-abuse-blocklist-tool.git
   cd ip-abuse-blocklist-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```env
   API_KEY=your_abuseipdb_api_key
   ```

4. Add IPs to `ips.txt` (one per line), then run:
   ```bash
   python check_ips.py
   ```

## 📂 Files

- `check_ips.py`: Main script
- `ips.txt`: Input file for IP addresses
- `blocklist.txt`: Output file for flagged IPs
- `.env`: Stores your AbuseIPDB API key (should not be committed)
- `.gitignore`: Prevents `.env` from being tracked
- `requirements.txt`: Python dependencies

## 📄 License

MIT License
```
