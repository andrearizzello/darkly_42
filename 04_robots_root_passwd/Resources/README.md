# Vulnerability

go to `http://<IP>/robots.txt` with file content :
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

go to `http://<IP>/whatever/` and download htpasswd with content
```
root:8621ffdbc5698829397d97767ac13db3
```

crack password with md5 hash
credentials are :
```
root:dragon
```

login at `http://<IP>/admin/` with these credentials

# Protection

Do not let sensitive information and files in web root directory
