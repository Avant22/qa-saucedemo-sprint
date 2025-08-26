Title: Sprint QA Portfolio – SauceDemo
Target: https://www.saucedemo.com
Objective: Demonstrate end-to-end QA for a realistic sprint: strategy, planning, manual tests, defect tracking, light automation, CI, and release sign-off.

Contents
1. docs/QA_Strategy.md
2. docs/TestPlan.md
3. docs/TestScenarios.md
4. docs/TestCases.md
5. docs/ExploratoryCharters.md
6. docs/DefectReports.md
7. docs/RegressionChecklist.md
8. docs/ReleaseSignoff.md
9. tests/ (Playwright automation, Python)
10. artifacts/ (screenshots, gifs, logs)
11. .github/workflows/ci.yml (CI pipeline)

How to run locally
1) python3 -m venv venv
2) source venv/bin/activate
3) pip install -r requirements.txt
4) playwright install
5) pytest -q --html=artifacts/report.html --self-contained-html

Automation scope
Login happy path and invalid login
Add-to-cart and checkout happy path

Ethics
Keep automation runs light and infrequent
Do not run load or performance tests against public demos

Evidence to capture
Manual test execution screenshots or gifs
At least two realistic defect reports with repro steps
HTML test report from pytest
