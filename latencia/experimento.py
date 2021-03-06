#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
from mininet.node import OVSKernelSwitch, UserSwitch
import time
import sys

homedir = "/home/"+sys.argv[1]+"/versionado/experimentos_dissertacao/:/vol1"

print(homedir)

setLogLevel('info')

net = Containernet(controller=Controller)

info('*** Adding controller\n')
net.addController('c0')

info('*** Adding docker containers\n')
d0 = net.addDocker('d0', ip='10.0.0.250', volumes=[homedir], dimage="ubuntu_gstreamer", dcmd="/bin/bash")

# d2 = net.addDocker('d2', ip='10.0.0.252', volumes=["/home/battisti/versionado/alfa/docs/teste:/vol1"], dimage="ubuntu_gstreamer", dcmd="/bin/bash")

# d3 = net.addDocker('d3', ip='10.0.0.253', dimage="alpine_bash", dcmd="/bin/bash")

d1 = net.addDocker(
    'd1', 
    ip='10.0.0.251',
    dimage="alfa/vms/video_qrcode_detection", 
    dcmd="python /root/video_qrcode_detection/v2.py",
    ports=[(5000, 'udp')],
    publish_all_ports=True
    )

# d2 = net.addDocker(
#     'd2', 
#     ip='10.0.0.252',
#     dimage="alfa/vms/video_qrcode_detection", 
#     dcmd="python /root/video_qrcode_detection/v2.py",
#     ports=[(5000, 'udp')],
#     publish_all_ports=True
#     )

# d3 = net.addDocker(
#     'd3', 
#     ip='10.0.0.253',
#     dimage="alfa/vms/video_qrcode_detection", 
#     dcmd="python /root/video_qrcode_detection/v2.py",
#     ports=[(5000, 'udp')],
#     publish_all_ports=True
#     )

# d4 = net.addDocker(
#     'd4', 
#     ip='10.0.0.254',
#     dimage="alfa/vms/video_qrcode_detection", 
#     dcmd="python /root/video_qrcode_detection/v2.py",
#     ports=[(5000, 'udp')],
#     publish_all_ports=True,
#     cpuset_cpus="2"
#     )

# d5 = net.addDocker(
#     'd5', 
#     ip='10.0.0.255',
#     dimage="alfa/vms/video_qrcode_detection", 
#     dcmd="python /root/video_qrcode_detection/v2.py",
#     ports=[(5000, 'udp')],
#     publish_all_ports=True,
#     cpuset_cpus="2"
#     )        

info('*** Adding switches\n')
s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

info('*** Creating links\n')
# net.addLink(s1, s2, cls=TCLink, bw=1, delay='0ms', loss=5)
# net.addLink(s1, s2, cls=TCLink, bw=1, delay='0ms')

net.addLink(d0, d1, cls=TCLink, bw=100,       delay='450ms')

# net.addLink(d1, s1, cls=TCLink, bw=100,       delay='50ms')
# net.addLink(d2, s1, cls=TCLink, bw=100,       delay='100ms')
# net.addLink(d3, s1, cls=TCLink, bw=100,       delay='150ms')

info('*** Starting network\n')
net.start()

# info('*** Testing connectivity\n')
net.pingAll()

time.sleep(10)

print(time.time())

info('*** Executing test\n')
d0.cmd("/vol1/latencia/send_video.sh 10.0.0.251")
info('*** End test\n')

print("\n")
info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()