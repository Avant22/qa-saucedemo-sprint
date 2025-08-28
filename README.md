# Sprint QA Portfolio – SauceDemo

Target: [https://www.saucedemo.com](https://www.saucedemo.com)  
Objective: Demonstrate end-to-end QA for a realistic sprint: strategy, planning, manual tests, defect tracking, light automation, CI, and release sign-off.

---

## 📂 Contents

1. docs/QA_Strategy.md  
2. docs/TestPlan.md  
3. docs/TestScenarios.md  
4. docs/TestCases.md  
5. docs/ExploratoryCharters.md  
6. docs/DefectReports.md  
7. docs/RegressionChecklist.md  
8. docs/ReleaseSignoff.md  
9. tests/ (Playwright automation, Python)  
10. artifacts/ (screenshots, gifs, logs, reports)  
11. .github/workflows/tests.yml (CI pipeline)  
12. Dockerfile (Dockerised test runner)  

---

## 🛠 Automation Scope

- Login happy path and invalid login  
- Add-to-cart and checkout happy path  

---

## 🚦 Ethics

- Keep automation runs light and infrequent  
- Do not run load or performance tests against public demos  

---

## 📸 Evidence to Capture

- Manual test execution screenshots or gifs  
- At least two realistic defect reports with repro steps  
- HTML test report from pytest  
- Screenshots & traces on automation failure  

---

## 🖥 Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m playwright install --with-deps
pytest -q --html=artifacts/report.html --self-contained-html
🐳 Running with Docker
bash
Copy code
docker build -t qa-sprint .
docker run --rm -v $(pwd)/artifacts:/app/artifacts qa-sprint
📊 CI/CD (GitHub Actions)
Runs tests in Chromium, Firefox, WebKit

Uploads HTML reports, screenshots, traces as artifacts

Builds & runs Docker image

Optional: sends Slack notifications on failures

📈 Extended Features
Parallel execution (pytest -n auto)

Allure reports support

API testing ready (tests/api/)

Performance testing ready (tests/load/)

Mobile emulation (--device="iPhone 12")

✨ Portfolio Value
This repo demonstrates a full QA engineer skillset:

Strategy & planning documentation (test plans, scenarios, defect reports)

End-to-end automation (UI, API, performance)

CI/CD pipelines with artifact management

Dockerised test runner

Professional test reporting