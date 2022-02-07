#!/usr/bin/env python3

"""
Usage: python3 domain2ip.py subdomain-list.txt
"""

from ctypes import pydll
import nmap
import sys
import socket
import threading

##  Get the ports of the domain
def get_url(domain):
    nm = nmap.PortScanner()
    nm.scan(domain, arguments='--host-timeout 40s --max-retries 0 --data-length=50 -PS443,832,981,1010,1311,2083,2087,2095,2096,4712,80,8000,8080,8443')
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    if port == 443:
                        print('https://' + domain + '/')
                    elif port == 80:
                        print('http://' + domain + '/')
                    elif port == 832:
                        print('https://' + domain + ':832/')
                    elif port == 981:
                        print('https://' + domain + ':981/')
                    elif port == 1010:
                        print('https://' + domain + ':1010/')
                    elif port == 1311:
                        print('https://' + domain + ':1311/')
                    elif port == 2083:
                        print('https://' + domain + ':2083/')
                    elif port == 2087:
                        print('https://' + domain + ':2087/')
                    elif port == 2095:
                        print('https://' + domain + ':2095/')
                    elif port == 2096:
                        print('https://' + domain + ':2096/')
                    elif port == 4712:
                        print('https://' + domain + ':4712/')
                    elif port == 8000:
                        print('http://' + domain + ':8000/')
                    elif port == 8080:
                        print('http://' + domain + ':8080/')
                    elif port == 8443:
                        print('http://' + domain + ':8443/')

## Get the domains from the file
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 domain2url.py <file>')
        sys.exit(1)

## Get the arguments
    domains = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            domains.append(line.strip())

## if is not file
    if not domains:
        print('Usage: python3 domains2url.py <file>')
        sys.exit(1)

 
    for i in range(0, len(domains), 500):  ## Use 500 threads to speed up the process
        threads = []
        for domain in domains[i:i+500]: ## Use 500 threads to speed up the process
            t = threading.Thread(target=get_url, args=(domain,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()


if __name__ == '__main__':
    main()
