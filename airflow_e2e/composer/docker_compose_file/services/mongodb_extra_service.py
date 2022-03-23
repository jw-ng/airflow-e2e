MONGODB_EXTRA_SERVICE = {
    "mongodb": {
        "container_name": "airflow-mongodb",
        "image": "mongo:latest",
        "command": "mongod",
        "ports": ["27017:27017"],
    }
}
