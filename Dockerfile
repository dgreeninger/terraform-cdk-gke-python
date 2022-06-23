FROM amd64/ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /app
RUN apt update
RUN apt install -y gpg pipenv yarn wget make curl
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN wget -qO - terraform.gpg https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/terraform-archive-keyring.gpg
RUN echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/terraform-archive-keyring.gpg] https://apt.releases.hashicorp.com focal main' > /etc/apt/sources.list.d/terraform.list
RUN apt update
RUN apt install -y terraform nodejs
RUN npm install --silent --global cdktf-cli@0.12.0-pre.22
