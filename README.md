Pre-reqs:
- docker
- Terraform Cloud account
- GCP project
- Create a Terraform Cloud workspace in your organization
- Add a sensitive environment variable titled `GOOGLE_CREDENTIALS` set that has valid GCP credentials: https://registry.Terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#using-terraform-Cloud

Edit the `main.py` file to utilize your workspace and Terraform organization.
You will need to set several variables in your provider block to connect to Terraform Cloud
```
# Terraform Enterprise/Cloud hostname
tf_hostname = "app.terraform.io"
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
Run the `cdktf deploy` to deploy your stack to Terraform Cloud.
As the deployment runs, you can check in on things in the GCP console.

Enable VCS Triggered Runs
- Update the `Terraform Working Directory` in your `Settings` -> `General` tab to `cdktf.out/stacks/STACK_NAME/`
- Connect your VCS Repo in `Settings` -> `Version Control`
- Update your .gitignore and remove the `cdktf.out` entry.
- `git commit add -f cdktf.out` and commit/push your output directory.
- The Terraform Cloud Workspace should now be able to to trigger a Run.

Finally, tear down your resources with `cdktf destroy`.
