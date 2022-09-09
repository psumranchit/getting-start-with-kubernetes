# getting-start-with-kubernetes
>This very simple demo is setup to run on Docker Desktop just for learning the concept of Kubernetes.

## Deployment
~~~
│   README.md
│
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
└───database
    └───k8s
            deployment.yaml
            service.yaml
            set-data.txt
~~~
