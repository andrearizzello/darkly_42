# Vulnerability

On page `http://<IP>/index.php?page=recover`

Accessed by going to:
- sign in
- i forgot password

```
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

Change value by your email ...
Submit form and get flag

# Exploit

This attack can be performed by a malicious user who wants to exploit the application for their own benefit, or an attacker who wishes to attack a third-person using a Man-in-the-middle attack.

# Protection

Don't put sensitive data inside forms
Check and/or set the data in the backend

# Sources
- https://www.owasp.org/index.php/Web_Parameter_Tampering
