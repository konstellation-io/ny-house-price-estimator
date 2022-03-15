apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: krt-demo-configmap
  namespace: demo
data:
  DOMAIN_NAME: $DOMAIN_NAME
  config.json: |
    {
      "API_BASE_URL": "https://demo.$DOMAIN_NAME"
    }

