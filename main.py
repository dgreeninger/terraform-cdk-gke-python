#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, RemoteBackend, NamedRemoteWorkspace

from cdktf_cdktf_provider_google import (
    GoogleProvider,
    ContainerCluster,
)



class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here
        GoogleProvider(self, id=project_id, region="us-central1", zone="us-central1-a", project=project_id)
        cluster = ContainerCluster(self, "cluster", \
                name="rubrik-test-cluster",
                initial_node_count=2,
            )

app = App()
project_id = "hc-8255d8aec51f4af78c98df80971"
stack = MyStack(app, "gke")
RemoteBackend(stack,
  hostname='app.terraform.io',
  organization='dgreeninger',
  workspaces=NamedRemoteWorkspace('gke')
)

app.synth()
