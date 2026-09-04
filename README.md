# 🤖 Agentic AI Governance Framework

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![OWASP Agentic](https://img.shields.io/badge/OWASP%20Agentic-Aligned-blue.svg)]()
[![NIST AI RMF](https://img.shields.io/badge/NIST%20AI%20RMF-Mapped-green.svg)]()
[![CSA ATF](https://img.shields.io/badge/CSA%20ATF-Compatible-purple.svg)]()

---

## 📋 Table of Contents

- [About This Framework](#-about-this-framework)
- [Why Agentic AI Governance?](#-why-agentic-ai-governance)
- [What's Inside](#-whats-inside)
- [Framework Architecture](#-framework-architecture)
- [Quick Start](#-quick-start)
- [Key Artifacts](#-key-artifacts)
- [Regulatory & Industry Alignment](#-regulatory--industry-alignment)
- [Contact](#-contact)
- [License](#-license)

---

## 🎯 About This Framework

This repository contains a **complete, production-ready governance framework** for **Agentic AI** — autonomous AI systems that can plan, act, and adapt with minimal human intervention.

The framework is:

- ✅ **Practical** — Built from real-world implementation experience
- ✅ **Implementable** — Ready-to-use templates, controls, and runbooks
- ✅ **Audit-Ready** — Designed to satisfy regulatory and internal audit requirements
- ✅ **Framework-Aligned** — Mapped to OWASP Agentic Top 10, NIST AI RMF, IMDA Model Framework, and CSA Agentic Trust Framework[reference:0][reference:1][reference:2]

**Organization:** NovaTech Financial Group *(hypothetical)*  
**Effective Date:** 1 September 2026  
**Version:** 1.0

---

## 🚨 Why Agentic AI Governance?

Agentic AI represents a fundamental shift in risk profile. Unlike traditional AI that generates outputs, agentic AI:

| Traditional AI | Agentic AI |
|----------------|------------|
| Generates recommendations | Takes autonomous actions |
| Requires human approval | Executes independently |
| Single-turn interactions | Multi-step planning and execution |
| Limited tool access | Full tool and API integration |
| Predictable outputs | Emergent, adaptive behavior |

> **The Governance Gap:** Traditional AI governance frameworks assume human-in-the-loop oversight. Agentic AI breaks this assumption. **We need new controls.**

The OWASP Top 10 for Agentic Applications 2026 identifies critical risks including:
- **Goal Hijacking** — Agents manipulated to pursue malicious objectives[reference:3]
- **Tool Misuse** — Agents using tools in unauthorized ways[reference:4]
- **Privilege Abuse** — Agents escalating their own permissions[reference:5]
- **Rogue Agents** — Unauthorized or compromised agents[reference:6]
- **Excessive Agency** — Agents given too much autonomy[reference:7]

**This framework addresses all of these risks with enforceable controls.**

---

## 📂 What's Inside

| Folder | Description |
|--------|-------------|
| **01-principles** | Core governance principles for agentic AI |
| **02-risk-register** | Comprehensive risk register + autonomy impact assessment |
| **03-controls** | Enforceable controls: identity, sandboxing, delegation, human escalation |
| **04-monitoring** | Activity logging, cost runaway detection, KRI dashboards |
| **05-incident-response** | Agentic-specific incident runbook with severity tiers |
| **06-frameworks-mapping** | Mappings to OWASP, NIST AI RMF, IMDA, CSA ATF |
| **07-templates** | Agent Passport System, Deployment Approval Form |
| **examples** | Complete example: Autonomous Trading Agent |
| **scripts** | Agent inventory scanner and control validator |

---

## 🏗️ Framework Architecture
┌─────────────────────────────────────────────────────────────────┐
│ GOVERNANCE LAYER │
│ Principles | Risk Register | Policies │
├─────────────────────────────────────────────────────────────────┤
│ CONTROL LAYER │
│ Identity & Access | Sandboxing | Delegation | Human Escalation│
├─────────────────────────────────────────────────────────────────┤
│ MONITORING LAYER │
│ Activity Logging | Cost Detection | KRI Dashboards │
├─────────────────────────────────────────────────────────────────┤
│ RESPONSE LAYER │
│ Incident Runbook | Escalation | Recovery │
└─────────────────────────────────────────────────────────────────┘


**Core Principle:** *Agents begin with zero trust and earn autonomy through demonstrated reliability.*[reference:8]

---

## 🚀 Quick Start

| Step | Action | Description |
|------|--------|-------------|
| **1** | Review principles | Understand the governance philosophy |
| **2** | Assess risks | Use the risk register for your agentic systems |
| **3** | Implement controls | Apply identity, sandboxing, and delegation controls |
| **4** | Deploy monitoring | Set up activity logging and cost detection |
| **5** | Prepare for incidents | Review and customize the incident runbook |
| **6** | Run the scanner | Use `scripts/agent-inventory-scanner.py` to discover agents |

---

## 🏆 Key Artifacts

### 1. [Agentic AI Risk Register](02-risk-register/agentic-ai-risk-register.md)

A comprehensive risk register covering 12+ agentic-specific risks:

| Risk Category | Examples |
|---------------|----------|
| **Autonomy Escalation** | Agents increasing their own permissions |
| **Goal Hijacking** | Agents pursuing malicious objectives |
| **Tool Misuse** | Unauthorized tool or API access |
| **Cost Runaway** | Uncontrolled resource consumption |
| **Rogue Agents** | Unauthorized or compromised agents |

### 2. [Identity & Access Controls](03-controls/identity-access-controls.md)

Zero-trust identity management for AI agents:

- Cryptographically anchored agent identities[reference:9]
- Short-lived credentials with automatic rotation[reference:10]
- Strict least-privilege scoping[reference:11]
- Human approval gates for high-impact actions[reference:12]

### 3. [Agentic Incident Runbook](05-incident-response/agentic-incident-runbook.md)

Agentic-specific incident response:

| Severity | Examples | Timeline |
|----------|----------|----------|
| **Critical** | Rogue agent, financial fraud | 2-10 days |
| **High** | Goal hijacking, data exfiltration | 15 days |
| **Medium** | Cost runaway, minor tool misuse | 24 hours |

### 4. [OWASP Agentic Top 10 Mapping](06-frameworks-mapping/owasp-agentic-top-10-mapping.md)

Complete mapping of OWASP Agentic Top 10 risks to controls[reference:13].

### 5. [Agent Passport System](07-templates/agent-passport-template.md)

Identity and authorization framework for every agent in your environment[reference:14].

---

## 🔗 Regulatory & Industry Alignment

| Framework | Alignment | Artifact |
|-----------|-----------|----------|
| **OWASP Agentic Top 10 2026** | ✅ Full Mapping | `06-frameworks-mapping/owasp-agentic-top-10-mapping.md` |
| **NIST AI RMF Agentic Profile** | ✅ Full Mapping | `06-frameworks-mapping/nist-ai-rmf-agentic-mapping.md` |
| **IMDA Model AI Governance Framework for Agentic AI** | ✅ Full Mapping | `06-frameworks-mapping/imda-agentic-framework-mapping.md`[reference:15] |
| **CSA Agentic Trust Framework** | ✅ Full Mapping | `06-frameworks-mapping/imda-agentic-framework-mapping.md`[reference:16] |
| **CISA Agentic AI Secure Adoption Guide** | ✅ Aligned | All controls[reference:17] |

---

## 📫 Contact

| Channel | Details |
|---------|---------|
| **GitHub** | [github.com/yourusername](https://github.com/yourusername) |
| **LinkedIn** | [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile) |
| **Email** | your.email@domain.com |

---

## 📝 License

This framework is licensed under the **MIT License**. You are free to use, modify, and distribute with attribution.

---

## ⭐ Star This Repository

If you find this framework helpful, please **star** this repository and share it with your network!

**Core Principle:** *Agents begin with zero trust and earn autonomy through demonstrated reliability.*[reference:8]

---

## 🚀 Quick Start

| Step | Action | Description |
|------|--------|-------------|
| **1** | Review principles | Understand the governance philosophy |
| **2** | Assess risks | Use the risk register for your agentic systems |
| **3** | Implement controls | Apply identity, sandboxing, and delegation controls |
| **4** | Deploy monitoring | Set up activity logging and cost detection |
| **5** | Prepare for incidents | Review and customize the incident runbook |
| **6** | Run the scanner | Use `scripts/agent-inventory-scanner.py` to discover agents |

---

## 🏆 Key Artifacts

### 1. [Agentic AI Risk Register](02-risk-register/agentic-ai-risk-register.md)

A comprehensive risk register covering 12+ agentic-specific risks:

| Risk Category | Examples |
|---------------|----------|
| **Autonomy Escalation** | Agents increasing their own permissions |
| **Goal Hijacking** | Agents pursuing malicious objectives |
| **Tool Misuse** | Unauthorized tool or API access |
| **Cost Runaway** | Uncontrolled resource consumption |
| **Rogue Agents** | Unauthorized or compromised agents |

### 2. [Identity & Access Controls](03-controls/identity-access-controls.md)

Zero-trust identity management for AI agents:

- Cryptographically anchored agent identities[reference:9]
- Short-lived credentials with automatic rotation[reference:10]
- Strict least-privilege scoping[reference:11]
- Human approval gates for high-impact actions[reference:12]

### 3. [Agentic Incident Runbook](05-incident-response/agentic-incident-runbook.md)

Agentic-specific incident response:

| Severity | Examples | Timeline |
|----------|----------|----------|
| **Critical** | Rogue agent, financial fraud | 2-10 days |
| **High** | Goal hijacking, data exfiltration | 15 days |
| **Medium** | Cost runaway, minor tool misuse | 24 hours |

### 4. [OWASP Agentic Top 10 Mapping](06-frameworks-mapping/owasp-agentic-top-10-mapping.md)

Complete mapping of OWASP Agentic Top 10 risks to controls[reference:13].

### 5. [Agent Passport System](07-templates/agent-passport-template.md)

Identity and authorization framework for every agent in your environment[reference:14].

---

## 🔗 Regulatory & Industry Alignment

| Framework | Alignment | Artifact |
|-----------|-----------|----------|
| **OWASP Agentic Top 10 2026** | ✅ Full Mapping | `06-frameworks-mapping/owasp-agentic-top-10-mapping.md` |
| **NIST AI RMF Agentic Profile** | ✅ Full Mapping | `06-frameworks-mapping/nist-ai-rmf-agentic-mapping.md` |
| **IMDA Model AI Governance Framework for Agentic AI** | ✅ Full Mapping | `06-frameworks-mapping/imda-agentic-framework-mapping.md`[reference:15] |
| **CSA Agentic Trust Framework** | ✅ Full Mapping | `06-frameworks-mapping/imda-agentic-framework-mapping.md`[reference:16] |
| **CISA Agentic AI Secure Adoption Guide** | ✅ Aligned | All controls[reference:17] |

---

## 📫 Contact

| Channel | Details |
|---------|---------|
| **GitHub** | [github.com/yourusername](https://github.com/yourusername) |
| **LinkedIn** | [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile) |
| **Email** | your.email@domain.com |

---

## 📝 License

This framework is licensed under the **MIT License**. You are free to use, modify, and distribute with attribution.

---

## ⭐ Star This Repository

If you find this framework helpful, please **star** this repository and share it with your network!
