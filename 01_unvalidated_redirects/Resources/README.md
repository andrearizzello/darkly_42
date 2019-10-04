# Vulnerability

Found url on main page: `http://10.11.200.146/index.php?page=redirect&site=facebook`
Accessed on the main page by clicking the Facebook social icon at the bottom
Replace `facebook` of `site` attribute

# Exploit

It allows the user to potentially navigate through the website files, render files, send malicious script
The backend processes the user input which can be malicious.

# Protection

The backend here generates url following the user click
Avoid processing user input whenever possible and always sanitize it
Links are external and must be static

