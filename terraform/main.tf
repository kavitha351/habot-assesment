resource "google_storage_bucket" "raw_landing" {
  name                        = var.bucket_name
  location                    = var.region
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  force_destroy               = false
  public_access_prevention    = "enforced"
}

resource "google_storage_bucket_iam_member" "data_ingestor" {
  bucket = google_storage_bucket.raw_landing.name
  role   = "roles/storage.objectCreator"
  member = "serviceAccount:data-ingestor@${var.project_id}.iam.gserviceaccount.com"
}

resource "google_bigquery_dataset" "staging_dataset" {
  dataset_id                 = var.dataset_id
  location                   = var.region
  description                = "Staging dataset for validated student onboarding data"
  delete_contents_on_destroy = false
}

resource "google_bigquery_dataset_iam_member" "analytics_reader" {
  dataset_id = google_bigquery_dataset.staging_dataset.dataset_id
  role       = "roles/bigquery.dataViewer"
  member     = "group:analytics@example.com"
}