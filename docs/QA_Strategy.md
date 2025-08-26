Title: Sprint QA Strategy – SauceDemo Checkout Flow
Objective: Validate core ecommerce flow: login, add-to-cart, checkout, and order confirmation. Demonstrate test design, execution, defect tracking, and release readiness.
Scope: Functional UI, negative testing, cross-browser sanity (Chromium by default), basic accessibility smoke via focus and tab order checks.
Out of Scope: Load testing, security, localization, mobile native coverage.
Risks: Demo credentials rate limits, UI timing flakiness, environment instability.
Test Levels: Unit (dev-owned), UI functional (QA), smoke accessibility, regression of critical paths.
Environments: Public demo site on latest Chrome.
Entry Criteria: Target reachable, credentials available, baseline smoke green.
Exit Criteria: All Critical/High defects closed or deferred with sign-off, regression checklist green, automation green.
Reporting: Daily status note in README or project board, defects logged in DefectReports.md, release signoff in ReleaseSignoff.md.
