# OWASP Agentic Top 10 2026 — Control Mapping

**Document ID:** AGENT-OWASP-2026-001  
**Date:** 1 September 2026  
**Version:** 1.0

---

## 1. Purpose

This document maps the OWASP Top 10 for Agentic Applications 2026 to controls in this framework[reference:36].

---

## 2. OWASP Agentic Top 10 2026

| Rank | Risk | Description | Framework Control |
|------|------|-------------|-------------------|
| **ASI01** | **Goal Hijacking** | Agent is manipulated to pursue malicious or unintended objectives[reference:37] | `03-controls/delegation-boundaries.md`<br>`03-controls/human-escalation-protocols.md` |
| **ASI02** | **Tool Misuse** | Agent uses tools or APIs in unauthorized ways[reference:38] | `03-controls/tool-access-policy.md`<br>`03-controls/execution-sandboxing.md` |
| **ASI03** | **Privilege Abuse** | Agent escalates its own permissions[reference:39] | `03-controls/identity-access-controls.md`<br>`03-controls/delegation-boundaries.md` |
| **ASI04** | **Excessive Agency** | Agent is given too much autonomy[reference:40] | `03-controls/delegation-boundaries.md`<br>`07-templates/agent-deployment-approval-form.md` |
| **ASI05** | **Memory Poisoning** | Agent's memory is corrupted with malicious data[reference:41] | `03-controls/execution-sandboxing.md`<br>`04-monitoring/agent-activity-logging.md` |
| **ASI06** | **Rogue Agent** | Unauthorized or compromised agent operates in the environment[reference:42] | `03-controls/identity-access-controls.md`<br>`04-monitoring/agent-activity-logging.md` |
| **ASI07** | **Cost Runaway** | Agent consumes uncontrolled resources | `04-monitoring/cost-runaway-detection.md`<br>`05-incident-response/agentic-incident-runbook.md` |
| **ASI08** | **Hallucination Cascade** | Agent makes decisions based on false information | `03-controls/human-escalation-protocols.md`<br>`04-monitoring/agent-activity-logging.md` |
| **ASI09** | **Delegation Escalation** | Agent delegates tasks to untrusted sub-agents | `03-controls/delegation-boundaries.md`<br>`07-templates/agent-passport-template.md` |
| **ASI10** | **Identity Spoofing** | Attacker impersonates a legitimate agent | `03-controls/identity-access-controls.md`<br>`03-controls/execution-sandboxing.md` |

---

## 3. Control Coverage Summary

| OWASP Risk | Covered By | Status |
|------------|------------|--------|
| ASI01 — Goal Hijacking | ✅ Full | Controls implemented |
| ASI02 — Tool Misuse | ✅ Full | Controls implemented |
| ASI03 — Privilege Abuse | ✅ Full | Controls implemented |
| ASI04 — Excessive Agency | ✅ Full | Controls implemented |
| ASI05 — Memory Poisoning | ✅ Full | Controls implemented |
| ASI06 — Rogue Agent | ✅ Full | Controls implemented |
| ASI07 — Cost Runaway | ✅ Full | Controls implemented |
| ASI08 — Hallucination Cascade | ✅ Full | Controls implemented |
| ASI09 — Delegation Escalation | ✅ Full | Controls implemented |
| ASI10 — Identity Spoofing | ✅ Full | Controls implemented |

---

## 4. Implementation Guidance

| OWASP Risk | Recommended Mitigation |
|------------|----------------------|
| ASI01 | Implement goal validation; human escalation for high-impact decisions |
| ASI02 | Implement tool access policy; runtime tool validation[reference:43] |
| ASI03 | Implement zero-trust identity; permission boundaries[reference:44] |
| ASI04 | Implement autonomy tiers; graduated deployment[reference:45] |
| ASI05 | Implement memory validation; periodic memory review |
| ASI06 | Implement agent inventory; continuous monitoring[reference:46] |
| ASI07 | Implement cost monitoring; spending limits |
| ASI08 | Implement output validation; human review |
| ASI09 | Implement delegation policy; sub-agent tracking |
| ASI10 | Implement cryptographic identities; MFA[reference:47] |

---

## 5. Signatories

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | Head of AI Governance | | |
| | CISO | | |
| | Security Architect | | |
