# Vulnerability

Try a path traversal to access a file outside of the website scope
`http://<IP>/?page=../../../../../../../etc/passwd`

Then get the flag !

# Protection

- Don't store sensitive configuration files inside the web root
- Prefer working withouth user input when using file system calls
- Use chrooted jails and code access policies to restrict where the files can be obtained or saved to

# Source

- https://www.owasp.org/index.php/Path_Traversal
- https://www.owasp.org/index.php/File_System#Path_traversail
- https://unix.stackexchange.com/questions/105/chroot-jail-what-is-it-and-how-do-i-use-it
