# QA-Practical-Project: Suggestion Generator Efekan Calim
<br>
<br>
<h1> Efekan Calim <h1>

<br>
<h3>Brief</h3>
<br>
<h3>Introduction</h3>
<br>
The objective of this project is to create an application that uses four separate services to generate an object based on a set of rules. The four services should seamlessly communicate with each other without disrupting the application. <br>
The project must include: <br>
1. Software development with Python with the use of Flask, Jinja2 and MySQL modules <br>
2. Use of Jenkins for continuous integration and automated build <br>
3. Cloud fundamentals 
<br> 
<h3>Requirements</h3>
1. An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project. <br>
2. An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine. <br>
3. If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application <br>
4. The project must follow the Service-oriented architecture that has been asked for. <br>
5. The project must be deployed using containerisation and an orchestration tool. <br>
6. As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run. <br>
7. The project must make use of a reverse proxy to make your application accessible to the user.
<br>
<h3>Structure and Planning</h3>
I decided to create an application where four services communicate with each other to generate a suggestion for visiting a given city depending on the weather conditions. <br>
<h4>Service 1</h4><br>
Service 1 was the core service. It's purpose was to perform a GET request on service 2 and 3 and a post request on service 4. The communication was written in the routes section of the python code and containerised via Docker containers. Data was persisted through a MySQL database and responses from services 2, 3 and 4 are displayed via a HTML file in service 1. Below is a snippet of the routes.py file used for service 1.<br>

```python
from flask import Flask, render_template, request
import requests
from application import app

@app.route('/', methods=['GET', 'POST']) 
def index():
    city = requests.get("http://service_2:5001/city")
    weather = requests.get("http://service_3:5002/weather")
    suggestion = requests.post("http://service_4:5003/suggestion", data=weather.text)

    return render_template('index.html', city=city.text, weather=weather.text, suggestion=suggestion.text)
```
<br>
<h4>Service 2</h4><br>
Service 2's purpose was to generate a random city from a list.<br>

```python
from flask import Flask, Response, request
import random
from application import app

@app.route('/city', methods=['GET'])
def city():
    cities = ["London", "Paris", "New York", "Tokyo", "Istanbul", "Rome", "Los Angeles", "Hong Kong", "Amsterdam", "Berlin"]
    return Response(random.choices(cities), mimetype="text/plain")
```
<br>
<h4>Service 3</h4><br>
Service 3's purpose was to generate a random weather condition for the chosen city.<br>

```python
from flask import Flask, Response, request
import random
from application import app

@app.route('/weather', methods=['GET'])
def weather():
    weather_conditions = ["rain", "sun", "snow", "wind", "cloud"]
    return Response(random.choices(weather_conditions), mimetype="text/plain")
```
<br>
<h4>Service 4</h4><br>
Service 4 was used to generate a suggestion based on the weather conditions in the given city. It then returned the suggestion to service 1 as a POST request which was subsequently displayed on the HTML template. <br>

```python
from flask import Flask, Response, request
import random
from application import app

@app.route('/suggestion', methods=['POST'])
def suggestion():
    weather = request.data.decode('utf-8')
    if weather == "rain":
        suggestion = "Not a great time to visit"
    elif weather == "sun":
        suggestion = "It is a great time to visit"
    elif weather == "snow":
        suggestion = "Wrap up warm"
    elif weather == "wind":
        suggestion = "It could get a little brisk"
    elif weather == "cloud":
        suggestion = "It's a bit dull, but at least it isn't raining"
    else:
        suggestion = "No suggestion available"
    return Response(suggestion, mimetype="text/plain")
```
<br>
<h3>Service Orientated Architecture</h3>
<br>
The intial service orientated architecture is shown below. Initially, I had the four services running on four seperate VMs.
<br>
<a href="https://imgur.com/YhWdEwQ"><img src="https://i.imgur.com/YhWdEwQ.png" title="source: imgur.com" /></a>
<br>
After ensuring the application was running smoothly and the 4 services were running in a live environment, I proceeded to change the communication between services from 4 VMs to a Dockerised architecture. I had a different container for each service and ensured that communication persisted through a Docker network. 
<br>
<a href="https://imgur.com/aokbs46"><img src="https://i.imgur.com/aokbs46.png" title="source: imgur.com" /></a>
<br>
<h3>Entity Relation</h3>
<br>
Only one database table was required for the data in this project.<br>
<a href="https://imgur.com/mpYmAxY"><img src="https://i.imgur.com/mpYmAxY.png" title="source: imgur.com" /></a>
<br>
<h3>CI Pipeline and CI</h3>
<br>
Below is a diagram describing the structure of my pipeline. Unfortunately, I ran into problems with SSHing as a Jenkins user, so I was unable to cover the full deployment of the application this time around.<br>
<a href="https://imgur.com/wLabRHC"><img src="https://i.imgur.com/wLabRHC.png" title="source: imgur.com" /></a>
<br>
Checkout, Test and Build stages were successful in my pipeline.<br>
<a href="https://imgur.com/djojVSX"><img src="https://i.imgur.com/djojVSX.png" title="source: imgur.com" /></a>
<br>
Below is a snippet of my Jenkinsfile<br>

```Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "./scripts/test.sh"
            }
        }
        stage('Build') {
            steps {
                sh "./scripts/build.sh"
            } 
        }
        stage('Deploy') {
            steps {
                sh "./scripts/deploy.sh" 
            }
        }
    }
}
```

<br>
<h3>Testing</h3>
<br>
Testing was performed using Pytest and Unittest mock. 100% Testing coverage was achieved in all areas. 
<br>
<h4>Service 1</h4>
<br>
<a href="https://imgur.com/PeVcvAc"><img src="https://i.imgur.com/PeVcvAc.png" title="source: imgur.com" /></a>
<br>
<h4>Service 2</h4>
<br>
<a href="https://imgur.com/xYJcMfM"><img src="https://i.imgur.com/xYJcMfM.png" title="source: imgur.com" /></a>
<br>
<h4>Service 3</h4>
<br>
<a href="https://imgur.com/Q16SYFf"><img src="https://i.imgur.com/Q16SYFf.png" title="source: imgur.com" /></a>
<br>
<h4>Service 4</h4>
<br>
<a href="https://imgur.com/Q16SYFf"><img src="https://i.imgur.com/Q16SYFf.png" title="source: imgur.com" /></a>
<br>
Below is a snippet from my service 1 test.<br>

```python
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_city(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "sun"
                p.return_value.text = "It is a great time to visit"
                response = self.client.get(url_for('index'))
                self.assertIn(b'It is a great time to visit', response.data)
```
<br>
<h3>Frontend Design</h3>
<br>
The user was able to view the homepage through port 5000. A button was provided to make generating the values more user friendly.<br>
<a href="https://imgur.com/j4CytdD"><img src="https://i.imgur.com/j4CytdD.png" title="source: imgur.com" /></a>
<br>
<h3>Risk Assessment</h3>
<br>
My initial risk assessment is displayed below.<br>
<a href="https://imgur.com/nui6oE5"><img src="https://i.imgur.com/nui6oE5.png" title="source: imgur.com" /></a>
<br>
After the project, I revisited this and observed my responses to the risks.<br>
<a href="https://imgur.com/NZAOQoB"><img src="https://i.imgur.com/NZAOQoB.png" title="source: imgur.com" /></a>
<br>
<h3>VCS and Feature Branch Model</h3>
<br>
Using the feature branch model on Github helped me develop different features without affecting my main application. I used pull and merge requests to merge branches with the main once all features were fully working.<br>
<a href="https://imgur.com/sgvh89w"><img src="https://i.imgur.com/sgvh89w.png" title="source: imgur.com" /></a>
<br>
<a href="https://imgur.com/HpuGxiC"><img src="https://i.imgur.com/HpuGxiC.png" title="source: imgur.com" /></a>
<br>
<h3>Project Tracking</h3>
<br>
I used a Jira board to keep track of user stories and tasks required to complete the app
<br>
<a href="https://imgur.com/wH6B8tk"><img src="https://i.imgur.com/wH6B8tk.png" title="source: imgur.com" /></a>
<br>
My final Jira Board is below<br>
<a href="https://imgur.com/2gIZJx9"><img src="https://i.imgur.com/2gIZJx9.png" title="source: imgur.com" /></a>
<br>
<h3>Tools used</h3>
1. Languages: Python, HTML, SQL
<br>
2. Virtual Machine Instance: GCP
<br>
3. Framework: Flask
<br>
4. CI Server: Jenkins
<br>
5. Testing: Pytest, unittest.mock
<br>
6. Project Tracker: Jira
<br>
7. Container Tool: Docker 
<br>
8. Orchestration: Docker-compose
<br>
<h3>Improvements</h3>
<br>
More practice with SSH. The root of the problem with being unable to incorporate Ansible was not due to errors within Ansible itself. I experienced trouble with SSHing as a Jenkins user into swarm nodes and was unable to find the cause of the problem. The error I was faced with was a permission denied prompt. 

















 
    
