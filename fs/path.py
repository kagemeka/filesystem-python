
import typing
import os
import glob


def preparedir(path: str) -> NoReturn:
    os.makedirs(os.path.dirname(path), exist_ok=True)


def makefile(path: str) -> NoReturn:
    preparedir(path)
    with open(file=path, mode='w') as f: pass


def finddirs(root: str) -> list[str]:
    return sorted(glob.glob(f'{root}/**/*/', recursive=True))


def findfiles(root: str, exts: typing.Iterable[str] = ['*']) -> list[str]:
    import itertools
    return sorted(itertools.chain(*(
        glob.glob(f'{root}/**/*.{ext}', recursive=True)
        for ext in exts
    )))


def changepath_ignorecase(s: str, ptn: str, to: str) -> str:
    import re
    return re.sub(pattern=ptn, repl=to, string=s, flags=re.IGNORECASE)


def currentfiledir(__file__: str) -> str:
    return os.path.abspath(os.path.dirname(__file__))


def currentfiledir_jupyter(globals: typing.Callable[[], typing.Dict[str, typing.Any]]) -> str:
    return globals()['_dh'][0]


def getext(path: str) -> str:
    return os.path.splitext(os.path.abspath(path))[-1].lstrip('.').lower()


def getrootname(path: str) -> str:
    return os.path.splitext(os.path.abspath(path))[0]


def getbaserootname(path: str) -> str:
    return os.path.basename(getrootname(path))


def assert_ext(path: str, ext: str = r'.+') -> bool:
    import re 
    return re.compile(ext, re.IGNORECASE).match(getext(path)) is not None
