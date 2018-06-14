# depth-slave
A smol daemon for reading from the bar30 depth sensor.

# USE ME
Depth-slave listens for a TCP socket connection on localhost port 8083.

Upon connection, depth-slave will respond to certain one letter commands with their respective values. The one-letter commands are as follows:

command character | response
:---: | :---
`P` | pressure in millibars
`p` | pressure - offset in millibars
`D` | depth in meters based on pressure
`d` | depth in meters based on pressure minus offset
`Z` | set current pressure as offset (like zeroing depth)