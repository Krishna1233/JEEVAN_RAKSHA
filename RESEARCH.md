# JEEVANRAKSHA
### Research, Problem Analysis & Solution Framework

**Buildathon Track:** CityFix  
**Project Category:** Civic Technology | Smart City Solutions  
**Product Vision:** Building Safer & Smarter Citie

## Independent Development

JEEVANRAKSHA was independently conceptualized and developed without any team support, through self-learning, individual effort, and hands-on implementation.

---

## 1. Executive Summary

JEEVANRAKSHA is a citizen-centric civic issue reporting and tracking platform designed to improve how local infrastructure and public-service problems are documented, organized, and monitored.

The platform addresses common civic challenges such as damaged roads, waterlogging, improper waste management, drainage problems, streetlight failures, and public safety concerns.

Its primary objective is to provide citizens with a structured digital interface for reporting issues, securely tracking submissions, and viewing aggregated civic information through a centralized dashboard.

## 2. Problem Statement

Urban and semi-urban communities experience recurring civic infrastructure and public-service issues. However, citizens may face difficulties in identifying appropriate reporting channels, maintaining complaint records, and understanding the progress of submitted complaints.

The absence of a simple, organized tracking experience can make civic issue monitoring less transparent and less accessible.

There is a need for a citizen-friendly digital solution that simplifies issue documentation and provides a structured way to monitor reported problems.

## 3. Identified Problem Areas

The project focuses on the following civic challenge categories:

- **Infrastructure:** Road damage, potholes and drainage issues.
- **Water Management:** Waterlogging and water supply problems.
- **Waste Management:** Garbage accumulation and sanitation concerns.
- **Public Utilities:** Streetlight failures and related service issues.
- **Public Safety:** Civic hazards that may require timely attention.

## 4. Proposed Solution

JEEVANRAKSHA provides a centralized digital platform where citizens can:

1. Submit civic issue reports through a structured form.
2. Receive a unique Ticket ID and private Access Code.
3. Track report status using secure verification.
4. View aggregated information through a public dashboard.
5. Identify report priority through a keyword-based assessment system.
6. Access relevant emergency and official information resources.

The platform is designed to make civic reporting more organized, accessible, and transparent.

## 5. Core Product Capabilities

| Module | Purpose |
|---|---|
| Civic Issue Reporting | Structured issue submission |
| Secure Report Tracking | Ticket ID and private Access Code verification |
| Smart Priority Engine | Rule-based keyword assessment |
| Civic Dashboard | Aggregated report visibility |
| Admin Panel | Authorized report review and status management |
| Emergency Help Center | Access to emergency information |
| Government Help Finder | Discovery of relevant official resources |

## 6. Technical Approach

JEEVANRAKSHA uses a lightweight, cloud-based application architecture.

- **Frontend & Application:** Python and Streamlit
- **Database:** Supabase with PostgreSQL
- **Backend Integration:** Supabase API
- **Security:** Private access-code hashing and database Row Level Security
- **Version Control:** GitHub
- **Deployment:** Streamlit Community Cloud

The application separates public dashboard information from private report-verification data and uses server-side database access for protected operations.

## 7. Privacy & Security Considerations

Privacy is an important design consideration.

- Private Access Codes are stored as SHA-256 hashes rather than plain text.
- Report tracking requires both Ticket ID and private Access Code.
- Database Row Level Security is enabled.
- Administrative access is password-protected.
- Public dashboard information is presented in aggregated form.
- Uploaded photos are currently preview-only and are not permanently stored.

Users should avoid uploading photographs containing unnecessary personal or sensitive information.

## 8. Research & Validation Methodology

This document presents an initial problem analysis based on the CityFix challenge scope and the civic problem categories addressed by the product.

The project has not yet completed a formal citizen survey, field study, or institutional validation. Accordingly, no survey statistics, user adoption figures, or verified impact claims are presented.

Future validation can include citizen interviews, usability testing, and pilot evaluation.

## 9. Current Limitations

The current implementation has the following limitations:

- Reports are not automatically submitted to government departments.
- Priority classification is rule-based and does not replace professional emergency assessment.
- Uploaded photographs are not permanently stored.
- Resource Matching forms are currently demonstration placeholders; real-time matching is not active.
- Government Help Finder assists with discovering information but does not guarantee official resolution.

## 10. Expected Outcomes

JEEVANRAKSHA aims to:

- Simplify the digital documentation of civic problems.
- Improve the visibility of submitted reports.
- Provide a more organized report-tracking experience.
- Support better understanding of recurring civic issue categories.
- Encourage responsible citizen participation.

These are intended outcomes, not yet independently measured results.

## 11. Future Development Roadmap

Potential future improvements include:

- Secure image storage with user consent.
- Map-based civic issue visualization.
- Verified integration with official reporting channels.
- Real-time resource matching.
- Multilingual accessibility improvements.
- Advanced analytics and trend monitoring.

## 12. Conclusion

JEEVANRAKSHA demonstrates how accessible digital technology can support more organized civic issue reporting and tracking.

By combining secure report verification, structured data management, priority assessment, and dashboard-based visibility, the project proposes a practical foundation for citizen-focused civic technology.

**JEEVANRAKSHA — Building Safer & Smarter Cities.**

---

*Developed as an independent project for the CityFix Buildathon. JEEVANRAKSHA is not an official government platform.*