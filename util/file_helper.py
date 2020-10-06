from dataclasses import dataclass
import os
import pandas as pd

@dataclass
class FileReader:
    
    context : str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''
    
    def new_file(self) -> str:
        return os.path.join(self.context, self.fname)
    
    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8')
    