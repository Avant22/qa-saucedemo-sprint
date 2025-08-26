# Test Cases
| ID | Title | Pre-req | Steps | Expected |
|---|---|---|---|---|
| TC-01 | Login happy path | App reachable | Open site; enter standard_user/secret_sauce; click Login | Lands on inventory page |
| TC-02 | Login invalid shows error | App reachable | Enter user X / wrong pass; Login | Error banner displayed |
| TC-03 | Add item to cart | Logged in | Add Backpack to cart | Cart badge shows 1 |
| TC-04 | Remove item from cart | Item in cart | Open cart; remove item | Cart empty |
| TC-05 | Cart persists on refresh | Item in cart | Refresh inventory | Cart badge still 1 |
| TC-06 | Checkout requires info | Item in cart | Start checkout; continue empty | Validation errors shown |
| TC-07 | Checkout completes | Item in cart | Fill info; finish | Thank You message shown |
| TC-08 | Logout clears session | Logged in | Open menu; Logout | Back to login; inventory blocked |
| TC-09 | Locked out user blocked | App reachable | Use locked_out_user | Error shown |
| TC-10 | Price totals consistent | Item in cart | Proceed to overview | Item total + tax equals displayed total |
