# 🎵 Spotify Smart Playlist Prediction — AWS-Native Big Data Pipeline

## 🚀 Project Overview
This project is an end-to-end automated AWS-native data pipeline that ingests, processes, models, and visualizes Spotify playlist data to predict the next track a user is likely to enjoy. The system leverages multiple AWS services to simulate a production-grade infrastructure for music recommendation, showcasing the power of scalable cloud-native design.

## 📌 Motivation
As part of my Big Data Infrastructure course at the University of Illinois Urbana-Champaign, I wanted to deeply explore how enterprise-grade machine learning systems are built. I challenged myself to design a pipeline that uses **all key AWS services** — from ingestion to orchestration, modeling, storage, and visualization — with a focus on reliability, modularity, and learning how each AWS component fits into a production analytics system.

## Dataset
This project uses the [Spotify Million Playlist Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge) provided by AIcrowd and Spotify for the RecSys Challenge. The dataset contains one million user-generated playlists and metadata, which serves as the foundation for building predictive and personalized recommendation systems.

## 🛠️ Technologies Used
- **Amazon S3** – Raw and processed storage (JSON & Parquet)
- **AWS Glue + PySpark** – Serverless ETL & schema transformation
- **AWS Lambda** – Lightweight orchestration and job triggering
- **AWS Athena + Glue Catalog** – SQL querying and data cataloging
- **Amazon SageMaker** – PyTorch model training for next-song prediction
- **Amazon RDS (MySQL)** – Structured storage for model predictions
- **Amazon QuickSight** – Business intelligence dashboard
- **Amazon EventBridge + SNS** – Silent-fail alerting and monitoring

## 🔁 End-to-End Pipeline Architecture
1. **Data Ingestion:** Raw Spotify JSON dumps are uploaded to an S3 bucket.
2. **Orchestration:** A Lambda function triggers a Glue ETL job upon S3 upload.
3. **ETL:** The Glue job parses the JSON files, flattens nested structures (e.g., track arrays), and writes them to Parquet format.
4. **Data Cataloging:** A Glue Crawler registers the output in the Data Catalog for Athena SQL queries.
5. **Modeling:** A PyTorch-based sequence model is trained on playlist patterns using SageMaker.
6. **Storage:** Predicted song sequences are stored in Amazon RDS for downstream access.
7. **Visualization:** QuickSight dashboards present key business insights such as artist frequency, mood shifts, and song duration patterns.
8. **Monitoring:** EventBridge and SNS ensure any pipeline failures are captured and alerted.

## 🧠 ML Component – Next Song Predictor
- Embedding-based neural network
- Trained using Adam optimizer and CrossEntropy loss
- Inputs: sequences of songs from playlists
- Outputs: predicted next song URIs

## 📊 Key Insights
- Mood patterns evolve across playlists — users start energetic and taper into calming music.
- Outliers in track duration flag potential data or user anomalies.
- Model performance captured co-occurrence and temporal dependencies effectively.

## ✅ Outcomes
- Successfully demonstrated use of major AWS services in a unified pipeline.
- Built a functional music recommendation engine from raw data to insights.
- Improved understanding of data engineering best practices and cloud-native architectures.

## 📍 Next Steps
- Add real-time streaming ingestion with Kinesis.
- Expand training data to include additional playlist attributes (e.g., genre, tempo).
- Containerize the model inference using SageMaker Endpoints.

---

If you find this project useful or insightful, feel free to ⭐ the repo!
