# IoT Sensor Data Lakehouse

This repository contains a complete IoT Sensor Data Lakehouse implementation including:

- **infra/**: Terraform code for provisioning AWS infrastructure (IoT Core, S3, Glue, IAM).
- **simulator/**: Python-based IoT sensor simulator publishing to AWS IoT Core.
- **etl/**: AWS Glue ETL job (Python) to process raw data in S3 and load into Snowflake.
- **api/**: Spring Boot Java microservice exposing REST endpoints to query sensor readings.

## Setup

1. **Infra (Terraform)**
    ```bash
    cd infra
    terraform init
    terraform apply -auto-approve
    ```

2. **Simulator**
    ```bash
    cd simulator
    pip install -r requirements.txt
    python sensor_simulator.py
    ```

3. **ETL (AWS Glue)**
    - Upload `glue_job.py` to an AWS Glue job.
    - Assign the IAM role created by Terraform.
    - Configure job arguments and run.

4. **API**
    ```bash
    cd api
    ./mvnw spring-boot:run
    ```
    Access endpoints at `http://localhost:8080/sensors/latest`.

