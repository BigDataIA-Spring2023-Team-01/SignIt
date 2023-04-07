## Architecture Diagram
#------------------------------------------------------------------------------------------------
# Importing the labels from diagrams

from cProfile import label
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.general import Userresource # to denote user 
from diagrams.alibabacloud.communication import DirectMail # to denote streamlit cloud
from diagrams.elastic.elasticsearch import LogstashPipeline # to denote api 
from diagrams.onprem.container import Docker # to denote docker
from diagrams.custom import Custom # for custom logos : streamlit, whiper api, kaggle
from diagrams.aws.storage import S3 # to denote aws bucket

#-----------------------------------------------------------------------------------------------
#Creating the cloud cluster
with Diagram("Workflow", show=False, direction="LR"):
  user = Userresource("Users")
  with Cluster("Cloud"):
    kaggle = Custom("kaggle","./data/images/kaggle.png")
    # creating streamlit cloud
    with Cluster("Streamlit"):
        with Cluster("Streamlit Cloud"):
          streamlit_cloud = DirectMail("Streamlit Cloud")
          streamlit_app = Custom("Streamlit","./data/images/streamlit-logo.png") 


