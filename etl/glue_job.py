import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://<raw-bucket>/sensors/"]},
    format="json"
)

df = df.resolveChoice(specs=[('temperature', 'cast:double'), ('humidity', 'cast:double')])
df = df.withColumn('event_date', df['timestamp'].cast('timestamp'))

sf_options = {
    "sfURL": "<account>.snowflakecomputing.com",
    "sfUser": "USER",
    "sfPassword": "PASSWORD",
    "sfDatabase": "IOT_DB",
    "sfSchema": "PUBLIC",
    "sfTable": "SENSOR_READINGS",
    "sfWarehouse": "COMPUTE_WH"
}

glueContext.write_dynamic_frame.from_options(
    frame=df,
    connection_type="snowflake",
    connection_options=sf_options
)
job.commit()
