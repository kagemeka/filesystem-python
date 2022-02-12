# import io
# import json
# import pathlib
# import typing

# Path_ = typing.Union[pathlib.Path, str]

# Input = typing.Union[
#     io.TextIOWrapper,
#     io.BufferedReader,
#     str,
#     bytes,
#     int,
# ]
# T = typing.TypeVar("T")
# U = typing.TypeVar("U")


# class Readable(typing.Protocol):
#     def read(self) -> bytes:
#         ...

#     def readline(self) -> bytes:
#         ...

#     def readlines(self) -> list[bytes]:
#         ...


# Input: typing.Type = typing.Union[
#     io.TextIOWrapper,
#     io.BufferedReader,
#     Readable,
#     str,
#     bytes,
#     int,
# ]


# def dump_yaml(data: typing.Any, path: str) -> typing.NoReturn:
#     import yaml

#     with open(file=path, mode="w") as stream:
#         yaml.dump(data=data, stream=stream)


# def load_yaml(path: str) -> typing.Any:
#     import yaml

#     with open(file=path, mode="r") as stream:
#         return yaml.load(stream=stream, Loader=yaml.FullLoader)


# def dump_toml(
#     data: typing.Mapping[str, typing.Any], path: str
# ) -> typing.NoReturn:
#     """dump_toml"""
#     import toml

#     with open(file=path, mode="w", encoding="utf-8") as f:
#         toml.dump(o=data, f=f)


# import toml


# def load_toml(path: str) -> dict[U, V]:
#     import toml

#     with open(file=path, mode="r", encoding="utf-8") as f:
#         return toml.load(f=f)


# def dump_pickle(obj: T, path: str) -> None:
#     import pickle

#     with open(file=path, mode="wb") as f:
#         pickle.dump(obj=obj, file=f)


# def load_pickle(path: str) -> T:
#     import pickle

#     with open(file=path, mode="rb") as f:
#         return typing.cast(T, pickle.load(file=f))


# Jsonizable = typing.Union[
#     bool,
#     int,
#     float,
#     str,
#     list,
#     dict,
#     None,
# ]


# def load_json(path: str) -> Jsonizable:
#     with open(file=path, mode="r", encoding="utf-8") as fp:
#         return json.load(fp=fp)


# def dump_json(data: Jsonizable, path: str) -> typing.NoReturn:
#     with open(file=path, mode="w", encoding="utf-8") as fp:
#         json.dump(obj=data, fp=fp)


# def encode_json(obj: Jsonizable) -> bytes:
#     return json.dumps(obj).encode()


# def decode_to_json(obj: bytes) -> Jsonizable:
#     return json.loads(obj.decode())


# def read_ini(
#     path: str,
# ) -> typing.Mapping[str, typing.Mapping[str, typing.Any]]:
#     import configparser

#     cp = configparser.ConfigParser()
#     cp.read(filenames=path)
#     return cp._sections


# def write_ini(
#     data: typing.Mapping[str, typing.Mapping[str, typing.Any]],
#     path: str,
# ) -> typing.NoReturn:
#     import configparser

#     cp = configparser.ConfigParser()
#     cp.read_dict(data)
#     with open(file=path, mode="w") as f:
#         cp.write(f)
