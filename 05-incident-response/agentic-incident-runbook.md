# Agentic AI Incident Response Runbook

**Document ID:** AGENT-IR-2026-001  
**Date:** 1 September 2026  
**Version:** 1.0

---

## 1. Purpose

This runbook establishes the protocol for detecting, assessing, responding to, and learning from incidents involving agentic AI systems[reference:34].

---

## 2. Incident Severity Classification

### 2.1 Severity Tiers

| Severity | Definition | Examples | Reporting Timeline |
|----------|------------|----------|-------------------|
| **Critical** | Agent causing significant financial harm, data breach, or regulatory violation | Rogue agent executing unauthorized trades; agent exfiltrating sensitive data | 2-10 days to authority |
| **High** | Agent causing moderate harm or material compliance violation | Goal hijacking resulting in unauthorized actions; cost runaway exceeding $100k | 15 days to authority |
| **Medium** | Agent causing operational disruption | Tool misuse; minor cost runaway; hallucination cascade | Internal within 24 hours |
| **Low** | Minor anomalies | Minor prompt injection attempts; benign hallucinations | Internal within 7 days |

### 2.2 Severity Decision Matrix

| Impact | Likelihood | Severity |
|--------|------------|----------|
| High | High | Critical |
| High | Medium | High |
| High | Low | Medium |
| Medium | High | High |
| Medium | Medium | Medium |
| Medium | Low | Low |
| Low | Any | Low |

---

## 3. Incident Response Workflow

### 3.1 Detection

| Detection Source | Description | Owner |
|------------------|-------------|-------|
| **Runtime Monitoring** | Anomaly detection alerts from Agent Governance Toolkit[reference:35] | Security |
| **Cost Alerts** | Spending threshold breaches | FinOps |
| **User Reports** | Reports of unexpected agent behavior | Support |
| **Internal Reviews** | Periodic agent behavior reviews | AI Governance |
| **Tool Logs** | Unusual tool or API usage patterns | Security |

### 3.2 Triage & Classification

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Acknowledge** | Log the incident in the incident tracking system | Incident Manager | Immediate |
| **Classify** | Assign severity tier using the decision matrix | Incident Manager | < 30 min |
| **Assign** | Assign incident owner based on agent type | Incident Manager | < 30 min |
| **Notify** | Notify required stakeholders per tier | Incident Manager | Per timeline |

### 3.3 Containment

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Kill-Switch** | Activate emergency shutdown if necessary | Security | < 15 min for Critical |
| **Revoke Credentials** | Revoke the agent's credentials | IAM | < 15 min |
| **Isolate** | Isolate affected systems and data | Security | < 30 min |
| **Preserve Evidence** | Secure logs, agent snapshots, and incident data | Incident Manager | < 60 min |

### 3.4 Investigation & Root Cause Analysis

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Collect Data** | Gather logs, agent actions, and outputs | Incident Manager | < 24 hours |
| **Analyze** | Determine root cause (technical, process, data, or external) | Root Cause Team | < 72 hours |
| **Document** | Create incident report with findings | Incident Manager | < 5 days |

**Root Cause Categories:**

| Category | Examples |
|----------|----------|
| **Technical** | Model drift, software bug, configuration error |
| **Process** | Human error, oversight failure, inadequate testing |
| **Data** | Poisoned memory, biased training, data leakage |
| **External** | Adversarial attack, vendor failure, regulatory change |

### 3.5 Remediation & Recovery

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Fix Root Cause** | Implement permanent fix | Engineering | < 10 days |
| **Test** | Validate fix before re-deployment | ML Ops + Security | < 5 days |
| **Re-deploy** | Return agent to production | ML Ops | After validation |
| **Notify** | Notify stakeholders of resolution | Incident Manager | Upon resolution |

### 3.6 Post-Incident Review

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **After-Action Report** | Document full timeline, impact, root cause, remediation | Incident Manager | < 7 days |
| **Lessons Learned** | Identify improvements to controls or runbook | AI Governance Council | < 7 days |
| **Control Updates** | Update controls based on findings | AI Risk WG | < 30 days |
| **Board Report** | Report material incidents to Board Committee | CAIO | Quarterly |

---

## 4. Incident Communication Templates

### 4.1 Internal Notification Template
AGENTIC AI INCIDENT NOTIFICATION — [Severity]

Incident ID: AGENT-INC-2026-XXX
Agent: [Agent Name]
Agent ID: [Agent ID]
Date/Time: [Timestamp]
Severity: [Critical/High/Medium/Low]
Description: [Brief description]
Status: [Investigating/Containing/Remediated/Closed]
Impact: [Affected systems, financial impact, regulatory impact]
Owner: [Name]
Next Update: [Time]


### 4.2 Regulatory Notification Template
AGENTIC AI SERIOUS INCIDENT NOTIFICATION

Notification Date: [Date]
Notifying Entity: [Organization]
Agent: [Agent Name]
Agent ID: [Agent ID]
Incident Description: [Detailed description]
Date of Incident: [Date]
Date of Detection: [Date]
Affected Individuals: [Number]
Impact Assessment: [Financial, operational, regulatory impact]
Root Cause: [Preliminary findings]
Mitigations Taken: [Actions taken]
Contact Person: [Name, Title, Email, Phone]


---

## 5. Incident Log

| Incident ID | Agent | Severity | Date | Status | Owner |
|-------------|-------|----------|------|--------|-------|
| AGENT-INC-2026-001 | TradingBot | Medium | 15 Jan 2026 | Closed | Security |
| AGENT-INC-2026-002 | SupportAgent | Low | 12 Feb 2026 | Closed | ML Ops |
| AGENT-INC-2026-003 | DataScraper | High | 20 Mar 2026 | Open | Security |

---

## 6. Signatories

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | CISO | | |
| | Head of AI Governance | | |
| | AI Governance Council Chair | | |
