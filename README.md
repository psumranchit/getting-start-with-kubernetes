# getting-start-with-kubernetes
>This very simple demo is setup to run on Docker Desktop just for learning the concept of Kubernetes.

## Project Folders Structure
~~~
├───frontend
│   │   index.html
│   │   Dockerfile
│   │
│   └───k8s
│           deployment.yaml
│           service.yaml
│
├───backend
│   │   main.py
│   │   req.txt
│   │   Dockerfile
│   │
│   └───k8s
│           deployment.yaml
│           service.yaml
│
├───redis
│   └───k8s
│           deployment.yaml
│           service.yaml
|
└───README.md
~~~

## Deployment
- Run `kubectl apple -f` in each `k8s` folder to deploy services.
- Frontend and Backend service.yaml type is `type: LoadBalancer`. This is to automatically bind their services port to host port without the need for port-forward.
- Insert some keys to redis with `kubectl.exe exec <pod-name> -- redis-cli set key value`

## Testing
- Browse to `http://localhost` and enter your key to display value.
