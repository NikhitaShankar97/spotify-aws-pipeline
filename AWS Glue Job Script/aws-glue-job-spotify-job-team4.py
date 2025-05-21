import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import explode, col

# Step 1: Glue setup
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Step 2: Read multi-line JSON
df_raw = spark.read.option("multiLine", True).json("s3://spotify-mpd-pipeline-team4/raw/")

# Optional: Filter out corrupt records
df = df_raw.filter(df_raw.playlists.isNotNull())

print(f"✅ Raw JSON loaded. Total root records: {df.count()}")

# Step 3: Explode playlists
df_playlists = df.select(explode("playlists").alias("playlist"))
print(f"✅ Playlists exploded. Total playlists: {df_playlists.count()}")

# Step 4: Explode tracks inside playlists
df_tracks = df_playlists.select(
    col("playlist.pid").alias("playlist_id"),
    col("playlist.name").alias("playlist_name"),
    explode("playlist.tracks").alias("track")
)
print(f"✅ Tracks exploded. Total track rows: {df_tracks.count()}")

# Step 5: Flatten track fields
df_flat = df_tracks.select(
    "playlist_id",
    "playlist_name",
    col("track.track_name"),
    col("track.artist_name"),
    col("track.album_name"),
    col("track.duration_ms"),
    col("track.track_uri")
)
print(f"✅ Final flattened data rows: {df_flat.count()}")
df_flat.show(5)

# Step 6: Write output to S3 Parquet
df_flat.write.mode("overwrite").parquet("s3://output-team4/spotify_flat_output/")


job.commit()
