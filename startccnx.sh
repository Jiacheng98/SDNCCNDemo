#!/bin/sh
export CCN_LOCAL_PORT=900$1
ifconfig h$1-eth0 promisc
ccndstart &
