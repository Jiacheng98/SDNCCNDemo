#Forward all CCN packets from port to Wrapper and CCNx of that switch


curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-1", "cookie":"0", "priority":"32768", "ingress-port":"2","active":"true", "ether-type":"0x0800", "protocol":"17","actions":"set-tos-bits=4,set-dst-mac=00:00:00:00:00:01,set-dst-ip=10.0.0.1,set-dst-port=9001,output=1"}' http://localhost:8080/wm/staticflowentrypusher/json;
curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-2", "cookie":"0", "priority":"32768", "ingress-port":"3","active":"true", "ether-type":"0x0800", "protocol":"17","actions":"set-tos-bits=8,set-dst-mac=00:00:00:00:00:01,set-dst-ip=10.0.0.1,set-dst-port=9001,output=1"}' http://localhost:8080/wm/staticflowentrypusher/json;



curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-1", "cookie":"0", "priority":"32768", "ingress-port":"2","active":"true", "ether-type":"0x0800", "protocol":"17","actions":"set-tos-bits=4,set-dst-mac=00:00:00:00:00:02,set-dst-ip=10.0.0.2,set-dst-port=9002,output=1"}' http://localhost:8080/wm/staticflowentrypusher/json;
curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-2", "cookie":"0", "priority":"32768", "ingress-port":"3","active":"true", "ether-type":"0x0800", "protocol":"17","actions":"set-tos-bits=8,set-dst-mac=00:00:00:00:00:02,set-dst-ip=10.0.0.2,set-dst-port=9002,output=1"}' http://localhost:8080/wm/staticflowentrypusher/json;


#From Wrapper towards the server


curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-3", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true", "ether-type":"0x0800", "protocol":"17","dst-ip":"193.147.136.11","actions":"output=2"}' http://localhost:8080/wm/staticflowentrypusher/json;

curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-4", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true", "ether-type":"0x0800", "protocol":"17","dst-ip":"18.12.155.124","actions":"output=2"}' http://localhost:8080/wm/staticflowentrypusher/json;

#WARNING: You will need to set new IP address if you use new name for ping!!! The ip address is calculated by hashed function. 
#The best way is to let the controller install a rule for each new name. 


curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-3", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true", "ether-type":"0x0800", "protocol":"17","dst-ip":"193.147.136.11","actions":"set-dst-mac=00:00:00:00:00:04,set-dst-ip=10.0.0.4,set-dst-port=9004,output=3"}' http://localhost:8080/wm/staticflowentrypusher/json;

curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-4", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true", "ether-type":"0x0800", "protocol":"17","dst-ip":"18.12.155.124","actions":"set-dst-mac=00:00:00:00:00:04,set-dst-ip=10.0.0.4,set-dst-port=9004,output=3"}' http://localhost:8080/wm/staticflowentrypusher/json;


