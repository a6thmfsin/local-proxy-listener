# local-proxy-listener
Ment to be a tool that captues replay proxy requests on localhost:8088 when using tools like dirsearch etc.

But have had problems with it and seems like you can only use the tool on http:// websites, the idea came to my head when i started working on a tool
to captue requests and analyze them for Insecure Deserilization bugs on the go while browsing the website but due to Firefox high standards to
prevent MitM attacks ive failed, ive tried making my own CA-certs etc etc but wont get it to work. Maybe someone will get it to work. 
Even tho this wasnt the main tool i was working on but why not release it, as i wont work on it anymore, atleast for a long time and stick to using burpsuite as a replay proxy.

Start the local-proxy-listener0.py using Python3 and then run ex dirsearch and it will print out all requests in GET request format in stdout.
