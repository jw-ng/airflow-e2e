from airflow_e2e.composer.docker_compose_file.services.mongodb_extra_service import MONGODB_EXTRA_SERVICE


def test_should_return_correct_mongo_service_settings():
    assert MONGODB_EXTRA_SERVICE == {
        "mongodb": {
            "container_name": "airflow-mongodb",
            "image": "mongo:latest",
            "command": "mongod",
            "ports": ["27017:27017"],
        }
    }
