import glob
import os
import typing


def prepare_directory(filepath: str) -> None:
    directory_path = os.path.dirname(filepath)
    if not directory_path:
        return
    os.makedirs(directory_path, exist_ok=True)


def make_file(filepath: str) -> None:
    prepare_directory(filepath)
    with open(file=filepath, mode="w") as _:
        pass


def find_directories(root_directory: str) -> list[str]:
    return sorted(glob.glob(f"{root_directory}/**/*/", recursive=True))


def find_files(
    root_directory: str,
    extensions: typing.Iterable[str] = ["*"],
) -> list[str]:
    import itertools

    return sorted(
        itertools.chain(
            *(
                glob.glob(f"{root_directory}/**/*.{ext}", recursive=True)
                for ext in extensions
            )
        )
    )


def change_path_ignorecase(path: str, pattern: str, to: str) -> str:
    import re

    return re.sub(pattern=pattern, repl=to, string=path, flags=re.IGNORECASE)


def get_current_file_directory(__file__: str) -> str:
    return os.path.abspath(os.path.dirname(__file__))


def get_current_file_directory_jupyter(
    globals: typing.Callable[[], dict[str, str]],
) -> str:
    return globals()["_dh"][0]


class AmbiguousExtensionError(Exception):
    pass


def get_file_extension(filepath: str) -> typing.Optional[str]:
    filepath = os.path.abspath(filepath)
    if filepath.count(".") > 1:
        raise AmbiguousExtensionError
    chunks = os.path.splitext(filepath)
    if not chunks[-1]:
        return None
    return chunks[-1].lstrip(".").lower()


def get_rootname(path: str) -> str:
    return os.path.splitext(os.path.abspath(path))[0]


def get_base_rootname(path: str) -> str:
    return os.path.basename(get_rootname(path))


def assert_extension(filepath: str, extension: str = r".+") -> bool:
    import re

    return (
        re.compile(extension, re.IGNORECASE).match(
            _unwrap(get_file_extension(filepath))
        )
        is not None
    )


T = typing.TypeVar("T")


def _unwrap(item: typing.Optional[T]) -> T:
    assert item is not None
    return item
