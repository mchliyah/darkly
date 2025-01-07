# Exploit

When we navigate through the website, we can see the `page` variable in the GET method. We test with various values like `/` and `../../`. The website responds by trolling us. Why not test with something like:

```
x.x.x.x/?page=../../../../../../../../../../../etc/passwd
```

**here we go!** We got the flag:

```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
```

# how to avoid

Apply a whitelist filter on the `page` variable to block characters like `.` and `/`, as well as `%` to prevent directory traversal. For RFI vulnerabilities on PHP websites, disable `allow_url_open` and `allow_url_include` in the PHP configuration.
