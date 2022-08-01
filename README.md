# OperSo

This application can be used by sociological companies to analyse "Open questions" answers (question without answer options). THis application make a clustering of answers.

## Installation

To open Command Prompt press Win + R to open the Run box, then type "cmd" and hit Enter to open it.
Go to the folder where you want to install application with command: 
```
cd path_to_new_folder
```
Clone repository with application - type next command in Command Prompt:
```
git clone https://github.com/voluch/OperSo 
```
There are two ways what to do next:
### Installation without Docker
If you have installed Visual Studio and developed smth in python, then you can use next commands:
```
cd OperSo 
pip install virtualenv 
virtualenv venv 
.\venv\Scripts\activate 
pip install -r requirements.txt
```


### Installation with Docker on Windows
At first, you need to install wsl - package that allows to use Linux virtual machines on your Windows pc. To do that use next commands:
```
wsl --install

wsl --set-default-version 2
```
Then download Docker Desktop and install it on your Windows pc.
## Run
To run application without Docker run command:
```
python3 app.py runserver
```
If you have already installed Docker then use next command to build image (only at first run) note: dot at the end is needed:

```
docker build -t operso .
```
and then run this image each time when you need to use application (first run will be long, because application will load models, necessary to make clustering):
```
docker run -p 8090:8090 operso
```
To use application open Google Chrome and go to (type in url): 
```
localhost:8090
```