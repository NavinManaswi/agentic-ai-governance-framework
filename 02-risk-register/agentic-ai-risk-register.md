# Agentic AI Risk Register

**Document ID:** AGENT-RISK-2026-001  
**Date:** 1 September 2026  
**Version:** 1.0

---

## 1. Purpose

This document identifies, analyzes, and evaluates risks specific to agentic AI systems. It follows the NIST AI RMF framework and addresses the OWASP Agentic Top 10 2026[reference:24].

---

## 2. Risk Identification

| Risk ID | Risk Description | OWASP Mapping | Category | Inherent Risk |
|---------|------------------|---------------|----------|---------------|
| **AGT-R01** | **Goal Hijacking** — Agent is manipulated to pursue malicious or unintended objectives | ASI01 | Autonomy | Critical |
| **AGT-R02** | **Tool Misuse** — Agent uses tools or APIs in unauthorized ways | ASI02 | Security | Critical |
| **AGT-R03** | **Privilege Abuse** — Agent escalates its own permissions | ASI03 | Security | Critical |
| **AGT-R04** | **Excessive Agency** — Agent is given too much autonomy for its use case | ASI04 | Autonomy | High |
| **AGT-R05** | **Memory Poisoning** — Agent's memory is corrupted with malicious data | ASI05 | Data | High |
| **AGT-R06** | **Rogue Agent** — Unauthorized or compromised agent operates in the environment | ASI06 | Security | Critical |
| **AGT-R07** | **Cost Runaway** — Agent consumes uncontrolled resources | ASI07 | Operational | High |
| **AGT-R08** | **Hallucination Cascade** — Agent makes decisions based on false information | ASI08 | Reliability | High |
| **AGT-R09** | **Delegation Escalation** — Agent delegates tasks to untrusted sub-agents | ASI09 | Autonomy | Medium |
| **AGT-R10** | **Identity Spoofing** — Attacker impersonates a legitimate agent | ASI10 | Security | Critical |
| **AGT-R11** | **Prompt Injection** — Malicious input overrides agent instructions | LLM01 | Security | High |
| **AGT-R12** | **Data Leakage** — Agent exposes sensitive data through outputs | LLM02 | Privacy | High |

---

## 3. Risk Analysis

| Risk ID | Likelihood | Impact | Inherent Risk | Existing Controls | Residual Risk |
|---------|------------|--------|---------------|-------------------|---------------|
| AGT-R01 | Medium | Critical | Critical | Input validation; human oversight | High |
| AGT-R02 | Medium | Critical | Critical | Tool access policy; runtime enforcement | High |
| AGT-R03 | Low | Critical | Critical | Least privilege; permission boundaries | Medium |
| AGT-R04 | High | High | High | Autonomy tiers; approval gates | Medium |
| AGT-R05 | Medium | High | High | Memory validation; audit logs | Medium |
| AGT-R06 | Low | Critical | Critical | Agent inventory; anomaly detection | Medium |
| AGT-R07 | High | High | High | Cost monitoring; spending limits | Medium |
| AGT-R08 | Medium | High | High | Output validation; human review | Medium |
| AGT-R09 | Medium | Medium | Medium | Delegation policy; sub-agent tracking | Low |
| AGT-R10 | Low | Critical | Critical | Cryptographic identity; MFA | Medium |
| AGT-R11 | High | High | High | Input filtering; system prompt hardening | Medium |
| AGT-R12 | Medium | High | High | Output filtering; DLP | Medium |

---

## 4. Risk Treatment

| Risk ID | Treatment Decision | Treatment Plan | Owner | Target Date | Residual Risk |
|---------|-------------------|----------------|-------|-------------|---------------|
| AGT-R01 | Mitigate | Goal validation framework; human escalation for high-impact decisions | Security | 30 Nov 2026 | Medium |
| AGT-R02 | Mitigate | Tool access policy; runtime tool validation; Microsoft AGT integration[reference:25] | Security | 15 Nov 2026 | Medium |
| AGT-R03 | Mitigate | Zero-trust identity; permission boundaries; short-lived credentials[reference:26] | IAM | 30 Nov 2026 | Medium |
| AGT-R04 | Mitigate | Autonomy tiers; graduated deployment; human approval gates[reference:27] | AI Governance | 15 Oct 2026 | Medium |
| AGT-R05 | Mitigate | Memory validation; periodic memory review; immutable logs | Security | 15 Dec 2026 | Medium |
| AGT-R06 | Mitigate | Agent inventory; continuous monitoring; anomaly detection[reference:28] | Security | 15 Nov 2026 | Medium |
| AGT-R07 | Mitigate | Cost monitoring; spending limits; automatic kill-switch | FinOps | 15 Oct 2026 | Medium |
| AGT-R08 | Mitigate | Output validation; human review for critical decisions | ML Ops | 30 Nov 2026 | Medium |
| AGT-R09 | Accept | Delegation policy documented; sub-agent tracking in place | AI Governance | N/A | Low |
| AGT-R10 | Mitigate | Cryptographic identities; MFA; credential rotation[reference:29] | IAM | 15 Dec 2026 | Medium |
| AGT-R11 | Mitigate | Input sanitization; system prompt hardening; runtime filtering | Security | 15 Oct 2026 | Medium |
| AGT-R12 | Mitigate | Output filtering; DLP integration; privacy reviews | Privacy | 30 Nov 2026 | Medium |

---

## 5. Risk Acceptance

| Risk ID | Residual Risk | Acceptance Criteria | Approved By | Date |
|---------|---------------|---------------------|-------------|------|
| AGT-R09 | Low | Delegation policy documented; sub-agent tracking | Head of AI Governance | 1 Sep 2026 |

---

## 6. Overall Risk Assessment

| Metric | Value |
|--------|-------|
| **Total Risks Identified** | 12 |
| **Critical Risks** | 6 |
| **High Risks** | 6 |
| **Medium Risks** | 0 |
| **Low Risks** | 0 |
| **Residual Risk Rating** | Medium |
| **Risk Appetite Alignment** | ✅ Within appetite (with conditions) |

---

## 7. Signatories

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | Head of AI Governance | | |
| | CISO | | |
| | AI Governance Council Chair | | |
