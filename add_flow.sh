#All port -> forward to port of Wrapper and CCNx
#curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-1", "cookie":"0", "priority":"0", "ingress-port":"2","active":"true", "actions":"output=1,set-vlan-id=2"}' http://localhost:8080/wm/staticflowentrypusher/json
#curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-2", "cookie":"0", "priority":"0", "ingress-port":"1","active":"true", "actions":"output=2,set-vlan-id=1"}' http://localhost:8080/wm/staticflowentrypusher/json
#curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-1", "cookie":"0", "priority":"0", "ingress-port":"2","active":"true", "actions":"output=1,set-vlan-id=2"}' http://localhost:8080/wm/staticflowentrypusher/json
#curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-2", "cookie":"0", "priority":"0", "ingress-port":"1","active":"true", "actions":"output=2,set-vlan-id=1"}' http://localhost:8080/wm/staticflowentrypusher/json


#curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-2", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true","ether-type":"0x0800", "protocol":"17", "dst-port":"1234", "actions":"set-dst-mac=00:00:00:00:00:01,set-dst-ip=10.0.0.1,set-dst-port=1234,output=2"}' http://localhost:8080/wm/staticflowentrypusher/json

curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-2", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true","ether-type":"0x0800", "protocol":"17", "dst-ip":"193.147.136.11","tos-bits":"0","actions":"set-dst-mac=00:00:00:00:00:01,set-dst-ip=10.0.0.1,set-dst-port=1234,output=2"}' http://localhost:8080/wm/staticflowentrypusher/json
curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-2", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true", "ether-type":"0x0800", "protocol":"17","dst-ip":"193.147.136.11","tos-bits":"1","actions":"set-dst-mac=00:00:00:00:00:02,set-dst-ip=10.0.0.2,set-dst-port=1234,output=2"}' http://localhost:8080/wm/staticflowentrypusher/json

#curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-2", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true","ether-type":"0x0800", "protocol":"17", "dst-ip":"193.147.136.11","actions":"set-dst-mac=00:00:00:00:00:01,set-dst-ip=10.0.0.1,set-dst-port=9001,output=2"}' http://localhost:8080/wm/staticflowentrypusher/json


#curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1-2", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true", "ether-type":"0x0800", "protocol":"17","dst-ip":"193.147.136.11","tos-bits":"0","actions":"set-dst-mac=00:00:00:00:00:02,set-dst-ip=10.0.0.2,set-dst-port=9002,output=2"}' http://localhost:8080/wm/staticflowentrypusher/json


#curl -d '{"switch": "00:00:00:00:00:00:00:02", "name":"flow-mod-2-2", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true","ether-type":"0x0800", "protocol":"17", "dst-ip":"193.147.136.11","tos-bits":"3","actions":"set-dst-mac=00:00:00:00:00:01,set-dst-ip=10.0.0.1,set-dst-port=1234,output=2"}' http://localhost:8080/wm/staticflowentrypusher/json