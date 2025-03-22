from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    RemovalPolicy
    # aws_sqs as sqs,
)
from constructs import Construct

class AwsInfraPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)    

        # Create S3 bucket with standard configuration
        bucket = s3.Bucket(self, "Bucket",
            bucket_name="zaralinkawspipelinestore",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
            removal_policy=RemovalPolicy.DESTROY
        )        
                
