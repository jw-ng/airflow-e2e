from airflow_e2e.composer.docker_compose_file.services.airflow_seeder_service import AirflowSeederService


class TestAirflowSeederService:
    def test_should_return_correct_mongo_service_settings(self):
        assert AirflowSeederService().data == {
            "volumes": ["./airflow-connections-and-variables-seeder/:/tmp/seed/"],
        }
