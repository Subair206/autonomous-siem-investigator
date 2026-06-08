import requests
import json
import time
import urllib3

# Suppress local self-signed SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURATION ---
SPLUNK_HOST = "127.0.0.1"
SPLUNK_PORT = "8088"  
HEC_TOKEN = "e035aad9-edfd-4a3f-9c8e-7a4d81ef4171" 

url = f"https://{SPLUNK_HOST}:{SPLUNK_PORT}/services/collector/event"
headers = {
    "Authorization": f"Splunk {HEC_TOKEN}",
    "Content-Type": "application/json"
}

# --- SIMULATED ATTACK PAYLOADS ---
mock_alerts = [
    {
        "event": {
            "alert_type": "Kubernetes Control Plane Probe",
            "severity": "CRITICAL",
            "src_ip": "10.244.0.5",
            "compromised_pod": "nginx-ingress-controller-7f89",
            "namespace": "production",
            "action_taken": "Attempted read of cluster-admin service account token file",
            "timestamp": time.time()
        },
        "sourcetype": "_json",
        "index": "mac_telemetry"
    },
    {
        "event": {
            "alert_type": "AWS IAM Role Assumption Anomaly",
            "severity": "HIGH",
            "user_identity": "arn:aws:iam::123456789012:user/dev-automation-service-account",
            "assumed_role": "arn:aws:iam::123456789012:role/AdminAccessViaCloudtrail",
            "location": "Unknown/Suspicious Hosting Provider",
            "status": "SUCCESS",
            "timestamp": time.time()
        },
        "sourcetype": "_json",
        "index": "mac_telemetry"
    }
]

# --- SEND DATA TO SPLUNK ---
print("[*] Launching Python Security Simulation...")
for alert in mock_alerts:
    try:
        response = requests.post(url, headers=headers, data=json.dumps(alert), verify=False)
        if response.status_code == 200:
            print(f"[+] Successfully sent: {alert['event']['alert_type']}")
        else:
            print(f"[-] Failed to send alert. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error connecting to Splunk: {e}")
