# stock-web
Stock Web

## deploy
gcloud builds submit --config cloudmigrate.yaml --substitutions _INSTANCE_NAME=stock,_REGION=asia-northeast1

gcloud run deploy polls-service --platform managed --region asia-northeast1 --image gcr.io/stock-info-297717/polls-service
