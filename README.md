# depth-slave
A smol daemon for reading from the bar30 depth sensor.

# USE ME
Depth-slave listens for a TCP socket connection on localhost port 8083.

Upon connection, sending a one letter command through the socket will yield a response from `depth-slave` according to the following table

command character | response
:---: | :---
`P` | pressure in millibars
`p` | pressure - offset in millibars
`D` | depth in meters based on pressure
`d` | depth in meters based on pressure minus offset
`Z` | set current pressure as offset (like zeroing depth)