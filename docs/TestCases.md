| ID | Title | Pre-req | Steps | Expected |
| TC-01 | Login valid user | Site reachable | Open site, enter valid creds, click login | Inventory page visible, no error |
| TC-02 | Login invalid user | Site reachable | Open site, enter bad creds, click login | Error message displayed |
| TC-03 | Locked user login | Site reachable | Enter locked_out_user, click login | Blocked message displayed |
| TC-04 | Add to cart | Logged in | Add first item | Cart badge increments |
| TC-05 | Remove from cart | Item in cart | Remove item | Cart badge decrements or disappears |
| TC-06 | View cart | Items added | Open cart | Items and price totals correct |
| TC-07 | Checkout happy path | Items in cart | Checkout, fill form, continue, finish | Confirmation displayed |
| TC-08 | Checkout missing fields | On checkout info | Leave required field blank | Inline validation message |
| TC-09 | Refresh during flow | Logged in | Refresh after adding to cart | State consistent or gracefully reset |
| TC-10 | Logout | Logged in | Open menu, logout | Back to login page |
