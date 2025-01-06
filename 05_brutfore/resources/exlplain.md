# Exploit: Brute Force Attack on Login Page

## Description
A brute force attack is a trial-and-error method used to crack passwords, encryption keys, or login credentials. In this attack, an automated program systematically tries every possible combination of characters until it finds the correct one.

### Case Example
1. Target Page: 
http://10.14.60.12/index.php?page=signin


2. Method:
- Gathered a list of the 50 most commonly used passwords from internet resources.
- Used a script (`script.sh`) to automate password attempts with the usernames `admin` or `root`.
- The script continuously tested combinations until the correct password was found.

3. Script Used:
Refer to `script.sh` for the implementation details.

## How to Avoid

### 1. Use Strong Passwords
- Avoid weak passwords such as repetitive characters (e.g., `AAAA`, `bbbb`, `1234`).
- Include a mix of uppercase, lowercase, numbers, and special characters.
- Use passwords with a minimum length of 12 characters.

### 2. Implement Account Lockouts
- After a certain number of failed login attempts, temporarily lock the account or require a CAPTCHA.

### 3. Use Multi-Factor Authentication (MFA)
- Require an additional authentication factor, such as a code sent to a mobile device or an authenticator app.

### 4. Monitor and Block Suspicious IPs
- Detect and block IPs showing suspicious behavior, such as making multiple login attempts in a short timeframe.

### 5. Rate Limiting
- Limit the number of login attempts within a specific period to reduce brute force effectiveness.

### 6. Regular Security Audits
- Periodically review and test the application's defenses against brute force attacks.
