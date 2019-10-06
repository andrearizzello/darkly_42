# Vulnerability

Go to the feedback page with `Leave a feedback` button at the bottom of the page:
`http://<IP>/?page=feedback`

Inside the form enter a script:
```
<SCRIPT>alert("42")</SCRIPT>
```
Then submit... and get the flag

# Protection

- Escape all user input
- Whitelisting input validation

# Source 

http://breakthesecurity.cysecurity.org/2012/02/complete-cross-site-scriptingxss-cheat-sheets-part-1.html
