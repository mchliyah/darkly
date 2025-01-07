# Exploit Description

In the `robots.txt` page, we can observe the following content:
```plaintext
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

### Step 1: Navigating to `/whatever`
When we navigate to `/whatever`, we find the following directory listing:
```plaintext
Index of /whatever/
../
htpasswd                                           29-Jun-2021 18:09                  38
```

### Step 2: Downloading `htpasswd`
The `htpasswd` file is downloadable and contains a username and hashed password:
```plaintext
root:437394baff5aa33daa618be47b75cb49
```

### Step 3: Decrypting the Hash
The hash is identified as MD5. After decrypting it, we retrieve the password:
```plaintext
qwerty123@
```

### Step 4: Finding the Admin Page
Using the `dirsearch` tool, we discover an admin page located at `/admin/index.php`.

### Step 5: Logging In
Testing the credentials `root:qwerty123@` on the admin page successfully grants access. Upon logging in, we retrieve the flag.

# How to Avoid This Vulnerability

To mitigate similar vulnerabilities, the following measures should be applied:

1. **Secure Sensitive Files:**
   - Ensure that files like `htpasswd` are not accessible to the public by configuring proper permissions and server rules.

2. **Restrict Access to Robots.txt Directories:**
   - The `Disallow` directives in `robots.txt` should not point to sensitive directories. Instead, sensitive directories should be inaccessible altogether through server-side configurations.

3. **Hashing and Storing Passwords Securely:**
   - Avoid using weak or outdated hashing algorithms like MD5. Use modern algorithms such as bcrypt or Argon2 for password hashing.

4. **Implement Directory Listing Restrictions:**
   - Disable directory listing on the server to prevent unauthorized access to file structures.

5. **Use Strong Authentication Practices:**
   - Enforce strong password policies and multi-factor authentication (MFA) for admin accounts.

6. **Perform Regular Security Audits:**
   - Periodically scan for publicly accessible sensitive files and directories.

By addressing these issues, organizations can significantly reduce the risk of similar exploits.