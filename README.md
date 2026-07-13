# 🚨 Autonomous SIEM Investigator

An engineering proof-of-concept focused on automating high-velocity Tier-1 incident response triage.

This project automates Tier-1 incident triage by collecting security telemetry from Splunk, enriching alert context, and generating structured incident response playbooks. The goal is to reduce manual investigation time, improve analyst efficiency, and accelerate security response workflows.

---

## 🎯 The Problem

Modern Security Operations Centers (SOCs) are often overwhelmed by alert fatigue. Analysts spend valuable time manually pivoting across multiple tools and dashboards to establish incident context before meaningful investigation can begin.

For example, analysts may need to correlate:

- Cloud identity changes
- Authentication events
- Container activity
- Infrastructure logs
- Security alerts

This manual process increases Mean Time to Triage (MTTT) and reduces operational efficiency.

### Solution

The Autonomous SIEM Investigator automates the collection and correlation of security telemetry by:

1. Ingesting structured security events into Splunk
2. Querying relevant telemetry through the Splunk API
3. Enriching alert context programmatically
4. Generating structured incident response playbooks
5. Presenting actionable investigation guidance to analysts

---

## 🛠️ Key Skills Demonstrated

- Python Automation
- Security Operations Workflows
- Splunk Integration
- Incident Response Triage
- API Integrations
- Security Telemetry Analysis
- Documentation Automation
- Security Engineering Fundamentals

---

## 🏗️ System Architecture

The pipeline separates telemetry generation, log ingestion, data retrieval, and automated investigation workflows.

```text
 ┌───────────────────────────┐
 │   Python Attack Engine    │
 │ (Safely simulates threats)│
 └─────────────┬─────────────┘
               │ HTTPS POST
               ▼
 ┌───────────────────────────┐
 │ Splunk HEC Ingestion      │
 │ (Structured JSON Events)  │
 └─────────────┬─────────────┘
               │
               ▼
 ┌───────────────────────────┐
 │ Splunk Enterprise         │
 │ (Security Data Platform)  │
 └─────────────▲─────────────┘
               │ Splunk SDK
               ▼
 ┌───────────────────────────┐
 │ Python Triage Middleware  │
 │ (Search & Correlation)    │
 └─────────────┬─────────────┘
               │
               ▼
 ┌───────────────────────────┐
 │ Investigation Engine      │
 │ (Playbook Generation)     │
 └───────────────────────────┘
```

---

## 🧰 Tech Stack & Infrastructure

| Component | Technology |
|------------|------------|
| SIEM Platform | Splunk Enterprise |
| Data Ingestion | Splunk HTTP Event Collector (HEC) |
| Programming Language | Python 3.9+ |
| API Integration | Splunk SDK (splunklib) |
| Data Format | Structured JSON |
| Communication | HTTPS / TLS |
| Security Focus | Incident Response & Security Operations |

---

## 🚀 Project Goals

- Reduce manual Tier-1 triage effort
- Improve analyst productivity
- Accelerate incident investigations
- Standardize response workflows
- Demonstrate security automation concepts
- Explore practical applications of AI-assisted security operations
