# SignIt
## Bridging the gap between the deaf and hearing world 


Although sign language is an effective means of communication, not everyone is familiar with it. Likewise, communicating with the hearing world might be difficult for those who are deaf or hard of hearing. To solve this problem, we are creating this application- the SignIt, which will allow users to convert audio files into sign language with visuals.
The application will translate the speech into sign language using images with the help of  machine learning models. It will help specially abled people to communicate better
The application is user-friendly, interactive, and accessible to all users, including people with disabilities, with the aim to make bridge the gap and make sign language accessible to everyone and promote inclusivity in society.

Documentation : https://codelabs-preview.appspot.com/?file_id=1X1QqIOQJCSoaQi4mgK65-rOduMF31kH8m9TLyu2wmto/edit#3

Streamlit :

Fast API: 

# Project Execution 

The Git repository contains all the necessary resources for this project. To begin, you will need to clone the repository and access it within your virtual environment.
1. Open terminal
2. Browse the location where you want to clone the repository
3. Write the following command and press enter 
````
  git clone https://github.com/BigDataIA-Spring2023-Team-01/SignIt.git
 ````
4.Now we need to run the following command which will download the dataset from kaggle that we are using to generate the sign language videos.
 ````
python3 db_metadata.py
 ````
 ````
python3 dataset_download.py
 ````
	
Note: This will download around 5GB of dataset to the data/ directory. This will be needed to    create the sign language videos. 
Always run the above commands in sequence

5.We will run the docker compose command which will initiate all the containers and volumes needed and will startup the project
 ````
docker-compose build
 ````
 ````
Docker-compose up -d
 ````

Note: This assumes that you have docker desktop installed in your machine, if not please download docker desktop from the following website (Docker Desktop: https://www.docker.com/products/docker-desktop/) and startup the docker and docker-compose service using the below documentation : https://docs.docker.com/desktop/
  

In order to execute the project you would also need to make a .env file with the following requirements
 ````
 AWS_ACCESS_KEY = <Your AWS Access Key>
AWS_SECRET_KEY = <Your Aws Secret Access Key>
OPENAI_SECRET_KEY = <Your Whisper API Key>
SIGN_LANGUAGE_BUCKET = signlanguagevideos
STREAMLIT_URL = <To be taken from README.md>

  ````

Get a key for the Whisper API and Kaggle API
Our SignIt comes up with Whisper API Key and Kaggle API. In order to use it, you’ll need to request an API key and token for Kaggle API. These are easy to use, and free for non-commercial projects.
# Reference 
./api

This folder contains the fast API functions

./data

This folder contains the dataset, the missing alphabet's videos, and images used in the project

./pytest

This folder contains the testing file and use cases 

./streamlit

This folder contains the web application files.

# Declaration 
Contribution 
 
1. Anandita Deb : 25%
2. Cheril Yogi :25%
3. Shamin Chokshi :25%
4. Thejas Bharadwaj :25%
 
WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK.
