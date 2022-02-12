from __future__ import annotations

import io
import json
import pickle
import typing

import toml
import yaml

T = typing.TypeVar("T")
U = typing.TypeVar("U")


class Readable(typing.Protocol):
    def read(self) -> bytes:
        ...

    def readline(self) -> bytes:
        ...

    def readlines(self) -> list[bytes]:
        ...


Input = typing.Union[
    io.TextIOWrapper,
    io.BufferedReader,
    Readable,
    str,
    bytes,
    int,
]


def dump_yaml(data: typing.Any, path: str) -> None:
    with open(file=path, mode="w") as stream:
        yaml.safe_dump(data, stream, default_flow_style=False)


def load_yaml(path: str) -> typing.Any:
    with open(file=path, mode="r") as stream:
        return yaml.safe_load(stream)


def dump_toml(data: typing.Mapping[str, typing.Any], path: str) -> None:
    with open(file=path, mode="w", encoding="utf-8") as f:
        toml.dump(o=data, f=f)


def load_toml(path: str) -> dict[T, U]:
    with open(file=path, mode="r", encoding="utf-8") as f:
        return typing.cast(dict[T, U], toml.load(f=f))


def dump_pickle(obj: T, pickle_file_path: str) -> None:
    with open(file=pickle_file_path, mode="wb") as f:
        pickle.dump(obj=obj, file=f)


def load_pickle(pickle_file_path: str) -> T:
    with open(file=pickle_file_path, mode="rb") as fp:
        return typing.cast(T, pickle.load(file=fp))


Jsonizable = bool | int | float | str | list | dict | None


def load_json(json_file_path: str) -> Jsonizable:
    with open(file=json_file_path, mode="r", encoding="utf-8") as fp:
        return typing.cast(Jsonizable, json.load(fp=fp))


def dump_json(data: Jsonizable, path: str) -> None:
    with open(file=path, mode="w", encoding="utf-8") as fp:
        json.dump(obj=data, fp=fp)


def encode_json(item: Jsonizable) -> bytes:
    return json.dumps(item).encode()


def decode_to_json(item: bytes) -> Jsonizable:
    return typing.cast(Jsonizable, json.loads(item.decode()))


def read_ini(
    ini_file_path: str,
) -> typing.Mapping[str, typing.Mapping[str, typing.Any]]:
    import configparser

    parser = configparser.ConfigParser()
    parser.read(filenames=ini_file_path)
    return typing.cast(
        typing.Mapping[str, typing.Mapping[str, typing.Any]],
        getattr(parser, "_sections"),
    )


def write_ini(
    data: typing.Mapping[str, typing.Mapping[str, typing.Any]],
    ini_file_path: str,
) -> None:
    import configparser

    cp = configparser.ConfigParser()
    cp.read_dict(data)
    with open(file=ini_file_path, mode="w") as f:
        cp.write(f)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
