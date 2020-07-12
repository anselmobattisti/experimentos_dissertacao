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
logdir = "/home/"+sys.argv[1]+"/versionado/experimentos_dissertacao/:/vol1"

setLogLevel('info')

net = Containernet(controller=Controller)

info('*** Adding controller\n')
net.addController('c0')

info('*** Adding switches\n')
s1 = net.addSwitch('s1', cls=UserSwitch)

info('*** Adding docker containers\n')
d0 = net.addDocker('d0', ip='10.0.0.250', volumes=[homedir], dimage="ubuntu_gstreamer", dcmd="/bin/bash")

net.addLink(s1, d0, cls=TCLink, bw=100, delay='0ms')

# d2 = net.addDocker('d2', ip='10.0.0.252', volumes=["/home/battisti/versionado/alfa/docs/teste:/vol1"], dimage="ubuntu_gstreamer", dcmd="/bin/bash")

# d3 = net.addDocker('d3', ip='10.0.0.253', dimage="alpine_bash", dcmd="/bin/bash")

lat = {}
d = {}
line_out = ""

for i in range(1,3):

    lat = i * 5

    container_id = 'd'+str(i)

    container_ip = "10.0.0."+str(i+20)

    d = net.addDocker(
        container_id, 
        ip=container_ip,
        volumes=[homedir],
        dimage="alfa/vms/video_qrcode_detection", 
        dcmd="python /root/video_qrcode_detection/v2.py",
        ports=[(5000, 'udp')],
        publish_all_ports=True
    )

    # dcmd="python /root/video_qrcode_detection/v2.py > /vol1/latencia/logs/"+str(i)+".txt",

    info('*** Creating links\n')        
    net.addLink(s1, d, cls=TCLink, bw=100, delay=str(lat)+'ms')
    net.start()

    # info('*** Testing connectivity\n')
    net.pingAll()

    # time.sleep(5)

    line_out += "{}\t{}\t{}\t{}\n".format(container_id, container_ip, lat, time.time())

    cmd_send = '/vol1/latencia/send_video.sh '+container_ip
    print(cmd_send)
    d0.cmd(cmd_send)
    # net.removeDocker(d)

info('*** End test\n')


print("ID\tIP\tLatencia\tStart Time")
print(line_out)

info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()