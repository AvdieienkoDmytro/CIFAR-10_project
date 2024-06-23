import logging
import tarfile
import urllib.request
from pathlib import Path


logger = logging.getLogger(__name__)


class DatasetManager:
    DATASET_FILENAME = "dataset.tar.gz"

    def __init__(self, url: str, destination_folder: Path):
        self.url = url
        if not destination_folder.is_dir():
            raise ValueError(
                f"destination_folder must be a directory: {destination_folder}"
            )
        self.destination_folder = destination_folder

    def download(self) -> bool:
        if not self.destination_folder.exists():
            self.destination_folder.mkdir(parents=True, exist_ok=True)
        logger.info(
            f"downloading dataset: url={self.url}, "
            f"destination_folder={self.destination_folder}"
        )
        try:
            urllib.request.urlretrieve(
                self.url,
                self.destination_folder / self.DATASET_FILENAME
            )
        except Exception as e:
            logger.error(f"downloading dataset error: error={e}")
            return False
        return True

    def extract(self) -> bool:
        logger.info(
            f"extracting dataset: destination_folder={self.destination_folder}"
            )
        try:
            with tarfile.open(
                    self.destination_folder / self.DATASET_FILENAME,
                    "r:gz") as tar:
                tar.extractall(path=self.destination_folder)
        except Exception as e:
            logger.error(f"extracting dataset error: error={e}")
            return False
        return True


if __name__ == "__main__":
    url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    destination_folder = Path(__file__) / "data"
    dataset_manager = DatasetManager(url, destination_folder)
    if dataset_manager.download() and dataset_manager.extract():
        print("Download and extraction complete.")
    else:
        print("Download and extraction failed.")
