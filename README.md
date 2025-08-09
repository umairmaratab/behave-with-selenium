# 🛒 Selenium BDD Framework – E-commerce Automation

## 📌 Overview
This project is an **end-to-end automation framework** for testing an e-commerce application using:
- **Selenium WebDriver** for browser automation
- **Behave (BDD)** for writing human-readable scenarios
- **Page Object Model (POM)** for clean and maintainable code
- **Behave HTML Formatter** for rich test reports

It includes **4 core features**:
1. **Login** – Valid and invalid login scenarios.
2. **Cart** – Add/remove products from the cart.
3. **Checkout** – Complete the checkout process.
4. **Search & Filter** – Search products and apply sorting/filters.

---

## 📂 Project Structure
```
.
├── features/
│ ├── 001_login.feature
│ ├── 002_cart.feature
│ ├── 003_checkout.feature
│ ├── 004_search.feature
│ └── steps/
│ ├── login_steps_001.py
│ ├── cart_steps_002.py
│ ├── checkout_steps_003.py
│ ├── search_steps_004.py
├── pages/
│ ├── login_page_001.py
│ ├── search_page_004.py
│ ├── cart_page_002.py
│ └── checkout_page_003.py
├── environment.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone this repository:
```bash
git clone https://github.com/umairmaratab/behave-with-selenium.git
cd behave-with-selenium
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```
3. Install dependencies
``` pip install -r requirements.txt ```

4. Running the Tests
``` behave ```

5. Run a specific feature
``` behave features/001_login.feature ```

6. Run with a specific browser
```bash
behave -D browser=headless
behave -D browser=chrome
```
7. Reports 
Generate an HTML Report:
``` behave -f html -o report.html ```
