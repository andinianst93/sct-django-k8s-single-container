# After installing Ubuntu and Microk8s in the cloud 
You can follow these steps to deploy your Django app as a single container to Kubernetes. Please note that I am using NodePort for testing purposes, as it provides a simple way to expose the application externally and is well-suited for testing scenarios.  

![djangoappk8s](https://res.cloudinary.com/andinianst93/image/upload/v1699228312/Screenshot_2023-11-06_at_6.50.10_AM_dewd5n.jpg)
1. To connect your local computer to your Ubuntu VM in the cloud, you'll need the Kubernetes configuration. Retrieve it from your Ubuntu VM using the following command:
```
cat /var/snap/microk8s/current/credentials/client.config
```
2. Create a folder named sct-django-k8s on your local computer.
3. Open Visual Studio Code (VSCode) and create the following folder and files structure inside the sct-django-k8s directory. Then, copy the contents of client.config from your Ubuntu VM (from top to bottom) and paste it into a file named kubeconfig.yaml. Be careful not to change anything within the file.
```
- sct-django-k8s
 -- .kube
    --- kubeconfig.yaml
 -- k8s
    --- service.yaml
    --- deployment.yaml
 -- web
```
If your kubeconfig.yaml looks like this:
```
server: https://127.0.0.1:your-port
```
Run the following command on your Ubuntu VM, replacing your-port with the actual port:
```
kubectl get nodes -o wide
```
Copy the INTERNAL IP and paste it into your kubeconfig.yaml on your local computer, adding the port as shown in the example below:
```
server: https://000.000.000.000:your-port
```
4. On your local computer, set the KUBECONFIG environment variable to point to the kubeconfig.yaml file using the following commands:
```
export KUBECONFIG=$(pwd)/.kube/kubeconfig.yaml
```
Then, run the following command to ensure that you can connect to your Kubernetes cluster:

```
kubectl get nodes 
```
If you see "ubuntu" listed as a node and its status is "ready," you are now ready to deploy your Django web application to Kubernetes.