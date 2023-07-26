```python
import boto3

def setup_cloud():
    # Create a session using your user credentials
    session = boto3.Session(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY',
        region_name='YOUR_REGION'
    )

    # Create an EC2 resource object using the session
    ec2_resource = session.resource('ec2')

    # Create an S3 resource object using the session
    s3_resource = session.resource('s3')

    # Create an RDS resource object using the session
    rds_resource = session.resource('rds')

    # Store the configuration data for cloud setup
    cloud_config = {
        'ec2_resource': ec2_resource,
        's3_resource': s3_resource,
        'rds_resource': rds_resource
    }

    return cloud_config
```