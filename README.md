# 🧪 Selenium Python Automation Framework

A scalable and maintainable UI automation framework built using **Python, Selenium WebDriver, Pytest**, and **Page Object Model (POM)** design pattern.

---

## 🚀 Features

* ✅ Page Object Model (POM) design
* ✅ Pytest-based test execution
* ✅ Data-driven testing (CSV support)
* ✅ HTML test reports
* ✅ Headless execution support (CI ready)
* ✅ GitHub Actions integration (CI/CD)
* ✅ Reusable utilities (driver factory, data reader, etc.)

---

## 📁 Project Structure

```
selenium-framework/
│
├── pages/                # Page Object classes
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/                # Test cases
│   └── test_login.py
│
├── utils/                # Utilities (data reader, helpers)
│   └── data_reader.py
│
├── data/                 # Test data files
│   └── login_data.csv
│
├── reports/              # Test reports
│   └── report.html
│
├── conftest.py           # Pytest fixtures (driver setup)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running Tests

### Run all tests

```
pytest -v
```

### Run with HTML report

```
pytest -v --html=reports/report.html --self-contained-html
```

---

## 📊 Test Reports

* HTML reports are generated inside the `reports/` folder
* Open `report.html` in browser to view results

---

## 📄 Data-Driven Testing

Test data is stored in CSV format:

```
data/login_data.csv
```

Easily scalable to support multiple test scenarios.

---

## ⚡ CI/CD Integration

This framework supports **GitHub Actions** for continuous integration.

* Tests run automatically on every push
* Reports are uploaded as artifacts

Workflow file:

```
.github/workflows/ci.yml
```

---

## 🧠 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Pytest-HTML
* GitHub Actions

---

## 🔥 Future Improvements

* ✅ Allure Reporting integration
* ✅ Parallel test execution
* ✅ Cross-browser testing
* ✅ Docker support
* ✅ API + UI combined framework

---

## 🤝 Contributing

Feel free to fork the repo and raise pull requests.

---

## 📌 Author

**Vipul**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
