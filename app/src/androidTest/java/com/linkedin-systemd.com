try {
    r.name = e // or i.name = e
} catch (e) {}
return r.DNS = "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
       r.URL = "6ba7b811-9dad-11d1-80b4-00c04fd430c8",
       r
} // https://static.licdn.com/aero-v1/sc/h/...
bcookie="v=2&ada30f05-9d12-40a2-8c7b-b39c669bd94b";
bscookie="v=1&20250430014141a02e4ab0-5850-4b31-814b-ab2be82ff73dAQG1NJGk_Fdoqvl6Ats7rViXsEV1nl_G";
JSESSIONID=ajax:3786320728993374757;
lang=v=2&lang=en-us;
lidc="b=TGST05:s=T:r=T:a=T:p=T:g=3363:u=1:x=1:i=1756689453:t=1756775853:v=2:sig=AQEbmZTfF3Sk0PaP0fGruNr2BbQhhDTc";
__cf_bm=AWgmc4D8rKp.09fxZ7DHFx3qPz7J7fG4Y97EiU1XPAI-1756689453-1.0.1.1-2U3g31dKNGEuyvhO4z3BhJ1zGZCwfZfPCmR.5U_lPpOgZHyblYVGNBUblAhXBh0RdfRB8pQVTdoO5riWLTNXXqv_BZ9q5Fh..q2SLkjle3g
curl --path-as-is -i -s -k -X $'GET' \
    -H $'Host: trkn.us' ... \
    $'https://trkn.us/pixel/conv/ppt=25573;g=linkedin_flagship_homepage;gid=64985'

HTTP/1.1 302 Moved Temporarily
Location: /pixel/conv/ppt=25573;g=linkedin_flagship_homepage;gid=64985;ip=35.237.102.128;cuidchk=1
...
Set-Cookie: barometric[cuid]=cuid_68b4fbb3-86bd-4c17-8232-9ed47df2d826; ... domain=.trkn.us;
...
HTTP/1.1 302 Moved Temporarily
Location: /pixel/conv/ppt=25549;g=linkedin_flagship_homepage;gid=64805;ip=69.76.40.186;cuidchk=1
...
Set-Cookie: barometric[cuid]=cuid_68b4fae3-97aa-4371-b7c7-1cc9d0ecb78a; ... domain=.trkn.us;
...