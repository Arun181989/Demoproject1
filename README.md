# Selenium PyTest Automation Framework 🚀

This project is a **Python Selenium automation framework** built using **PyTest** and **Page Object Model (POM)**.  
It includes **navigation validation**, **data-driven testing**, **CI/CD integration with GitHub Actions**, and **HTML test reports**.

This framework is designed to demonstrate **real-world automation practices** used in IT companies.

---

## 🧰 Tech Stack

- **Language:** Python 3.x
- **Automation Tool:** Selenium WebDriver
- **Test Framework:** PyTest
- **Design Pattern:** Page Object Model (POM)
- **Data-Driven Testing:** CSV, Excel
- **CI/CD:** GitHub Actions
- **Reports:** PyTest HTML Report

---

## 📂 Project StructureDemoproject1/
Demoproject1/
├── .github/workflows/
│   └── pytest.yml
├── docs/
├── pages/
│   ├── base_page.py
│   ├── locators.py
│   ├── home_page.py
│   ├── contact_page.py
│   ├── courses_page.py
│   └── footer_page.py
├── tests/
│   ├── test_TC_HOME_01.py
│   ├── test_TC_NAV_01.py
│   ├── test_TC_COURSE_01.py
│   ├── test_TC_FORM_01.py
│   └── test_TC_FOOTER_01.py
├── utils/
│   ├── data_reader.py
│   └── performance_logger.py
├── data/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


---

## ✅ Features Implemented

✔ Home page validation  
✔ Navigation / Menu validation  
✔ Courses page validation  
✔ Contact form submission  
✔ Data-Driven Testing (CSV & Excel)  
✔ Screenshot capture on failure  
✔ HTML test report generation  
✔ CI/CD pipeline using GitHub Actions  

---
## ▶ How to Run the Tests Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Arun181989/Demoproject1.git
cd Demoproject1
2️⃣ Create & activate virtual environment
bash
Copy code
python -m venv .venv
.venv\Scripts\activate   # Windows
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run all tests
bash
Copy code
pytest
5️⃣ Run with HTML report
bash
Copy code
pytest --html=reports/automation_report.html --self-contained-html
📊 Test Reports
HTML reports are generated inside the reports/ folder

Screenshots are automatically captured for failed tests

Reports are excluded from Git using .gitignore

🔁 CI/CD with GitHub Actions
Tests run automatically on every push or pull request

Workflow file:
.github/workflows/pytest.yml

Ensures automation stability and regression safety

🧪 Data-Driven Testing
Contact form tests read data from:

contact_data.csv

contact_data.xlsx

Data reader utility handles multiple formats

📌 Notes
Some contact form submissions may redirect to error pages depending on site behavior

Such cases are intentionally validated to ensure site stability

👤 Author
Arun Prasad
Automation Test Engineer
📍 India


