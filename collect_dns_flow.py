# -*- coding:utf-8 -*-
import pyshark
import os
import subprocess
import time

pcapfile = '/home/liyucheng/workspace/stream/DNS.pcapng'
def collect_dns_stream():
    cap = pyshark.FileCapture(pcapfile, display_filter='dns')

    print dir(cap[0].dns)
'''
    i = 0dir(
    qry_domain_name = []
    for pkt in cap:
        if pkt.dns.qry_name:
            print ('DNS Request from %s: %s ' % (pkt.ip.src, pkt.dns.qry_name))
        elif pkt.dns.resp_name:
            print ('DNS Response from %s: %s ' % (pkt.ip.src, pkt.dns.resp_name))
        i += 1
'''
if __name__ == '__main__':
    collect_dns_stream()

