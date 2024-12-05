# Kubernetes & Helm Commands Cheat Sheet

## Kubernetes Basic Commands
### Check resources
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get configmaps
kubectl get secrets

### Describe resources
kubectl describe pod <pod-name>
kubectl describe deployment <deployment-name>
kubectl describe service <service-name>

### Apply manifests
kubectl apply -f <filename.yaml>
kubectl apply -f <directory>

### Delete resources
kubectl delete -f <filename.yaml>
kubectl delete pod <pod-name>

## Secret Management
### Create base64 encoded string
echo -n "your-password-here" | base64

### Decode base64 string
echo -n "eW91ci1wYXNzd29yZC1oZXJl" | base64 -d

## Testing & Debugging
### Check pod logs
kubectl logs <pod-name>

### Get pod details
kubectl get pod <pod-name> -o yaml

## Test NodePort service
### Get node IP
kubectl get nodes -o wide

### Access service
curl <node-ip>:<nodeport>

### Access service with authorization
curl -H "Authorization: Bearer your-password-here" <node-ip>:<nodeport>

## Helm Commands
### Create new chart
helm create <chart-name>

### Install chart
helm install <release-name> <chart-path>

### List installed releases
helm list

### Uninstall release
helm uninstall <release-name>

### Debug template rendering
helm template <chart-path>


### NodePort Range
- Valid NodePort range: 30000-32767


