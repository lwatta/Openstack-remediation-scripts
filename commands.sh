#!/bin/bash
getopts k keystone
if [ "$keystone" = "k" ]; then
	echo "run keystone"
	rm keystone-user-list
	rm keystone-tenant-list
	echo "create user-list"
	keystone --insecure user-list > keystone-user-list
	echo "create tenant-list"
	keystone --insecure tenant-list > keystone-tenant-list
else 
	echo "dont run keystone"
fi

rm nova-flavor-list
rm output
#neutron subnet-list | grep service
echo "starting nova-list-all-tenants with fields"
nova --insecure list --all-tenants --fields user_id,tenant_id,flavor,name,host,config_drive | grep nova > nova_list_all
echo "create nova-flavor-list "
nova --insecure flavor-list --all > nova-flavor-list
./get-vm-flavors.py
