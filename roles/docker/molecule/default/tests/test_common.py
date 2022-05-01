import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# Yes, it's parametrize
@pytest.mark.parametrize('name', [
    'yum-utils',
    'device-mapper-persistent-data',
    'lvm2'
    ])
def test_package(host, name):
    p = host.package(name)

    assert p.is_installed
