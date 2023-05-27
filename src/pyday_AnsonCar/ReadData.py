import sqlite3
import pandas as pd


class ReadData():
    fileName: str
    fileFormat: str
    df: pd.core.frame.DataFrame

    def __init__(self, fileName: str, *filetable: str):
        self.fileName = fileName
        self.fileFormat = fileName.split(".")[-1]
        self.filetable = filetable[0] if filetable else ""
        self.df = pd.DataFrame(self.input())

    def __str__(self):
        return self.table().to_string()

    def __repr__(self):
        return self.table().to_string()

    # setter
    # 輸入
    def input(self):
        if self.fileFormat == "db":
            return pd.read_sql_query(f"SELECT * FROM {self.filetable}", sqlite3.connect(self.fileName))
        elif self.fileFormat == "csv":
            return pd.read_csv(self.fileName)
        elif self.fileFormat == "json":
            return pd.read_json(self.fileName)
        elif self.fileName == "xlsx":
            return pd.read_excel(self.fileName)
        else:
            return print("input: Does not support ")

    # 輸出
    def output(self, file: str):
        file = file.split(".")
        name = file[0]
        format = file[-1]
        if format.lower() == "all":
            self.df.to_csv(f"{name}.csv", index=False)
            self.df.to_json(f"{name}.json")
            self.df.to_excel(f"{name}.xlsx")
        elif format == "csv":
            self.df.to_csv(f"{name}.csv", index=False)
        elif format == "json":
            self.df.to_json(f"{name}.json")
        elif format == "xlsx":
            self.df.to_excel(f"{name}.xlsx")
        else:
            print("output: Does not support ")

    # getter
    def name(self) -> str:
        return self.fileName

    def format(self) -> str:
        return self.fileFormat

    def table(self) -> pd.core.frame.DataFrame:
        return self.df
