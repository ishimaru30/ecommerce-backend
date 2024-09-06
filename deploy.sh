#!/bin/bash

# Project and service details
PROJECT_ID="citric-aleph-231013"
SERVICE_NAME="ecommerce-backend-service"  # Update the service name as needed
REGION="us-central1"
IMAGE="gcr.io/$PROJECT_ID/$SERVICE_NAME"

# Step 1: Build the Docker image without cache
echo "Building the Docker image..."
docker build --no-cache -t $IMAGE .

# Step 2: Push the Docker image to Google Container Registry
echo "Pushing the image to Google Container Registry..."
gcloud builds submit --tag $IMAGE

# Step 3: Deploy to Google Cloud Run
echo "Deploying to Google Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --image $IMAGE \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars SECRET_KEY="5c750dfc0cfd0b623427f891a59a2c10ad132374d9375efedbe567c830983d02"  # Use your actual secret key

echo "Deployment successful!"
