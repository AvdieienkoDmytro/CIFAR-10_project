import os
import urllib.request
import tarfile


def download_and_extract_cifar10(destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    filename = os.path.join(destination_folder, "cifar-10-python.tar.gz")

    if not os.path.exists(filename):
        print("Downloading CIFAR-10 dataset...")
        urllib.request.urlretrieve(url, filename)
        print("Download complete.")

    with tarfile.open(filename, "r:gz") as tar:
        print("Extracting CIFAR-10 dataset...")
        tar.extractall(path=destination_folder)
        print("Extraction complete.")


download_and_extract_cifar10("data")
