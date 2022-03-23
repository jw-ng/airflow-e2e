from airflow_e2e.composer.docker_compose_file.services.mongodb_extra_service import (
    MongoDbExtraService,
)


class TestMongoDbExtraService:
    def test_should_return_correct_mongo_service_settings(self):
        assert MongoDbExtraService().data == {
            "container_name": "airflow-mongodb",
            "image": "mongo:latest",
            "command": "mongod",
            "ports": ["27017:27017"],
        }
