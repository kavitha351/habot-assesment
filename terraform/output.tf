output "storage_bucket_name" {
  description = "Name of the Cloud Storage Bucket"
  value       = google_storage_bucket.raw_landing.name
}
output "bigquery_dataset_id" {
  description = "BigQuery Dataset ID"
  value       = google_bigquery_dataset.staging_dataset.dataset_id
}