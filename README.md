Pre-reqs:
- docker
- Terraform Cloud account
- GCP project
- Create a Terraform Cloud workspace in your organization
- Add a sensitive environment variable titled `GOOGLE_CREDENTIALS` set that has valid GCP credentials: https://registry.Terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#using-terraform-Cloud

Edit the `main.py` file to utilize your workspace and Terraform organization.
You will need to set several variables in your provider block to connect to Terraform Cloud
```
# Terraform enterprise/Cloud hostname
tf_hostname = "app.Terraform.io"
tf_org = "YOUR_USERNAME"
# create this workspace and make sure you have GOOGLE_CREDENTIALS set up
tf_workspace = "gke"

#GCP project ID
project_id = "example-gcp-id"
```

Run a docker container, mounting the root of this repo to the container.
`make docker-run`
After the docker container comes up, run the command `make init` to initialize the Terraform cdk and login to terraform Cloud.
- Type in `yes` to agree to connect to Terraform Cloud.
- Select the link to the token creation api and open it in your web browser.
- Copy the api key and paste it into the command prompt to link the docker container to Terraform Cloud.
Run the `cdktf deploy` to deploy your stack to Terraform Cloud
