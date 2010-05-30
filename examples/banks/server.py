#!/usr/bin/env python

#
#	The banks server
#

import sys
import Pyro
import banks

ns=Pyro.naming.locateNS()
daemon=Pyro.core.Daemon()
ns.remove("example.banks.rabobank")
ns.remove("example.banks.abn")

uri=daemon.register(banks.Rabobank())
ns.register("example.banks.rabobank",uri)
uri=daemon.register(banks.ABN())
ns.register("example.banks.abn",uri)

print("available banks:")
print([name for name in ns.list(prefix="example.banks.")])

# enter the service loop.
print("Banks are ready for customers.")
daemon.requestLoop()
