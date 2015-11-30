# SDNCCNDemo
Video demo: https://www.youtube.com/watch?v=Picg9RHEie0


Require:
Mininet 2
ccnx-0.8.2
floodlight 0.9
ccnping

Instruction to replay the demo (Updated Nov 2015):

1. Start the controller Floodlight. 


2. Start the python script: sudo python SDNCCNDemo2.py
Default OpenFlow port is 6633. If you want to use another port, you will need to change the number in the script


3. Now mininet started. In the Mininet terminal, start the terminal of all hosts: xterm h1 h2 h3 h4 

4. For each host, start ccnd: source startccnx.sh $hostId. For example, on host 2 terminal: source startccnx.sh 2.
That script will change the CCN_LOCAL_PORT, and make a new instance of ccnd on each host.

5. Start the Wrapper on H1 H2

In H1 terminal: sh run_wrapper1234.sh 1
In H2 terminal: sh run_wrapper1234.sh 2



6. In H4 terminal, Start ccnpingserver:
ccnpingserver ccnx:/nam


7. In H3 terminal, add a static route from H3 to H1: ccndc add / udp 10.0.0.1 9001

8. In H3 terminal, ping for content name: ccnping ccnx:/nam





Contact: xuan-nam.nguyen@inria.fr




