# OLoader
OLoader will offload containers from nodes if there are less HTTP requests and stops the instance if there are no active containers running ̶. down-scaling. 
Besides, it loads containers to the existing nodes if there are more requests, and If a node is running more than eight containers it will create a new virtual machine instance. 
What I am trying to do is, to iteratively put containers in a ship until it gets full (until a ship has 8 containers). 
If the ship is full, I will call another ship for the rest of the containers. 
Moreover, if a container in the ship is empty, I will make the ship inactive since it is costly to keep it. It’s all about loading and offloading containers to and from a ship.
