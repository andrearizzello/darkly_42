# Vulnerability

Directory traversal 

Map site:
```
python3 sitemap_generator.py > sitemap.txt
```

Get flag:
```
python3 get_flag.py
```

# Exploit

Directory traversal vulnerabilities allow attackers to access arbitrary files on your system. They tend to occur in older technology stacks, which map URLs too literally to directories on disk.
You need to be sure URLs describing file paths are safely interpreted, lest a hacker try to get access to sensitive files on your server.

# Protection

- Use a Content Management System
- Use Indirection: Each time a file is uploaded, construct a “friendly” name for this on your site, and when the file is accessed, perform a lookup in your data-store to discover the actual file path.
- Segregate Your Documents: Hosting documents on a separate file-server or file partition, or in cloud storage, is a good idea too.
- Sanitize Filename Parameters: If you insist on using raw file names, you need to sanitize the file names coming in from HTTP requests. The safest approach is to restrict filenames to a list of known good characters, and ensure that any references to files use only those characters.
- Run with Restricted Permissions: `chroot jail`

# Source 
git clone https://github.com/c4software/python-sitemap.git (Used to map the hidden part of the website)

run it with:
python3 main.py --domain http://<IP>/.hidden/ --output sitemap.xml --exclude 'href="../"'
