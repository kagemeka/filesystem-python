import typing 
import io
import pathlib 
import json 


Path_ = typing.Union[pathlib.Path, str]

Input = typing.Union[
    io.TextIOWrapper,
    io.BufferedReader,
    str,
    bytes,
    int,
]



class Readable(typing.Protocol):
    def read(self) -> bytes:
        ...

    def readline(self) -> bytes:
        ...

    def readlines(self) -> list[bytes]:
        ...


Input: typing.Type = typing.Union[
    io.TextIOWrapper,
    io.BufferedReader,
    Readable,
    str,
    bytes,
    int,
]



def dump_yaml(data: typing.Any, path: str) -> typing.NoReturn:
    import yaml
    with open(file=path, mode='w') as stream:
        yaml.dump(data=data, stream=stream)


def load_yaml(path: str) -> typing.Any:
    import yaml
    with open(file=path, mode='r') as stream:
        return yaml.load(stream=stream, Loader=yaml.FullLoader)



def dump_toml(data: typing.Mapping[str, typing.Any], path: str) -> typing.NoReturn:
    '''dump_toml

    '''
    import toml
    with open(file=path, mode='w', encoding='utf-8') as f:
        toml.dump(o=data, f=f)


def load_toml(path: str) -> dict:
    import toml
    with open(file=path, mode='r', encoding='utf-8') as f:
        return toml.load(f=f)





def dump_pickle(obj: typing.Any, path: str) -> typing.NoReturn:
    import pickle 
    with open(file=path, mode='wb') as f:
        pickle.dump(obj=obj, file=f)


def load_pickle(path: str) -> typing.Any:
    import pickle 
    with open(file=path, mode='rb') as f:
        return pickle.load(file=f)


Jsonizable: typing.Type = typing.Union[
    bool,
    int,
    float,
    str,
    list,
    dict,
    None,
]


def load_json(path: str) -> Jsonizable:
    with open(file=path, mode='r', encoding='utf-8') as fp:
        return json.load(fp=fp)


def dump_json(data: Jsonizable, path: str) -> typing.NoReturn:
    with open(file=path, mode='w', encoding='utf-8') as fp:
        json.dump(obj=data, fp=fp)


def encode_json(obj: Jsonizable) -> bytes:
    return json.dumps(obj).encode()


def decode_to_json(obj: bytes) -> Jsonizable:
    return json.loads(obj.decode())


def read_ini(path: str) -> typing.Mapping[str, typing.Mapping[str, typing.Any]]:
    import configparser
    cp = configparser.ConfigParser()
    cp.read(filenames=path)
    return cp._sections


def write_ini(
    data: typing.Mapping[str, typing.Mapping[str, typing.Any]],
    path: str,
) -> typing.NoReturn:
    import configparser
    cp = configparser.ConfigParser()
    cp.read_dict(data)
    with open(file=path, mode='w') as f:
        cp.write(f)
