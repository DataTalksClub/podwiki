---
title: "2 VM in AWS — MLOps Zoomcamp Module 1"
summary: "Note: You don't have to rent an instance in the cloud. You can follow the same instructions for setting up your local environment."
related_course:
  - mlops-module-01
---

[MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) › [Module 1: Introduction](/course-wiki/mlops-module-01/) › 2 VM in AWS

## Notes

**Note**: You don't have to rent an instance in the cloud. You can follow the same instructions 
for setting up your local environment. 

<a href="https://www.youtube.com/watch?v=IXSiYkP23zo&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK">
  
</a>

Code:

Recommended development environment: Linux

### Step 1: Download and install the Anaconda distribution of Python
```sh
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
bash Anaconda3-2022.05-Linux-x86_64.sh
```

### Step 2: Update existing packages

```sh
sudo apt update
```

### Step 3: Install Docker and Docker Compose
Follow the instructions here:
[install-using-the-repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)  
Set up Docker's apt repository.
```sh
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
Install the Docker packages.
```sh
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
To run docker without `sudo`:

```sh
sudo groupadd docker
sudo usermod -aG docker $USER
```

### Step 4: Run Docker

```sh
docker run hello-world
```

If you get `docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create": dial unix /var/run/docker.sock: connect: permission denied.` error, restart your VM instance, or run:
`sudo dockerd`

**Note**: If you get `It is required that your private key files are NOT accessible by others. This private key will be ignored.` error, you should change permits on the downloaded file to protect your private key:

 ```sh
chmod 400 name-of-your-private-key-file.pem
```

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

- [mlops-m01-1-github-codespaces](/course-wiki/mlops-m01-1-github-codespaces/)
- [mlops-m01-course-overview](/course-wiki/mlops-m01-course-overview/)
- [mlops-m01-environment-preparation](/course-wiki/mlops-m01-environment-preparation/)
- [mlops-m01-homework](/course-wiki/mlops-m01-homework/)
- [mlops-m01-introduction](/course-wiki/mlops-m01-introduction/)
- [mlops-m01-mlops-maturity-model](/course-wiki/mlops-m01-mlops-maturity-model/)
- [mlops-m01-optional-training-a-ride-duration-prediction-mod](/course-wiki/mlops-m01-optional-training-a-ride-duration-prediction-mod/)

## Sources

- [Video](https://www.youtube.com/watch?v=IXSiYkP23zo&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK)
- [Lesson file](https://github.com/mlops-zoomcamp/blob/main/01-intro/README.md)
