## Deployment attempt

I created a managed online endpoint from the registered MLflow model
`knn-maintenance-notebook`. I faced these issues:
1. SubscriptionNotRegistered: some resource providers (PolicyInsights, Cdn) were not registered on the new subscription. I registered them from the portal.
2. The deployment container crashed (Liveness probe failed) on Standard_DS2_v2, likely a VM size / library version issue.
The deployment code is in the repo notebook or described here, and all resources were deleted at the end to avoid charges.
