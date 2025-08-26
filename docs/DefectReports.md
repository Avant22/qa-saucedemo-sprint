# Defects
## BUG-001
Title: Cart badge not clearing after removing last item
Severity: Medium  Priority: P2
Env: Chromium headless, macOS
Steps: Add one item; open cart; remove; observe badge
Expected: Cart badge disappears
Actual: Badge shows 1
Status: Fixed in latest

## BUG-002
Title: Checkout allows blank postal code when autofill toggled
Severity: High  Priority: P1
Env: Chromium
Steps: Add item; checkout; toggle autofill; continue
Expected: Postal code required
Actual: Order advances
Status: Deferred with mitigation

## BUG-003
Title: Error banner text overlaps logo on 320px width
Severity: Low  Priority: P3
Env: Chrome device toolbar, iPhone SE
Steps: Invalid login on narrow width
Expected: Banner wraps without overlap
Actual: Overlap occurs
Status: Open
