kubectl create deployment --image=jupyter/all-spark-notebook kubernetes-data-science
kubectl get deployments
kubectl get pods
kubectl logs -f kubernetes-data-science-xxxx-xxxx
kubectl expose deployment kubernetes-data-science --port=8888 --name=kubernetes-data-science-http
kubectl port-forward kubernetes-data-science-xxxx-xxxx 8888:8888
