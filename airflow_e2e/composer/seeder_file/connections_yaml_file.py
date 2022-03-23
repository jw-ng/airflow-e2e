import typing


class ConnectionsYamlFile:
    @property
    def data(self) -> typing.Dict:
        return {
            "example_conn_id": {
                "conn_type": "mongo",
                "host": "192.168.1.123",
                "port": 27017,
            }
        }
