from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link,TCLink

class MyTopo( Topo ):

    def build( self ):

        h1=self.addHost("h1",ip="192.168.1.1")
        h2=self.addHost("h2",ip="192.168.1.2")
        h3=self.addHost("h3",ip="192.168.1.3")
        r1=self.addSwitch("r1")
        r2=self.addSwitch("r2")

        self.addLink(r1,h1)
        self.addLink(r1,h2)
        self.addLink(r2,h3)
        self.build()
        CLI(self)
        self.stop()

topos = { 'mytopo': ( lambda: MyTopo() ) }