##  Script : AWS Environment Provisioning Using Python Troposphere
##  Author : Alagusundaram Nithyananndam
##  Role   : Senior DevOps Engineer

from troposphere import Ref, Template, Retain
import troposphere.ec2 as ec2
from troposphere.ec2 import VPC , Tags

t = Template()
t.set_version()
environments=["dev","staging","production"]

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
    instance.ImageId = "ami-00768769"
    instance.InstanceType = "t1.micro"
    t.add_resource(instance)

#print(t.to_json())
print(t.to_yaml())