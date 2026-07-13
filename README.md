# 
🚨 Autonomous SIEM Investigator
An engineering proof-of-concept focused on automating high-velocity Tier-1 incident response triage. This project is a proof-of-concept that automates Tier-1 incident triage by collecting security telemetry from Splunk, enriching alert context, and generating structured incident response playbooks. The goal is to reduce manual investigation time and improve analyst efficiency.

## 🎯 The Problem Statement

Modern Security Operations Centers (SOCs) are plagued by alert fatigue. Analysts spend crucial minutes manually pivoting across multiple dashboards—correlating cloud provider identity changes with container runtime logs—just to establish a baseline incident timeline.
The Solution: An autonomous pipeline that detects threats at the ingestion layer, uses an orchestration fabric to query the SIEM via API, maps the telemetry against a security context engine, and instantly outputs formatted markdown incident triage playbooks. This drastically reduces Mean Time to Triage (MTTT) from minutes to milliseconds.

## 🏗️ System Architecture
The pipeline decouples telemetry generation, security log storage, extraction middleware, and context-aware intelligence.
A

```text

```text
 ┌───────────────────────────┐
 │   Python Attack Engine    │  (Safely simulates cloud threats)
 └─────────────┬─────────────┘
               │ (HTTPS POST via Port 8088)
               ▼
 ┌───────────────────────────┐
 │ Splunk HEC Data Ingestion │  (Ingests structured JSON payloads)
 └─────────────┬─────────────┘
               │ (Stores in custom 'mac_telemetry' index)
               ▼
 ┌───────────────────────────┐
 │ Splunk Enterprise Daemon  │  (Core SIEM Data Lake)
 └─────────────▲─────────────┘
               │ (Programmatic authenticated SDK session via Port 8089)
               ▼
 ┌───────────────────────────┐
 │ Python Triage Middleware  │  (Executes blocking SPL queries)
 └─────────────┬─────────────┘
               │ (Passes raw JSON string payloads)
               ▼
 ┌───────────────────────────┐
 │ Agentic Intelligence Core │  (Generates automated IR markdown playbooks)


## 🧰 Tech Stack & Infrastructure

SIEM Platform: Splunk Enterprise (Native ARM64 Daemon)
Ingestion Gateway: Splunk HTTP Event Collector (HEC) over TLS 1.3
Automation Fabric: Python 3.9+
Integration Vector: Official Splunk SDK Developer Framework (splunklib)
Data Serialization: Structured _json schemas

### 


Key Skills Demonstrated
Python automation
Security operations workflows
Splunk integration
Incident response triage
API integrations
Security telemetry analysis
Documentation automation
