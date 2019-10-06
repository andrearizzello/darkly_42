# Vulnerability

The website has a cookie `I_am_admin` to identify the admin user

`I_am_admin` value is set to false:
[md5] 68934a3e9455fa72420237eb05902327 = FALSE

Change the cookie to true
[md5] b326b5062b2f0e69046810717534cb09 = TRUE

# Exploit

- Making use of this vulnerability, an attacker can hijack a session, gain unauthorized access to the system which allows disclosure and modification of unauthorized information.
- The sessions can be high jacked using stolen cookies or sessions using XSS.

## More details: potentially vulnerable objects for session management and authentication

- Session IDs exposed on URL can lead to session fixation attack.
- Session IDs same before and after logout and login.
- Session Timeouts are not implemented correctly.
- Application is assigning same session ID for each new session.
- Authenticated parts of the application are protected using SSL and passwords are stored in hashed or encrypted format.
- The session can be reused by a low privileged user.

# Protection

- Cookies should be changed for each session and invalidated at the end.
- Never expose any credentials in URLs or Logs.
- Strong efforts should be also made to avoid XSS flaws which can be used to steal session IDs.

# Source 

https://www.guru99.com/web-security-vulnerabilities.html#3
