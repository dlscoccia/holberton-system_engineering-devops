# 0x19. Postmortem :coffin:

![pmmeme](https://memegenerator.net/img/instances/75063675.jpg)

## Issue Summary :ledger:

At the morning of 6th February we started getting tickets from users reporting that that the service of out web page was returning them an error indicating an empty reply from the server instead of the content they were asking for. This was from one of our servers hosted with apache, that quering with curl we noticed that was replying curl: (500) Server error code.
After checking the container with that service we detected the apache2 server was suddendly stopped.
___
## Timeline :hourglass_flowing_sand:
| Time | Description |
| ----------- | ----------- |
| 9:54AM | Got the first ticket reporting an issue on the service |
| 9:58AM | Peak of tickets from users getting error from server|
| 10:06AM | First check on the service returning an error status 500 |
|10:08AM | DevOps team was notified |
| 10:12AM | Routine for checking all servers status started |
| 10:18AM | The server with no response was detected |
| 10:20AM | Detected container was down and was restored |
| 10:24AM | Started trials on container |
| 10:28AM | Detected apache2 server status down |
| 10:30AM | Apache2 service restored |
| 10:33AM | Service from server down fully restored |
| 10:34AM | Started recheck for all servers status |
| 10:42AM | All servers running normally |
| 10:51AM | Detected the issue was caused due an electric failure and system rebooted|

![electric_cat](https://media.tenor.com/images/7e66c03228861fe6178e593e3f02a39b/tenor.gif)
___
## Root Cause :trollface:
After a electrical power failure on the data center the server was rebooted, and without having a automated protocol for this situations the service of apache2 wasn’t able to start unless it was started manually. Therefore every request made by the users after the shutdown was inevitably returning an error for any query.. 
___
## Resolution and recovery :adhesive_bandage:
To solve this issue was necessary to run the docker image, and manually start the apache2 web server. After that, we rechecked the status using a curl instruction and server was responding OK to queries.
___
## Corrective and Preventative Measures :hammer_and_wrench:
In order to prevent any other problem related to this root cause, we recommend to apply the following:

* Setup a alert trigger to detect changes on the voltages of the servers and send an email to DevOps team when needed.
* Setup an script on boot that automatically starts the servers service.
* Setup a runtime script that periodically check
the status of all servers and send an alert when one o more services are failing.