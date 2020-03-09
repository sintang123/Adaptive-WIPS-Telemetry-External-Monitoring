# Adaptive-WIPS-Telemetry-External-Monitoring

## Purpose
Starting with Catalyst 9800 IOS-XE 17.1, aWIPS detection will be natively available on the platform. 8 Signatures are supported on IOS-XE 17.1 release. DNA Center is required to store aWIPS alarm and to process them for monitoring.

## Challenge
For customers that do not yet have DNA Center in their environment, aWIPS alarm history will only be available for the past 5 minutes. Without DNA Center, they will have limited aWIPS logging and monitoring capabilities.

## Overall Solution
Using gRPC Dial-Out mechanism, we can stream aWIPS YANG data to an external collector (Pipeline) and store them in a database (InfluxDB) for logging.

This Python Web Application will serve the purpose of extracting aWIPS alarm data from InfluxDB and to present them in a dashboard for monitoring.

This "readme" will describe how you can configure the code to connect to InfluxDB and how to run the application.

## Environment

Application is tested on Ubuntu 16.04 LTS and MacOS Catalina 10.15.3.

## Pre-Requisites

*Commands will be based on Ubuntu syntax

### Install Packages into your Python3 Environment

sudo apt-get install python3-pip
pip3 install flask
pip3 install requests
pip3 install python-dateutil


### Configure Environment Variable for Flask

In the terminal, navigate into the main folder where **index.py** exist.

export FLASK_APP = index.py

*Command will inform Flask to run index.py whenever 'flask run' is executed*

### Configure the code to Integrate with InfluxDB

Open index.py

Line 20: InfluxDB_IP = "<IP_ADDRESS>"

**Replace** the <IP_Address> to your **InfluxDB's IP Address**

## Running the Application

On the terminal:

flask run





