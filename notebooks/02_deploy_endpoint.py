# Import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment
from azure.ai.ml.entities import Model, Environment
from azure.identity import DefaultAzureCredential
import json
import urllib.request

# 1. Authenticate and connect to Azure ML Workspace
credential = DefaultAzureCredential()

# Replace with your actual subscription id, resource group, and workspace name if needed
ml_client = MLClient.from_config(credential=credential)

print(f"Connected to workspace: {ml_client.workspace_name}")

# 2. Define Endpoint Name
endpoint_name = "knn-maint-iram15-v3"

# 3. Create or Update Managed Online Endpoint
endpoint = ManagedOnlineEndpoint(
    name=endpoint_name,
    description="Managed online endpoint for KNN predictive maintenance model",
    auth_mode="key",
)

print(f"Creating/Updating endpoint: {endpoint_name}...")
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
print("Endpoint created successfully.")

# 4. Configure Deployment (Blue Deployment)
deployment_name = "blue"

# Assuming you registered your model or referenced it correctly from previous steps
# If deploying directly from local files or a registered model name:
model_name = "knn-predictive-maintenance-model"
model_version = "1" # Update version if needed

# Define online deployment
blue_deployment = ManagedOnlineDeployment(
    name=deployment_name,
    endpoint_name=endpoint_name,
    model=model_name,
    version=model_version,
    instance_type="Standard_DS2_v2",
    instance_count=1,
)

print(f"Creating/Updating deployment '{deployment_name}' for endpoint '{endpoint_name}'...")
ml_client.online_deployments.begin_create_or_update(blue_deployment).result()
print("Deployment completed successfully.")

# 5. Allocate 100% Traffic to Blue Deployment
endpoint.traffic = {deployment_name: 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
print("Traffic allocated successfully.")

# 6. Test the Endpoint with Sample Input Data
scoring_uri = ml_client.online_endpoints.get(endpoint_name).scoring_uri
keys = ml_client.online_endpoints.get_keys(endpoint_name)
primary_key = keys.primary_key

input_data = {
    "input_data": {
        "columns": [
            "air_temp_k",
            "process_temp_k",
            "rpm",
            "torque_nm",
            "tool_wear_min",
            "type"
        ],
        "data": [
            [298.1, 308.6, 1551.0, 42.8, 5.0, "M"]
        ]
    }
}

body = str.encode(json.dumps(input_data))
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {primary_key}",
}

req = urllib.request.Request(scoring_uri, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read().decode("utf-8")
    print("Prediction Response:", result)
except urllib.error.HTTPError as error:
    print(f"Request failed with status code: {error.code}")
    print(error.read().decode("utf-8"))
