'''

'By' Locators in Selenium

| Locator                | Usage                    | Example                                                       |
| ---------------------- | ------------------------ | ------------------------------------------------------------- |
| `By.ID`                | Find element by `id`     | `driver.find_element(By.ID, "username")`                      |
| `By.NAME`              | Find element by `name`   | `driver.find_element(By.NAME, "password")`                    |
| `By.XPATH`             | Find element using XPath | `driver.find_element(By.XPATH, "//input[@type='text']")`      |
| `By.LINK_TEXT`         | Find anchor text         | `driver.find_element(By.LINK_TEXT, "Login")`                  |
| `By.PARTIAL_LINK_TEXT` | Partial anchor text      | `driver.find_element(By.PARTIAL_LINK_TEXT, "Log")`            |
| `By.TAG_NAME`          | Find element by tag      | `driver.find_element(By.TAG_NAME, "input")`                   |
| `By.CLASS_NAME`        | Find element by class    | `driver.find_element(By.CLASS_NAME, "btn-primary")`           |
| `By.CSS_SELECTOR`      | CSS selector             | `driver.find_element(By.CSS_SELECTOR, "input[name='email']")` |

Always try ID → Name → CSS first.

Only use XPath when no other reliable locator exists.

Avoid using index-based locators because DOM changes break the script.

| Priority | Locator                           | Notes                            |
| -------- | --------------------------------- | -------------------------------- |
| 1        | **ID**                            | Fastest, unique, most reliable   |
| 2        | **Name**                          | Good if unique                   |
| 3        | **CSS Selector**                  | Flexible, fast                   |
| 4        | **Class Name**                    | Only if unique                   |
| 5        | **Link Text / Partial Link Text** | For anchor links                 |
| 6        | **Tag Name**                      | Rarely alone, mostly with parent |
| 7        | **XPath**                         | Powerful but brittle, slow       |

'''