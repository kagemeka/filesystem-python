import sys
import typing


def _async_read_stdin_chunks() -> typing.Iterator[bytes]:
    while True:
        for chunk in sys.stdin.buffer.readline().split():
            yield chunk


class StdinReader:
    __chunks: typing.Iterator[bytes]

    def __init__(self) -> None:
        self.__chunks = _async_read_stdin_chunks()

    def __call__(self) -> bytes:
        return next(self.__chunks)

    def str(self) -> str:
        return self().decode()

    def int(self) -> int:
        return int(self())


# def line_ints_np(self) -> np.array:
#     return np.fromstring(
#         string=self.str_(),
#         dtype=np.int64,
#         sep=" ",
#     )


# def read_ints_np() -> np.array:
#     return np.fromstring(
#         string=(self().decode()),
#         dtype=np.int64,
#         sep=" ",
#     )
