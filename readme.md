# Career Map Api

An Api which returns detail of soft and hard skills for a given job role.

## Steps to Start VM Instance

Open Terminal and enter below command
* gcloud compute instances start api-deploy-ready<br />
'Instance external IP is External_IP' if this appears this means instance has started.

## Steps to run api

* ssh -L 8080:127.0.0.1:5000 trantoriot@External_IP
* source env/bin/activate
* cd api-flaskrestplus/
* python run.py<br />
Paste url: http://127.0.0.1:8080/api/v1/career_map/documentation in your browser to access api.

## Steps to stop VM Instance

* ctrl+c
* exit
* gcloud compute instances stop api-deploy-ready<br />
'Stopping instance(s) api-deploy-ready...done' if this appears this means instance has stopped.