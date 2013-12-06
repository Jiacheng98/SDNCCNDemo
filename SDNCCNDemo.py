'''
Created on Nov 4, 2013

@author: NamNX

'''

from mininet.net import Mininet
from mininet.topo import *
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from subprocess import call
import sys
import httplib,json, time

def add_topo_host(topo, id_host):
    topo.add_host('h%s' %str(id_host), mac='00:00:00:00:00:0%s' %str(id_host))

#build topology
def buildTopo():
    print 'init topology'
    namtopo=Topo()
#    h1 = add_topo_host(namtopo, 1)
    h1 = namtopo.addHost( 'h1', mac='00:00:00:00:00:01' )
    h2 = namtopo.addHost( 'h2', mac='00:00:00:00:00:02' )
    h3 = namtopo.addHost( 'h3', mac='00:00:00:00:00:03' )
#    h4 = namtopo.addHost( 'h4', mac='00:00:00:00:00:04' )
#    h5 = namtopo.addHost( 'h5', mac='00:00:00:00:00:05' )
#    h6 = namtopo.addHost( 'h6', mac='00:00:00:00:00:06' )
    
        
    
    
    s1 = namtopo.addSwitch( 's1' )
    s2 = namtopo.addSwitch( 's2' )
    s3 = namtopo.addSwitch( 's3' )

    # Add links Mbps, ms delay, 10% loss
#    linkopts = dict(bw=100, delay='5ms', loss=2, max_queue_size=1000, use_htb=True)
    linkopts = dict()

    # alternately: linkopts = {'bw':10, 'delay':'5ms', 'loss':10,
    # max_queue_size=1000, 'use_htb':True}

    print 'init link'
    namtopo.addLink( h1, s1, **linkopts)
#     namtopo.addLink( h2, s1, **linkopts)
    namtopo.addLink( h2, s2, **linkopts)
    namtopo.addLink( h3, s3, **linkopts)
    namtopo.addLink( s1, s2, **linkopts)
    namtopo.addLink( s1, s3, **linkopts)
    namtopo.addLink( s2, s3, **linkopts)
    
#    namtopo.addLink( h4, s1, **linkopts)
#    namtopo.addLink( h5, s2, **linkopts)
#    namtopo.addLink( h6, s3, **linkopts)
    
    return namtopo

#net = Mininet(controller=lambda name: RemoteController( name, defaultIP='127.0.0.1', port=6634), topo=SingleSwitchTopo(3), link=TCLink, switch=OVSKernelSwitch)
call("mn -c", shell=True)
 
call("sh /home/namnx/Downloads/Floodlight-0.9/start.sh > /home/namnx/Downloads/Floodlight-0.9/log.txt &", shell=True)
time.sleep(5)


net = Mininet(controller=lambda name: RemoteController( name, defaultIP='127.0.0.1', port=6634), topo=buildTopo(), link=TCLink, switch=OVSKernelSwitch)

#net = Mininet(controller=lambda name: RemoteController( name, defaultIP='127.0.0.1', port=6634), topo=LinearTopo(2), link=TCLink, switch=OVSKernelSwitch)




#Send traffic
def send_traffic(host):
    #get a random number in range
    print 'Generate traffic from %s to %s ' %(host.IP(),net.hosts[2].IP())                 
    host.cmd('python /home/namnx/workspace/PackGenPython/PackGen.py %s &' %net.hosts[2].IP())        

def server(host):
    #get a random number in range
    print 'Start content server %s ' %host.IP()                     
    host.cmd('python /home/namnx/workspace/PackGenPython/Server.py 5555 &')


def generate_traffic():
    #net.pingAll()#test pingall
    #i=0
    for host in net.hosts:
        send_traffic(host)

def start_ccnx():
    i=9001
    try:
        for host in net.hosts:
#             host.cmd('sysctl -w net.ipv4.ip_forward=1 &')
            host.cmd('export CCN_LOCAL_PORT=%s' %str(i))
            host.cmd('ifconfig %s-eth0 promisc' %host.name)
            host.cmd('ccndstart &')
            i+=1
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise    

def preinsert_path():
    try:
        i = 0
        for host in net.hosts:     
            host.cmd('ccndc add / udp 127.0.0.1 8888');            
            i+=1
            if i>2:
                break            
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise    



#===========================Static Flow Pusher Section================================
class StaticFlowPusher(object):

    def __init__(self, server):
        self.server = server

    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
    def getStats(self, sw):
        ret = self.rest_call_get_stats('GET', sw)
        if ret[2]!="":
            return json.loads(ret[2])
        else:
            print "Response getStats null", sw
            return ""
    
    def get_path(self, swA,pA,swB,pB ):
        ret = self.rest_call_find_route('GET',swA,pA,swB,pB)
        if ret[2]!="":
            return json.loads(ret[2])
        else:
            print "Response null", swA,pA,swB,pB
            return ""
    def get_server_attachpoint(self, ip ):
        ret = self.rest_call_find_device('GET',ip)
        if ret[2]!="":
            return json.loads(ret[2])
        else:
            print "Response null", ip
            return ""    
    

    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200

    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200

    def rest_call(self, data, action):
        path = '/wm/staticflowentrypusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
#         print ret
        conn.close()
        return ret
    def rest_call_find_route(self, action,swA,pA,swB,pB):
        path = '/wm/topology/route/%s/%s/%s/%s/json ' %(swA,pA,swB,pB)
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps({})
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
#         print ret
        conn.close()
        return ret
    
    def rest_call_find_device(self, action,ip):
        path = 'wm/device/?ipv4=%s ' %(ip)
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps({})
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
#         print ret
        conn.close()
        return ret
    def rest_call_get_stats(self, action, swId):
        path = '/wm/core/switch/%s/flow/json   ' %(swId)
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps({})
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
#         print ret
        conn.close()
        return ret
    
    
    
    
    #Set rule to switch
    
    def pushFlowToSwitch(self, sw, name, ip,dst):
        flow1 = {
        'switch':"%s" %sw,
        "name":"flow-%s" %name,
        "cookie":"0",
        "priority":"0",
        "ether-type":"0x0800", #Ethernet type ip4
        "protocol":"17", #UDP
        "src-ip":"10.0.0.%s" %sw,
        "dst-ip":"%s" %ip,
        "active":"true",
        "actions":"set-dst-mac=00:00:00:00:00:0%s,set-dst-ip=10.0.0.%s,set-dst-port=1234,output=%s" %(dst,dst,dst)
        }
        
        self.set(flow1)
    def pushFlowToSwitch1(self, sw, rule, action):
        flow1 = {
        'switch':"%s" %sw,
        "name":"flow-%s" %rule,
        "cookie":"0",
        "priority":"0",
        "ether-type":"0x0806", #Ethernet type
        #"protocol":"17", #UDP
        "src-ip":"10.0.0.1",
        "active":"true",
        "actions":"set-dst-mac=00:00:00:00:00:02,set-dst-ip=10.0.0.2,output=2"
        }
        
        self.set(flow1)
        
        
        
    def pushDefaultFlowToSwitch(self, sw, action):
        flow1 = {
        'switch':"%s" %sw,
        "name":"flow-default",
        "cookie":"0",
        "priority":"1",
        "ether-type":"0x0800", #Ethernet type
        "protocol":"17", #UDP
        "active":"true",
        "actions":"output=%s" %action
        }
        
        self.set(flow1)
        
        



pusher = StaticFlowPusher('127.0.0.1')











if __name__ == '__main__':
    

    net.start()
    #test ping
#    net.pingAll()
    call("sh ~/GIT/SDNCCNDemo/add_flow.sh", shell=True)
    
#     pusher.pushFlowToSwitch(1,1,"193.147.136.11",2)
#     pusher.pushFlowToSwitch(1,2,"18.12.155.124",3)
    #pusher.pushFlowToSwitch1(1,2,1)
    start_ccnx()
#    preinsert_path()
#    net.hosts[2].cmd('~/Downloads/workspace/Wrapper/Debug/wrapper ');
#    net.hosts[2].cmd('ccndc add / udp 127.0.0.1 8888');
    #start CCNx deamon
#    try:
#        net.hosts[0].cmd('/home/namnx/workspace/Wrapper/Debug/Wrapper h1-eth0 9001 10.0.0.3 1234 &')
#        net.hosts[1].cmd('/home/namnx/workspace/Wrapper/Debug/Wrapper h2-eth0 9002 10.0.0.3 1234 &')
#        net.hosts[2].cmd('/home/namnx/workspace/Wrapper/Debug/Wrapper h3-eth0 9003 10.0.0.6 9006 &')
#    except:
#        print "Unexpected error:", sys.exc_info()[0]
#        raise    
#    
#     try:
#         #net.hosts[0].cmd('sh run_wrapper1234.sh 1 &')
#         #net.hosts[1].cmd('sh run_wrapper1234.sh 2 &')
#         net.hosts[1].cmd('sh server.sh &')
#         #net.hosts[0].cmd('python Server.py 1234 &')
#         #net.hosts[1].cmd('python Server.py 1234 &')
#         #net.hosts[0].cmd('sh ping.sh &')
# #         net.hosts[1].cmd('sh ~/Downloads/mininet/custom/run_wrapper1234.sh 2 3 &')
# #        net.hosts[2].cmd('sh ~/Downloads/mininet/custom/run_wrapper.sh 3 6 &')
# #         net.hosts[1].cmd('sh ~/Downloads/mininet/custom/add_route_1234.sh 1 &')
#     except:
#         print "Unexpected error:", sys.exc_info()[0]
#         raise   
    

    
#    server(net.hosts[2])
#    send_traffic(net.hosts[0])
#    send_traffic(net.hosts[1])
    CLI(net)
    call(["killall", "Wrapper"])
    call("fuser -k 6634/tcp", shell=True)
    

    
    
        
    net.stop()    
    