'''
Created on Feb 18, 2013

@author: NamNX
'''

import socket, sys, signal,datetime

UDP_IP = "127.0.0.1"
UDP_PORT = 5555

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
#        myFile.close()
        sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
now = datetime.datetime.now() #current date time
#myFile = open('server_log %s.txt' %now.strftime("%Y-%m-%d %H:%M:%S"), 'w') 

if __name__ == '__main__':

    if (len(sys.argv)>1): 
        UDP_PORT = int(sys.argv[1])
    print "UDP server listen at", UDP_PORT
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(("", UDP_PORT))


    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        #addr tuple (ip, port)
        #string 1:nam1 -> reply 2:nam1:nam1_data        
#        print "received message:", data
#        myFile.write('received requests for %s\n' %data)
        rep = "2:" + data[:] + ":"+ data[:] + "_data"
        #print "rep:", rep        
#        sock.sendto(rep, (addr[0], addr[1]))
        


    
    
    
    