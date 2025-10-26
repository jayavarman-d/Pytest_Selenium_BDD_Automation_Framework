# Pytest Selenium BDD Automation Framework

A lightweight, maintainable automation framework built with PyTest, Selenium WebDriver, and pytest-bdd (Gherkin-style BDD). Designed to help QA engineers and developers write readable, reliable end-to-end UI tests using the Page Object Model (POM) and BDD feature files.

---

Contents
- Overview
- Features
- Prerequisites
- Installation
- Configuration
- Running tests
- Reporting
- Project structure
- Writing tests (BDD + POM)
- Debugging & troubleshooting
- Contributing
- License
- Contact

---

Overview
========
This repository provides a template automation framework combining:
- PyTest as the test runner
- Selenium WebDriver for browser automation
- pytest-bdd for Gherkin-style BDD feature files
- Page Object Model for maintainable UI interactions
- Support for headless runs, environment-based configuration, and CI integration

Use this project as a starting point for functional and acceptance testing of web applications.

Features
========
- BDD-style test scenarios using .feature files (pytest-bdd)
- Page Object Model organization for locators and interaction methods
- Config-driven (env vars / config files) test execution
- Cross-browser support (Chrome, Firefox) and headless mode
- Test reports (pytest-html / other reporters)
- Example tests and reusable fixtures for setup/teardown
- Easily integrable with CI (GitHub Actions / Jenkins / GitLab CI)

Prerequisites
=============
- Python 3.8+
- pip
- Google Chrome / Mozilla Firefox (if running non-headless locally)
- Recommended: virtualenv or venv

Optional
- webdriver-manager (to auto-download drivers) or ensure browser driver binaries exist on PATH
- Allure for advanced reporting (optional)

Installation
============
1. Clone the repository:
   git clone https://github.com/jayavarman-d/Pytest_Selenium_BDD_Automation_Framework.git
   cd Pytest_Selenium_BDD_Automation_Framework

2. Create and activate a virtual environment:
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

(If requirements.txt is not present in this template, typical packages include:
pytest, selenium, pytest-bdd, webdriver-manager, pytest-html, python-dotenv)

Configuration
=============
Configuration can be provided via environment variables or a config file (project conventions may vary). Common environment variables used by the framework:

- BASE_URL - Base URL of the AUT (Application Under Test)
- BROWSER - Browser to use (chrome, firefox). Default: chrome
- HEADLESS - true/false (run browser headless). Default: false
- IMPLICIT_WAIT - implicit wait time in seconds (optional)
- SELENIUM_HUB - URL for a remote WebDriver (Selenium Grid) if applicable
- ENV - test environment name (dev, qa, staging)

Example using environment variables:
# macOS / Linux
export BASE_URL="https://example.com"
export BROWSER="chrome"
export HEADLESS="true"
pytest -q

Or using a .env file (if python-dotenv is used):
BASE_URL=https://example.com
BROWSER=chrome
HEADLESS=true

Running tests
=============
Run the whole test suite:
pytest

Run tests with verbosity and generate an HTML report:
pytest -q --html=reports/report.html --self-contained-html

Run a specific feature file:
pytest tests/features/my_feature.feature -q

Run tests matching a marker (e.g., smoke):
pytest -m smoke

Run tests in headless Chrome (example):
export HEADLESS=true
pytest -q

Notes:
- The exact pytest command-line options depend on how pytest.ini or conftest.py is set up in this project.
- Use pytest -k <expression> to select tests by substring matching on test names.

Reporting
=========
- pytest-html: generate a single-file HTML report using --html=reports/report.html
- Allure (optional): use allure-pytest to produce rich reports; requires installing allure commandline and running:
  pytest --alluredir=allure-results
  allure serve allure-results

Project structure (example)
===========================
The repository follows a modular layout. Your repo may vary slightly — adapt as needed.

- features/                     # BDD feature files (.feature)
  - login.feature
- tests/                        # pytest tests (often glue between feature files & steps)
  - steps/                      # step definitions for pytest-bdd
    - test_login_steps.py
- pages/                        # Page Object Model classes
  - base_page.py
  - login_page.py
- drivers/                      # optional local driver binaries or driver helper code
- utils/                        # helper utilities (waits, common assertions)
- config/                       # configuration files or environment profiles
- reports/                      # test output (reports, screenshots)
- conftest.py                   # pytest fixtures (driver setup, env config)
- pytest.ini / tox.ini          # pytest or test runner configuration
- requirements.txt              # pip dependencies

Writing tests (BDD + POM)
=========================
1. Feature file (Gherkin)
Feature: Login
  Scenario: Valid user can login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard

2. Step definition (pytest-bdd)
- Implement steps in tests/steps/ that call POM methods.
- Use conftest.py fixtures to provide the WebDriver instance (driver) to steps.

3. Page objects
- Keep locators and page methods in pages/*.py
- Example:
class LoginPage(BasePage):
    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

Best practices
==============
- Keep tests small and focused on behavior
- Prefer explicit waits (WebDriverWait) over sleeps
- Use environment variables for secrets and environment-specific data
- Reuse fixtures and utilities; avoid duplication
- Store test data separately (fixtures, JSON, YAML)

Debugging & troubleshooting
=========================
- If tests fail due to locator changes, update the page object locator.
- For driver/version issues, use webdriver-manager or ensure driver matches browser version.
- Collect screenshots on failure via a pytest fixture (attach to report).
- Increase logging to debug issues:
  pytest -o log_cli=true -o log_cli_level=INFO

CI Integration
==============
- Add GitHub Actions or another CI pipeline to run pytest on PRs and pushes.
- Typical steps:
  - Set up Python and required browsers
  - Install dependencies
  - Run pytest and publish reports/artifacts
- Store secrets (like BASE_URL, credentials for test accounts) in CI secrets and not in repo.

Contributing
============
- Fork the repo
- Create a topic branch: git checkout -b feature/my-change
- Make your changes and add tests
- Ensure tests pass locally
- Open a pull request with a clear title and description

Please follow repository-specific contributing guidelines if present.

License
=======
Specify your project's license here (e.g., MIT, Apache-2.0). If none included, add a LICENSE file.

Contact
=======
Maintainer: jayavarman-d
GitHub: https://github.com/jayavarman-d

Acknowledgements
================
This template is inspired by common open-source test automation patterns and best practices for PyTest + Selenium + BDD frameworks.
