# Ecommerce Automation Testing Framework

## 1. Overview  
This repository contains an **end-to-end automation testing framework** developed for an eCommerce web application. The framework is implemented using **Python**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and reusability.  

The solution automates essential user journeys, including:  
- User authentication (Login & Registration)  
- Product browsing and selection  
- Shopping cart management  
- Checkout process  

The framework supports **HTML reporting** for detailed test results and is fully integrated with **Jenkins** for Continuous Integration and Continuous Delivery (CI/CD) pipelines.

---

## 2. Project Structure  

```
Ecommerce/
│
├─ pages/                     # Page Object Model classes
│   ├─ login.py               # Login page actions
│   ├─ register.py            # Registration page actions
│   ├─ product_page.py        # Product selection and details
│   ├─ view_cart.py           # Cart management actions
│   └─ checkout.py            # Checkout process actions
│
├─ tests/                     # Pytest test cases
│   ├─ test_login.py          # Login functionality tests
│   ├─ test_register.py       # User registration tests
│   └─ test_complete_purchase.py # End-to-end purchase flow tests
│
├─ requirements.txt           # Project dependencies
└─ README.md                  # Project documentation
```

---

## 3. Key Features  

- **Page Object Model (POM)** for a clean and modular architecture.  
- Automation of **critical eCommerce workflows**, including:
  - Login  
  - Registration  
  - Product selection  
  - Cart management  
  - Checkout  
- **Pytest** for structured and efficient test execution.  
- **HTML reporting** for comprehensive execution reports.  
- **Jenkins integration** for automated CI/CD test runs.  
- Clear separation between **page elements** and **test logic** to facilitate maintenance.

---

## 4. Future Enhancements  

- Expand test coverage to include edge cases and complex user flows.  
- Implement parallel test execution to optimize runtime.  
- Enhance reporting with additional analytics and real-time notifications.  
- Introduce Docker for containerized and environment-independent test execution.

---

## 5. Author  

**Solat Mehmood**  
QA Automation Engineer  

