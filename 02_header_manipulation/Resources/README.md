# Vulnerability

In code source of page : http://<IP>/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c 
To access this page click on `© BornToSec` button at the bottom of the main page

Found some comment :
```
You must coming from : "https://www.nsa.gov/" to go to the next step
```
and
```
Let's use this browser : "ft_bornToSec". It will help you a lot.
```

So we need to edit HTTP get request header of the current page.
add: `Referer = https://www.nsa.gov/`
add: `User-Agent = ft_bornToSec`

# Protection

Do not put hints for hackers in HTML pages because these are public


