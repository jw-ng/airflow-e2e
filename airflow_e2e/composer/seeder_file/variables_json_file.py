import typing


class VariablesJsonFile:
    @property
    def data(self) -> typing.Dict:
        return {
            "example_string_variable": "example_string_value",
            "example_json_variable": {"foo": "bar", "baz": 42},
            "example_array_variable": ["lorem", "ipsum"],
        }
