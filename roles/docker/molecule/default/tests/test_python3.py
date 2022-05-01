import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# Yes, it's parametrize
@pytest.mark.parametrize('name', [
    #'python3',
    'python3-pip'
    ])
def test_package(host, name):
    p = host.package(name)

    assert p.is_installed


@pytest.mark.parametrize('package', [
    'docker'
    ])
def test_pip(host, package):
    p = host.pip_package.get_packages(pip_path='pip3')
    assert package in p
