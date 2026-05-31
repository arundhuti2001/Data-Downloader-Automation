# Data-Downloader-Automation

## Overview

This project automates the collection and organization of monthly and quarterly reports published by the Association of Mutual Funds in India (AMFI).

The solution downloads PDF and Excel reports directly from the AMFI portal, automatically organizes them into structured folders, and creates a centralized repository for financial analysis, reporting, and research.

---

## Features

* Automated AMFI report downloads
* Monthly report collection
* Quarterly report collection
* PDF and Excel file support
* Automatic folder creation
* Organized directory structure
* Bulk file processing
* Error handling and download validation

---

## Technologies Used

* Python
* Requests
* OS Module

---

## Data Sources

* AMFI Monthly Reports
* AMFI Quarterly Reports
* Industry AUM Reports
* Mutual Fund Industry Statistics

---

## Workflow

1. Generate report URLs automatically.
2. Connect to the AMFI portal.
3. Download monthly PDF reports.
4. Download monthly Excel reports.
5. Download quarterly PDF reports.
6. Download quarterly Excel reports.
7. Organize files into structured directories.
8. Create a centralized financial data repository.

---

## Directory Structure

```text
AMFI_Data_2025_2026/
│
├── Monthly_Data/
│   ├── PDFs/
│   └── Excels/
│
├── Quarterly_Data/
│   ├── PDFs/
│   └── Excels/
│
└── main.py
```

---

## Installation

```bash
pip install requests
```

---

## Run

```bash
python main.py
```

---

## Output

The automation creates:

* Monthly PDF reports
* Monthly Excel reports
* Quarterly PDF reports
* Quarterly Excel reports

All files are automatically organized into dedicated folders for easy access and analysis.

---

## Business Applications

* Mutual Fund Research
* Asset Management Analytics
* Financial Data Collection
* Industry Trend Analysis
* Investment Research
* Regulatory Reporting
* Market Intelligence
* Data Engineering Pipelines

---

## Benefits

* Eliminates manual downloading
* Saves research time
* Creates a centralized report repository
* Supports automated reporting workflows
* Improves data availability for analysis
* Scalable for future reporting periods

---

## Future Enhancements

* Automated scheduling using Task Scheduler or Cron
* Email notifications for new reports
* Database integration
* Data warehouse ingestion
* Dashboard integration with Power BI or Tableau
* Automated report parsing and analytics

