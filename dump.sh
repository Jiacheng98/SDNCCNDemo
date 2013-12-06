tcpdump -i h$1-eth0 -w h$1.pcap
# -s200 'udp && !icmp'