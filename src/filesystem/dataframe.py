# import pandas as pd


# def write_df() -> NoReturn:
#     ...


# class DFWriter:
#     def __call__(
#         self,
#         df: pd.DataFrame,
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         return self.write(
#             df,
#             path,
#             *args,
#             **kwargs,
#         )

#     @classmethod
#     def write(
#         cls,
#         df: pd.DataFrame,
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> None:
#         from .. import DFFormats as DF

#         f = DF.get_fmt(path)
#         if f is None:
#             return

#         f = f.name

#         if f == FF.CSV:
#             cls.csv(
#                 df,
#                 path,
#                 *args,
#                 **kwargs,
#             )

#         if f == FF.EXCEL_WORKBOOK:
#             cls.excel(
#                 df,
#                 path,
#                 *args,
#                 **kwargs,
#             )

#         if f == FF.PICKLE:
#             cls.pkl(
#                 df,
#                 path,
#                 *args,
#                 **kwargs,
#             )

#         if f == FF.DB:
#             cls.db(
#                 df,
#                 path,
#                 *args,
#                 **kwargs,
#             )

#     @staticmethod
#     def csv(
#         df: pd.DataFrame,
#         path: Path_,
#         *args,
#         index=False,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_csv(path)
#         if not ok:
#             return
#         PM.prepare_dir(path)
#         df.to_csv(
#             path,
#             *args,
#             **kwargs,
#             index=index,
#         )

#     @staticmethod
#     def excel(
#         df: pd.DataFrame,
#         path: Path_,
#         *args,
#         index=False,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_excel(path)
#         if not ok:
#             return
#         PM.prepare_dir(path)
#         df.to_excel(
#             path,
#             *args,
#             **kwargs,
#             index=index,
#         )

#     @staticmethod
#     def pkl(
#         df: pd.DataFrame,
#         path: Path_,
#         *args,
#         index=False,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_pkl(path)
#         if not ok:
#             return
#         PM.prepare_dir(path)
#         df.to_pickle(
#             path,
#             *args,
#             **kwargs,
#             index=index,
#         )

#     @staticmethod
#     def db(
#         df: pd.DataFrame,
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_db(path)
#         if not ok:
#             return
#         ...


# import pandas as pd

# from ... import FileFormat as FF
# from .. import Path_
# from .. import PathManager as PM


# class DFReader:
#     def __call__(
#         self,
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         return self.read(
#             path,
#             *args,
#             **kwargs,
#         )

#     @classmethod
#     def read(
#         cls,
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         f = DF.get_fmt(path)
#         if f is None:
#             return

#         f = f.name

#         if f == FF.CSV:
#             df = cls.csv(
#                 path,
#                 *args,
#                 **kwargs,
#             )
#             return df

#         if f == FF.EXCEL_WORKBOOK:
#             df = cls.excel(
#                 path,
#                 *args,
#                 **kwargs,
#             )
#             return df

#         if f == FF.PICKLE:
#             df = cls.pkl(
#                 path,
#                 *args,
#                 **kwargs,
#             )
#             return df

#         if f == FF.DB:
#             df = cls.db(
#                 path,
#                 *args,
#                 **kwargs,
#             )
#             return df

#     @staticmethod
#     def csv(
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_csv(path)
#         if not ok:
#             return
#         df = pd.read_csv(
#             path,
#             *args,
#             **kwargs,
#         )
#         return df

#     @classmethod
#     def excel(
#         cls,
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_excel(path)
#         if not ok:
#             return
#         df = pd.read_excel(
#             path,
#             *args,
#             **kwargs,
#         )
#         df = cls.remove_unnamed(df)
#         return df

#     @staticmethod
#     def pkl(
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_pkl(path)
#         if not ok:
#             return
#         df = pd.read_pickle(
#             path,
#             *args,
#             **kwargs,
#         )
#         return df

#     @staticmethod
#     def db(
#         path: Path_,
#         *args,
#         **kwargs,
#     ) -> pd.DataFrame:
#         from .. import DFFormats as DF

#         ok = DF.assert_db(path)
#         if not ok:
#             return
#         ...

#     @staticmethod
#     def remove_unnamed(
#         df: pd.DataFrame,
#     ) -> pd.DataFrame:
#         ok = ~(df.columns.str.contains("^Unnamed"))
#         df = df.loc[
#             :,
#             ok,
#         ]
#         return df
