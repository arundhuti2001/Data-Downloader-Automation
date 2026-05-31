import os
import requests

# =========================================================
# DIRECTORY STRUCTURE
# =========================================================

BASE_DIR = "AMFI_Data_2025_2026"

# Monthly folders
MONTHLY_DIR = os.path.join(BASE_DIR, "Monthly_Data")
MONTHLY_PDF_DIR = os.path.join(MONTHLY_DIR, "PDFs")
MONTHLY_EXCEL_DIR = os.path.join(MONTHLY_DIR, "Excels")

# Quarterly folders
QUARTERLY_DIR = os.path.join(BASE_DIR, "Quarterly_Data")
QUARTERLY_PDF_DIR = os.path.join(QUARTERLY_DIR, "PDFs")
QUARTERLY_EXCEL_DIR = os.path.join(QUARTERLY_DIR, "Excels")

# Create folders
os.makedirs(MONTHLY_PDF_DIR, exist_ok=True)
os.makedirs(MONTHLY_EXCEL_DIR, exist_ok=True)

os.makedirs(QUARTERLY_PDF_DIR, exist_ok=True)
os.makedirs(QUARTERLY_EXCEL_DIR, exist_ok=True)

# =========================================================
# MONTHLY DATA
# =========================================================

monthly_months = [
    ("apr", "2025"),
    ("may", "2025"),
    ("jun", "2025"),
    ("jul", "2025"),
    ("aug", "2025"),
    ("sep", "2025"),
    ("oct", "2025"),
    ("nov", "2025"),
    ("dec", "2025"),
    ("jan", "2026"),
    ("feb", "2026"),
    ("mar", "2026")
]

# =========================================================
# QUARTERLY DATA
# =========================================================

quarterly_files = [
    "aqu-vol25-issueI",
    "aqu-vol25-issueII",
    "aqu-vol25-issueIII",
    "aqu-vol25-issueIV"
]

# =========================================================
# BASE URL
# =========================================================

BASE_URL = "https://portal.amfiindia.com/spages/"

# =========================================================
# DOWNLOAD FUNCTION
# =========================================================

def download_file(url, filepath):

    try:

        response = requests.get(url, timeout=60)

        if response.status_code == 200:

            with open(filepath, "wb") as file:
                file.write(response.content)

            print(f"Downloaded: {filepath}")

        else:

            print(f"Not Found: {url}")

    except Exception as e:

        print(f"Error downloading: {url}")
        print(e)

# =========================================================
# DOWNLOAD MONTHLY FILES
# =========================================================

print("\nDOWNLOADING MONTHLY FILES...\n")

for month_code, year in monthly_months:

    # Original filenames
    pdf_filename = f"am{month_code}{year}repo.pdf"
    xls_filename = f"am{month_code}{year}repo.xls"

    # URLs
    pdf_url = BASE_URL + pdf_filename
    xls_url = BASE_URL + xls_filename

    # Save paths
    pdf_path = os.path.join(
        MONTHLY_PDF_DIR,
        pdf_filename
    )

    xls_path = os.path.join(
        MONTHLY_EXCEL_DIR,
        xls_filename
    )

    # Download
    download_file(pdf_url, pdf_path)
    download_file(xls_url, xls_path)

# =========================================================
# DOWNLOAD QUARTERLY FILES
# =========================================================

print("\nDOWNLOADING QUARTERLY FILES...\n")

for file_code in quarterly_files:

    # Original filenames
    pdf_filename = f"{file_code}.pdf"
    xls_filename = f"{file_code}.xls"

    # URLs
    pdf_url = BASE_URL + pdf_filename
    xls_url = BASE_URL + xls_filename

    # Save paths
    pdf_path = os.path.join(
        QUARTERLY_PDF_DIR,
        pdf_filename
    )

    xls_path = os.path.join(
        QUARTERLY_EXCEL_DIR,
        xls_filename
    )

    # Download
    download_file(pdf_url, pdf_path)
    download_file(xls_url, xls_path)

print("\nALL FILES DOWNLOADED SUCCESSFULLY")