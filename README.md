# 
🚨 Autonomous SIEM Investigator
An engineering proof-of-concept focused on automating high-velocity Tier-1 incident response triage. This project bridges the gap between structured SIEM logging engines and agentic AI architectures, converting raw infrastructure security alerts into contextualized, actionable incident response playbooks programmatically.

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
