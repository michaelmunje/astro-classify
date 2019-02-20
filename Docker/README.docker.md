# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Guide](#2-Guide)
    - [2.1. Why use Docker?](#21-why-use-docker)
    - [2.2. Installing Docker](#22-installing-docker)
        - [2.2.1. Windows](#221-windows)
        - [2.2.2. MacOS](#222-macos)
        - [2.2.3. Linux](#223-linux)
        - [2.2.4. GPU Support](#224-gpu-support)    
    - [2.3. Jupyter Notebook](#23-jupyter-notebook)
- [3. References](#3-references)

<!-- /TOC -->
# 2. Guide
## 2.1. Why use Docker?
Docker makes it easier for us to set up a common environment that contains all of the software we use. Additionally, it's likely that we'll want to use some cloud computing later in this class; most cloud providers support uploading a docker image to run an ML training job (Google Cloud has ML, AWS has SageMaker, Paperspace has Gradient). Building our expiremental code around containers will make it easier to deploy in the cloud later.

For now, this guide focuses on getting Docker installed and setting up a python environment for playing with machine learning tools.

## 2.2. Installing Docker
Linux has the best support for the Docker ecosystem, although you can install it on Windows and MacOS as well. Instructions for each are below. Docker on Linux has the benefit of not requiring virtualization, and it's also easier to run it with GPU support.

### 2.2.1. Windows
If you have Windows 10 64bit: Pro, Enterprise or Education, [follow these instructions](https://docs.docker.com/docker-for-windows/install/). Make sure you enable virtualization in your BIOS.

If you don't meet the minimum requirements, you can use Docker inside of a virtual machine. [Docker toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) will make this easier.

### 2.2.2. MacOS
Instructions for MacOS are [here](https://docs.docker.com/docker-for-mac/install/).


### 2.2.3. Linux
Instructions for Linux are here. Choose the appropriate distribution. If you want GPU support, skip to the next section.
 - [CentOS](
https://docs.docker.com/install/linux/docker-ce/centos/)
 - [Debian](
https://docs.docker.com/install/linux/docker-ce/debian/)
 - [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)
 - [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

It's advisable to follow [these post-installation steps](https://docs.docker.com/install/linux/linux-postinstall/) so your docker service can be without `sudo` and so the service starts on boot.

### 2.2.4. GPU Support
This section only applies to Linux installations. GPU support isn't (natively) available on systems using virtualization to run Docker.

[`nvidia-docker`](https://www.nvidia.com/object/docker-container.html) makes it unneccessary to install GPU drivers inside each container, allowing instead for drivers to be kept on the host OS. This setup is particularly useful if you're planning on running multiple containers which require GPU acceleration, but it might not be necessary for this class. Follow the instructions [here](https://github.com/NVIDIA/nvidia-docker) to install `nvidia-docker`.


## 2.3. Jupyter Notebook
We'll be using the jupyter/tensorflow-notebook docker image. It comes with tensorflow, keras, scikit-learn, and jupyter notebook. You can pull the image using the following command:

`docker pull jupyter/tensorflow-notebook`

After it pulls the image, run the following command to start the container. It will mount your ~/notebooks directory for use inside Jupyter Notebook - if you want to run notebooks from another folder, replace `~/notebooks` with the appropriate path.

`docker run -p 8888:8888 -v ~/notebooks:/home/${USER} jupyter/tensorflow-notebook`

# 3. Cloud ML with Docker
TODO. This section should describe how to take a container and set it up to run on AWS Sagemaker or Google Cloud Platform ML (aka GCP ML). 

## 3.1 Brainstorming
Some of the details of this need to be worked out as a team.
- Do we want to cloud-host inference-making as well?
  - Sagemaker has Endpoints, GCP has something similar. These let you place a model in object storage, and then exposes a REST interface for requesting inferences.
- Is there a preference for platforms? 
- Cost:
  - GCP's $300 credit is great for learning how to do ML
  - Paperspace has a referral program, ie if you use [my referral code](https://www.paperspace.com/&R=2RCPUXR) you get $10, I get $15 later if you stay with the platform. Their [jobs API](https://support.paperspace.com/hc/en-us/articles/360003415434-Containers-Public-Private) is useful for deploying docker training tasks.




# 4. References
These resources may be useful.
- https://www.dataquest.io/blog/docker-data-science/
  - Considerations for using docker containers with Jupyter.