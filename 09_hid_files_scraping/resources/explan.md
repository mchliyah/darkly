# Exploit: Web Scraping of Sensitive Files in Hidden Directories

## Vulnerability
1. After conducting a subdirectory search, the `/robot.txt` file was discovered, revealing the path `/.hidden`.
2. This path contained numerous subdirectories, many of which had `README.md` files.
3. A Python script was used to iterate over these subdirectories, searching for and printing the contents of `README.md` files.
4. Upon examining the initial results, certain words were frequently found in these files. By excluding files containing these words, the script was optimized to focus on potentially sensitive information.
5. The final results were stored in a separate output file.

## Python Script
check the script "scrapy.py" in the resources folder
## Patch
To mitigate such exploits:

Avoid exposing sensitive paths like /robot.txt and /.hidden. Use proper access control mechanisms.
Prevent directory listing by disabling it in the web server configuration.
Use file permissions to restrict access to sensitive files.
Regularly audit your website for exposed files and paths.
Remove unnecessary or sensitive files from the server.
