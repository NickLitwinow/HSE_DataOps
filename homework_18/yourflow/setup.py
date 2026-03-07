from setuptools import setup, find_packages

setup(
    name="yourflow",
    version="0.1.0",
    description="Custom MLFlow artifact repository plugin for S3-compatible storage (MinIO)",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "mlflow>=2.0",
        "boto3",
    ],
    entry_points={
        "mlflow.artifact_repository": [
            "s3=yourflow.artifacts:YourFlowArtifactRepository",
        ],
    },
)
