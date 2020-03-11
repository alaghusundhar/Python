##  Script : AWS Environment Provisioning Using Python Troposphere
##  Author : Alagusundaram Nithyananndam
##  Role   : Senior DevOps Engineer


from troposphere import Ref, Template, Retain
import troposphere.ec2 as ec2
from troposphere.ec2 import VPC , Tags
import logging
import argparse
import os

t = Template()
t.set_version()
environments=["dev","staging","production"]

LOGGER=logging.getLogger()
logging.basicConfig(format="[%(asctime)s %(levelname)s: %(message)s ",level="INFO")

parser=argparse.ArgumentParser(description="Environment Scaling Using Python Troposphere")
parser.add_argument("-e","--environment",type=str, required=True, choices=['development','integration','production'])
args=parser.parse_args()

repolocation=os.path.dirname(os.path.realpath(__file__))
configurationpath="{}/environment_profiles/{}.yaml".format(repolocation,args.environment)


print(repolocation)
print(configurationpath)

t.add_resource(VPC(
    "VPC",
    EnableDnsSupport="true",
    CidrBlock="10.100.0.0/16",
    EnableDnsHostnames="true",
    DeletionPolicy="Retain",
    Tags=Tags(
        Application=Ref("AWS::StackName"),
        Network="{0} Spot Instance VPC",
        Name="alagu-test-vpc"
    )
))

for env in environments:
    instance = ec2.Instance(env,DeletionPolicy=Retain)
    instance.ImageId = "ami-ed6bec86"
    instance.InstanceType = "t1.micro"
    t.add_resource(instance)

#print(t.to_json())
print(t.to_yaml())