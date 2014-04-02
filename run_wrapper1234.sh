#Script to execute Wrapper.
#Add forwarding entry from CCNx to Wrapper.
ccndc add / udp 127.0.0.1 8888;
#Browse to Wrapper folder
cd ../Wrapper/Debug;
./Wrapper -i h$1-eth0 -p 900$1
