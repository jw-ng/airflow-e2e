from airflow_e2e.composer.seeder_file.connections_yaml_file import ConnectionsYamlFile


class TestConnectionsYamlFile:
    def test_should_return_correct_examples(self):
        yaml_file = ConnectionsYamlFile()

        assert yaml_file.data == {
            "example_conn_id": {
                "conn_type": "mongo",
                "host": "192.168.1.123",
                "port": 27017,
            }
        }
