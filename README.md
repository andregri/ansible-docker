# Deploy services from local machine
Setup a remote context with docker:
```
docker context create manager-remote --docker "host=ssh://vagrant@192.168.56.4"
docker context use manager-remote
```
