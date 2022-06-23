deploy:
	cdktf deploy gke
destroy:
	cdktf destroy gke
init:
	pipenv install --skip-lock
	terraform login
	cdktf get
docker:
	docker build .
	docker image list
docker-run:
	docker run -it --rm -w="/app" --mount type=bind,source="$(shell pwd)",target=/app dgreeninger/terraform-cdk-python bash
