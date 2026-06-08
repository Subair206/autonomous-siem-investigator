import splunklib.client as client
import splunklib.results as results
import json
import urllib3

# Suppress local self-signed SSL/TLS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- SPLUNK CLIENT CONFIGURATION ---
SPLUNK_HOST = "127.0.0.1"
SPLUNK_PORT = 8089 # The default Splunk Management/API port
SPLUNK_USER = "admin"
SPLUNK_PASSWORD = "SecurityLab2026!" # Uses the credentials we seeded earlier

print("[*] Connecting to Splunk Enterprise API Gateway...")
try:
    # Establish an authenticated programmatic session with your local SIEM
    service = client.connect(
        host=SPLUNK_HOST,
        port=SPLUNK_PORT,
        username=SPLUNK_USER,
        password=SPLUNK_PASSWORD,
        verify=False
    )
    print("[+] Connection successful! Fetching recent critical alerts...")
    
    # Define our SPL search query targeting the data your simulator injected
    search_query = "search index=mac_telemetry severity=CRITICAL"
    
    # Run a blocking search job on the Splunk engine
    kwargs_normal = {"exec_mode": "blocking"}
    job = service.jobs.create(search_query, **kwargs_normal)
    
    # Parse the raw binary results into clean dictionaries
    search_results = job.results(output_mode="json")
    reader = results.JSONResultsReader(search_results)
    
    alert_counter = 0
    print("\n=== RAW SECURITY LOGS RETRIEVED FOR AI ANALYSIS ===")
    for result in reader:
        if isinstance(result, results.Message):
            # Skip debug system messages
            continue
        elif isinstance(result, dict):
            alert_counter += 1
            # Extract the raw JSON event payload we injected earlier
            raw_event = json.loads(result['_raw'])
            print(f"\n[Alert #{alert_counter}] Details:")
            print(json.dumps(raw_event, indent=4))
            
    if alert_counter == 0:
        print("[-] No critical alerts found. Run your 'sim_attack.py' script again to generate telemetry!")

except Exception as e:
    print(f"[!] Error communicating with Splunk API: {e}")
