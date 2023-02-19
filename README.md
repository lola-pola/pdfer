# pdfer


[![pdfer](https://github.com/lola-pola/pdfer/actions/workflows/pdfer.yaml/badge.svg)](https://github.com/lola-pola/pdfer/actions/workflows/pdfer.yaml)
[![Deployment Status](https://github.com/lola-pola/pdfer/actions/actions/workflows/pdfer/badge.svg)]
[![GitHub license](https://img.shields.io/github/license/lola-pola/pdfer.svg)](https://github.com/lola-pola/pdfer/blob/main/LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://pdfer-elhay.eastus.cloudapp.azure.com/)
[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/lolapola/pdfer?label=docker%20image)](https://hub.docker.com/r/lolapola/pdfer)
[![Docker Pulls](https://img.shields.io/docker/pulls/lolapola/pdfer)](https://hub.docker.com/r/lolapola/pdfer)
[![Helm Chart](https://img.shields.io/badge/helm-chart-blue)](https://lola-pola.github.io/pdfer/)
## Description

pdfer is a Streamlit application that allows you to upload files and convert them to PDF format. The application is built using Python and the following libraries:

- Streamlit
- FPDF
- Requests
- UUID

## Demo

You can try the application by clicking on the Streamlit badge above or by going to the following URL: `https://share.streamlit.io/lola-pola/pdfer/main/app.py`. The application is hosted on Streamlit's servers and does not require any installation or setup.

## How to Use

1. Upload a file by clicking on the "Upload File" button and selecting a file from your local machine.
2. Click on the "Convert to PDF" button to convert the uploaded file to PDF format. The converted file will be downloaded automatically.

## Installation

If you want to run the application locally, you can clone the repository and install the required libraries using pip:

```
git clone https://github.com/lola-pola/pdfer.git
cd pdfer
pip install -r requirements.txt
```


After installing the required libraries, you can run the application using the following command:

```
streamlit run app.py
```


### Docker

You can also run the `pdfer` application using Docker. Here are the steps to do this:

1. Clone the repository:
```bash
   git clone https://github.com/lola-pola/pdfer.git
   cd pdfer
```
Build the Docker image:
```
docker build -t pdfer .
```
This will build a Docker image called pdfer using the Dockerfile in the repository.

Run a container from the image:
```
docker run -p 8501:8501 pdfer
```
This will run a container from the pdfer image and map port 8501 in the container to port 8501 on your host machine. You can access the application by going to http://localhost:8501 in your web browser.


###Helm 
You can also run the pdfer application on Kubernetes using Helm. Here are the steps to do this:

Install Helm if you haven't already done so:
```
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```
Add the Helm chart repository:
```
helm repo add pdfer https://lola-pola.github.io/pdfer/ 
```
Install the chart:

```
helm install pdfer pdfer/pdfer
```
This will install the pdfer application on your Kubernetes cluster using the Helm chart.

Access the application:

You can access the pdfer application by going to http://<EXTERNAL-IP>:8501 in your web browser, where <EXTERNAL-IP> is the external IP address of the pdfer service. You can get the external IP address by running:
```
kubectl get services pdfer
```
This will display information









## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.