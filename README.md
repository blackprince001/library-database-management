# Library Management Database

This repo serves as a presentation demo for my end of semester Data Structures & Algorithms class Project. All future commits will only contain the relevant additions to scale this to a working GUI application. If you want to contribute to that, make a pull request, and let's create magic.

## Structure of Database

![database structure](assets/database_structure.jpg)

This may or may not have been updated during the course of project implementation.

## Structure of the project

```bash

.
├── app.py
├── assets
│   └── database_structure.jpg
├── books.json
├── library.db
├── manager
│   ├── database
│   │   ├── core.py
│   │   ├── crud
│   │   │   ├── author.py
│   │   │   ├── book.py
│   │   │   ├── borrowed_book.py
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── schemas
│   │       ├── author.py
│   │       ├── book.py
│   │       ├── __init__.py
│   │       ├── library.py
│   │       └── users.py
│   ├── __init__.py
│   ├── main.py
│   ├── security.py
│   └── utils
│       ├── book_metadata_parser.py
│       └── __init__.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py
    ├── crud
    │   ├── __init__.py
    │   ├── test_author.py
    │   ├── test_book.py
    │   ├── test_borrowed_book.py
    │   └── test_load_book_metadata.py
    └── __init__.py

8 directories, 33 files

```

## Quick Start

- Clone the repository

    ```bash
    git clone https://github.com/blackprince001/library-database-management
    ```

- Move into the directory

    ```bash
    cd library-database-management
    ```

- Set up a virtual environment with [Pipenv](https://pipenv.pypa.io/en/latest/index.html) and install the project dependencies (from the `Pipfile.lock` file to ensure deterministic builds)

  ```bash
  pipenv sync
  ```

- If you get `ModuleNotFoundError: No module named 'manager'`, you need to inject the package into `PYTHONPATH`.
One of the ways to so is to put the following code at the very beginning of `manager/main.py`

  ```python
  import sys
  from pathlib import Path
  
  sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
  ```

- For the lazy ones like me do not have pipenv install, just use the requirements.txt and download the dependencies to your path package path.
  
  ```bash
    python -m pip install -r requirements.txt
  ```

  while you're in `/dsa-library-management`

## Running the program

After making sure all required dependencies are installed, run the `app.py` in the parent directory of this repository. This should provide a terminal interface of the Database API capabilities to future work.

  ```python
  python3 app.py
  ```

## Terminal Interface

![Terminal Interface](assets/screenshot.png)

### Testing

To run the tests in the project:

- You need to install the dev packages:

  ```bash
  pipenv sync --dev
  ```
  
- Run pytest

  ```bash
  pipenv run pytest
  ```
