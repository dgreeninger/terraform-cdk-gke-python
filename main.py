#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, RemoteBackend, NamedRemoteWorkspace

from cdktf_cdktf_provider_google import (
    GoogleProvider,
    ContainerCluster,
)

# Set the variables below to match your environment
# terraform enterprise/cloud hostname
tf_hostname = "app.terraform.io"
tf_org = "dgreeninger"
tf_workspace = "terraform-cdk-python-gke"

#GCP project ID
project_id = "hc-9ece0761f15b43008bcdb729cc9"

# Example code continues. You shouldn't need to modify anything below.

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here
        GoogleProvider(self, id=project_id, region="us-central1", zone="us-central1-a", project=project_id)
        cluster = ContainerCluster(self, "cluster", \
                name="gke-test-cluster",
                initial_node_count=2,
            )

app = App()
stack = MyStack(app, "gke")
RemoteBackend(stack,
  hostname=tf_hostname,
  organization=tf_org,
  workspaces=NamedRemoteWorkspace(tf_workspace)
)

app.synth()
