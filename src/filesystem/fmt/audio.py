# from dataclasses import dataclass

# from .... import FileFormat as FF
# from .. import Path_
# from . import BaseFormat, BaseFormats


# @dataclass
# class AudioFormat(
#     BaseFormat,
# ):
#     ...


# @dataclass
# class AudioFormats(
#     BaseFormats,
# ):
#     mp3: AudioFormat = AudioFormat(
#         name=FF.MP3,
#     )

#     wav: AudioFormat = AudioFormat(
#         name=FF.WAV,
#     )

#     @classmethod
#     def get_fmt(
#         cls,
#         path: Path_,
#     ) -> AudioFormat:
#         fmt = super().get_fmt(path)
#         return fmt
