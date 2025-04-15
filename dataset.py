from keras import utils
import polars
from utils import read_bytes

class MalwareDataset(utils.PyDataset):
    def __init__(
        self,
        file_path: str,
        workers: int = 10,
        use_multiprocessing: bool = True,
        max_queue_size: int = 10
    ):
        super().__init__(workers, use_multiprocessing, max_queue_size)
        self.__metadata = polars.read_csv(file_path)

    def __len__(self):
        return len(self.__metadata)

    def __getitem__(self, index: int):
        path, y = self.__metadata.row(index)
        train = read_bytes(path)
        return (train,y)        