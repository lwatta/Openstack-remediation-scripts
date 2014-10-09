Scripts for pulling VM, tenant, host data out of nova and combining with keystone 
to make human readable.

We use this data for figuring out what is running on servers when we need an outage.

commands.sh
	Creates all keystone files used to map user-id to name, tenant-id to name, and to run everything
	Can run with argument to recreate keystone files or use the ones that are already present
	Assumes you have sourced your openrc file

get-vm-flavors.py
	Simply loops through nova list and the keystone files to create human readable.
	Dumps into an output file that is csv importable.
