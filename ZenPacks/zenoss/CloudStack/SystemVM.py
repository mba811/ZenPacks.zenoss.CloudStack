###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

from Products.ZenRelations.RelSchema import ToManyCont, ToOne

from ZenPacks.zenoss.CloudStack import BaseComponent


class SystemVM(BaseComponent):
    meta_type = portal_type = "SystemVM"

    gateway = None
    host_id = None
    hostname = None
    linklocal_ip = None
    linklocal_macaddress = None
    linklocal_netmask = None
    network_domain = None
    private_ip = None
    private_macaddress = None
    private_netmask = None
    public_ip = None
    public_macaddress = None
    public_netmask = None
    systemvm_type = None
    template_id = None

    _properties = BaseComponent._properties + (
        {'id': 'gateway', 'type': 'string', 'mode': 'w'},
        {'id': 'host_id', 'type': 'int', 'mode': 'w'},
        {'id': 'hostname', 'type': 'string', 'mode': 'w'},
        {'id': 'linklocal_ip', 'type': 'string', 'mode': 'w'},
        {'id': 'linklocal_macaddress', 'type': 'string', 'mode': 'w'},
        {'id': 'linklocal_netmask', 'type': 'string', 'mode': 'w'},
        {'id': 'network_domain', 'type': 'string', 'mode': 'w'},
        {'id': 'private_ip', 'type': 'string', 'mode': 'w'},
        {'id': 'private_macaddress', 'type': 'string', 'mode': 'w'},
        {'id': 'private_netmask', 'type': 'string', 'mode': 'w'},
        {'id': 'public_ip', 'type': 'string', 'mode': 'w'},
        {'id': 'public_macaddress', 'type': 'string', 'mode': 'w'},
        {'id': 'public_netmask', 'type': 'string', 'mode': 'w'},
        {'id': 'systemvm_type', 'type': 'string', 'mode': 'w'},
        {'id': 'template_id', 'type': 'int', 'mode': 'w'},
        )

    _relations = BaseComponent._relations + (
        ('pod', ToOne(ToManyCont,
            'ZenPacks.zenoss.CloudStack.Pod.Pod',
            'systemvms')
            ),
        )

    def device(self):
        return self.pod().device()

    def getRRDTemplateName(self):
        if self.systemvm_type == 'consoleproxy':
            return 'ConsoleProxy'

        return super(BaseComponent, self).getRRDTemplateName()
