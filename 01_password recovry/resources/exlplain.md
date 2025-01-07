# Flag Documentation: Sign In / Forget Password Flag

## Challenge Overview
This challenge involves exploiting a hidden input field in the "Forget Password" functionality of a website to reveal a hidden flag. The breach leverages client-side manipulation to bypass the expected workflow.

## Tools Needed
- Browser Developer Tools (DevTools)

## Steps to Solve

1. **Initial Observation**:
   - Navigated to the **Sign In** page and clicked on the "Forget My Password" link.
   - This action redirected to a new page with a submit button but no input field to enter an email address.

2. **Reconnaissance**:
   - Opened the browser's Developer Tools (usually accessible via `F12` or `Ctrl+Shift+I`) to inspect the HTML structure of the page.
   - Identified a hidden input field for the email address in the HTML code.

3. **Exploitation**:
   - Edited the hidden input field in the HTML code using DevTools to change the email address to a different value.
   - Reloaded the page after making the changes.

4. **Flag Extraction**:
   - After reloading the page, the hidden flag appeared:
     ```
     1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
     ```

## How to Avoid This Breach in a Website
1. **Server-Side Validation**: Always validate input data server-side, regardless of client-side behavior. Never trust client-side data.
2. **Avoid Sensitive Data in Hidden Inputs**: Never store sensitive data such as flags or critical logic in hidden input fields or client-side scripts.
3. **Minimize Client-Side Trust**: Design your application logic to rely on secure server-side operations rather than client-side inputs.
4. **Use Secure Coding Practices**: Apply frameworks and tools that help enforce secure defaults for input handling.
5. **Conduct Regular Security Audits**: Test your application using penetration testing tools to identify and patch vulnerabilities like hidden field tampering.


