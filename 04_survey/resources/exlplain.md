# Exploit
1. On the survey page, inspect the HTML for the slots selection input fields.
2. The input fields allow any number to be entered as the value, which can manipulate the results.
   - For example, entering a large number like `999999` can cause the selected name to jump to the top of the list.
3. This behavior bypasses the intended survey methodology, which is supposed to limit the maximum value to 10.

# Patch
1. Validate input values strictly on the backend:
   - Ensure the values are within the allowed range, e.g., [0, 10].
   - Reject or sanitize inputs outside this range.
2. Restrict slot selection on the frontend as well, but rely primarily on backend validation to enforce rules.