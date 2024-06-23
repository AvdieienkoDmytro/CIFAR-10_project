# CIFAR-10_project

Neural network project using [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset.

## Installation guide

1. Install required binaries.

    - Python 3.10 or higher

2. Create virtual environment (optional).

    This allows for all dependencies to be located in one place and not to interfere with dependencies on other projects.

    Linux installation:

    ```bash
    python3.10 -m venv .venv
    source .venv/bin/activate
    ```

    Windows installation:

    ```cmd
    python3.10 -m venv .venv
    .venv/Scripts/activate.bat
    ```

    For more detailed info on using venv on your project, see [here](https://docs.python.org/3.10/library/venv.html).

3. Install required libraries.

    ```bash
    python3.10 -m pip install -r requirements.txt
    ```

4. Download CIFAR-10 dataset.

    To automate this process, a file is included in this repository. Just run the file in order to save it:

    ```bash
    python3.10 dataset_manager.py
    ```

## Development

1. In order to add new library:

    - Add it to your local virtual environment

    ```bash
    pip install <library-name>
    ```

    - Add it to requirements.txt **(only do this if you work in virtualenv!)**

    ```bash
    pip freeze >requirements.txt
    ```

## Copyright

Under MIT License. See [LICENSE](LICENSE).

## Authors

Avdieienko Dmytro

Shalaiev Andrii
