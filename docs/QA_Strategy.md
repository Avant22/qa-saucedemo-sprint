# Sprint QA Strategy — SauceDemo Checkout/Login
## Objective
Validate the core e-commerce flows on https://www.saucedemo.com: login, add to cart, and checkout. Ensure functionality, basic UX sanity, and resilience to common negatives.

## Scope
Functional UI tests, negative tests, smoke regression, exploratory charters, defect taxonomy and triage notes.

## Risks
Auth state issues, flaky network, dynamic selectors, environment outages, browser differences.

## Test Levels
Unit (dev-owned), UI functional (QA), smoke regression (QA), basic accessibility smoke.

## Environments
Local Playwright with Chromium headless; target site at https://www.saucedemo.com.

## Entry Criteria
Stories in scope are defined, tests runnable locally, credentials available, no open P0s blocking smoke.

## Exit Criteria
All P0/P1 fixed or consciously deferred with sign-off; regression checklist green; report archived.

## Reporting
Daily notes in repo issues; automated HTML test report per run; release sign-off doc.
