import splunklib.client as client
import splunklib.results as results
import json
import urllib3
from datetime import datetime

# Suppress local self-signed SSL/TLS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- SPLUNK CLIENT CONFIGURATION ---
SPLUNK_HOST = "127.0.0.1"
SPLUNK_PORT = 8089 
SPLUNK_USER = "admin"
SPLUNK_PASSWORD = "SecurityLab2026!" 

def mock_llm_analyst(security_log):
    """
    Simulates a localized, deterministic LLM context window analysis.
    This mimics how Claude/GPT processes the data payload and extracts intelligence.
    """
    alert_name = security_log.get("alert_type", "Unknown Threat")
    severity = security_log.get("severity", "INFO")
    
    # Context-aware logic engineering based on incoming JSON schema keys
    if "Kubernetes" in alert_name:
        target_asset = security_log.get("compromised_pod", "Unknown Pod")
        vector = security_log.get("action_taken", "N/A")
        namespace = security_log.get("namespace", "default")
        source = security_log.get("src_ip", "Unknown IP")
        
        markdown_report = f"""
# 🚨 SEC_AGENT_REPORT: {alert_name.upper()}
**Timestamp Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Threat Severity Level:** {severity}

## 🔍 Incident Context Summary
An automated analysis engine parsed a critical telemetry anomaly originating from the container orchestration fabric. An anomalous actor at source IP **{source}** initiated unauthorized discovery vectors against cluster configuration files.

## 🎯 Target Information
* **Compromised Asset:** {target_asset}
* **Cluster Namespace:** {namespace}
* **Attacker Action Executed:** {vector}

## 🛡️ Recommended Incident Response Playbook (Tier-1 Triage)
1. **Isolate Network Topology:** Immediately execute `kubectl delete pod {target_asset} -n {namespace}` to terminate the compromised runtime environment.
2. **Revoke Secrets:** Rotate all service account tokens associated with the `{namespace}` namespace.
3. **Block Source IP:** Apply a network security policy rule to drop incoming traffic from host `{source}` at the firewall perimeter.
"""
    elif "AWS" in alert_name:
        user = security_log.get("user_identity", "Unknown User")
        role = security_log.get("assumed_role", "Unknown Role")
        loc = security_log.get("location", "Unknown Location")
        
        markdown_report = f"""
# 🚨 SEC_AGENT_REPORT: {alert_name.upper()}
**Timestamp Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Threat Severity Level:** {severity}

## 🔍 Incident Context Summary
CloudTrail log parsing detected a high-severity IAM authorization bypass anomaly. A credential set mapping to identity **{user}** successfully escalated execution boundaries to an administrative tier from an unverified network gateway.

## 🎯 Target Information
* **Target Identity:** {user}
* **Escalated Role Assumed:** {role}
* **Geographic/Network Anomaly:** Traffic originating from *{loc}*

## 🛡️ Recommended Incident Response Playbook (Tier-1 Triage)
1. **Quarantine Identity:** Apply an explicit `DeniAll` inline policy to IAM User `{user}` to freeze active runtime access.
2. **Invalidate Sessions:** Terminate all active global programmatic STS sessions associated with role `{role}`.
3. **Audit Log Trail:** Initiate an historical cloud trail query across the source network gateway to calculate data exfiltration vectors.
"""
    else:
        markdown_report = "# SEC_AGENT_REPORT: Unrecognized telemetry structure configuration."
        
    return markdown_report


# --- MAIN PIPELINE EXECUTION ---
print("[*] Connecting to Splunk Enterprise API Gateway...")
try:
    service = client.connect(
        host=SPLUNK_HOST, port=SPLUNK_PORT, username=SPLUNK_USER, password=SPLUNK_PASSWORD, verify=False
    )
    print("[+] Connection successful! Querying live indexes...")
    
    # We broaden our query to capture BOTH alerts now (CRITICAL and HIGH)
    search_query = "search index=mac_telemetry"
    kwargs_normal = {"exec_mode": "blocking"}
    job = service.jobs.create(search_query, **kwargs_normal)
    
    search_results = job.results(output_mode="json")
    reader = results.JSONResultsReader(search_results)
    
    report_counter = 0
    for result in reader:
        if isinstance(result, dict):
            report_counter += 1
            raw_event = json.loads(result['_raw'])
            
            # Pass the raw log dynamically to the simulated LLM engine
            compiled_analysis = mock_llm_analyst(raw_event)
            print(compiled_analysis)
            print("-" * 60)
            
    if report_counter == 0:
        print("[-] No events found inside the index. Refresh your telemetry simulator!")

except Exception as e:
    print(f"[!] Core pipeline failure: {e}")
