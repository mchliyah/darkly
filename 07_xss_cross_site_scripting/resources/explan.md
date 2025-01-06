# Exploit
1. Visit the URL: `/index.php?page=feedback`.
2. This page allows signing a guestbook and viewing messages from other users.
3. Attempt an XSS attack by injecting a script tag. However, the Web Application Firewall (WAF) filters out script tags.
4. Explore alternative tags that might not be blocked. For example, try using an SVG tag:
   ```html
   <svg/onload=alert('XSS')>a
This attempt reveals the flag: 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e.
Note: Further testing indicated some uncertainty about why the flag was obtained, but the exploit succeeded nonetheless.

# Avoid
Avoid displaying unsanitized user input directly.
When displaying user input is necessary, implement the following precautions:
Sanitize input by filtering out special characters or patterns, such as <svg*>.
Use escaping functions to neutralize potentially harmful input.