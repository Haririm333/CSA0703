# Computer Networks (CSA07) - Assessment Tool 2 Case Study

## 📌 Student Details
- **Student Name:** S Hariram 
- **Registration Number:** 1965260018
- **Section / Batch:** CSA0703_D
- **Course Code & Title:** CSA07 - Computer Networks

## 📖 Case Study Overview
**NimbusEdge Technologies Pvt. Ltd. - Network Outage Incident (March 2024)**

This repository contains the complete case study analysis for the NimbusEdge Technologies multi-site network outage. The analysis investigates four distinct routing protocol failures across the enterprise network and provides technical reasoning, root cause analysis, and solution designs.

### 🔍 Analyzed Network Segments
1. **Chennai HQ Campus (RIP v2):** Investigated the hop-count limitation (16 hops) causing silent route drops for the newly provisioned Delivery subnet.
2. **Regional Link (IGRP):** Analyzed the metric recalculation lag during a fiber degradation event, which caused severe convergence delays and high latency.
3. **Core Backbone (OSPF):** Traced a multi-area migration transcription error (Area ID mismatch) that resulted in failed neighbor adjacency and an undetected routing black hole.
4. **ISP Peering (BGP):** Evaluated an untested failover policy and `LOCAL_PREF` misconfiguration that prevented automatic traffic failover during a primary ISP fiber cut.

## Repository Structure
* `README.md` - This overview file.
* `Case_Study_Answers.pdf` / `.docx` - The final compiled answer document containing all technical reasoning, diagrams, and proposed solutions.

## 🛠️ Key Concepts Applied
- **Distance-Vector Routing:** RIP hop-count mechanics, IGRP composite metric formulas (bandwidth & delay).
- **Link-State Routing:** OSPF neighbor adjacency requirements, multi-area hierarchy, and SPF reconvergence.
- **Path-Vector Routing:** BGP path attribute selection (`LOCAL_PREF`, `AS-PATH`) and dual-ISP redundancy.
- **Network Troubleshooting:** Root cause analysis, change management validation, and silent route withdrawal detection.
