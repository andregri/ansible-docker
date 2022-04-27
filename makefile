pingall:
	ansible -i hosts all -m ping

testdocker:
	curl http://192.168.10.4:4243/version