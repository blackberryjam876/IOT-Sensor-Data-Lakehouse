output "raw_bucket_name" {
  value = aws_s3_bucket.raw_bucket.bucket
}

output "processed_bucket_name" {
  value = aws_s3_bucket.processed_bucket.bucket
}

output "glue_db_name" {
  value = aws_glue_catalog_database.db.name
}

output "glue_role_arn" {
  value = aws_iam_role.glue_role.arn
}
