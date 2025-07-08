provider "aws" {
  region = var.region
}

resource "random_id" "suffix" {
  byte_length = 4
}

resource "aws_iot_thing" "sensor_thing" {
  name = "iot-sensor-thing"
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket = "iot-raw-data-bucket-${random_id.suffix.hex}"
  acl    = "private"
}

resource "aws_s3_bucket" "processed_bucket" {
  bucket = "iot-processed-data-bucket-${random_id.suffix.hex}"
  acl    = "private"
}

resource "aws_glue_catalog_database" "db" {
  name = "iot_data"
}

resource "aws_iam_role" "glue_role" {
  name = "glue_etl_role"
  assume_role_policy = jsonencode({
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "glue.amazonaws.com" }
    }]
    Version = "2012-10-17"
  })
}
