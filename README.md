# Toy Robot

Terminal interface for moving robot on a table.

## Requirements

Python 2.7

`make requirements.py` or optional `pip install -r requirements/requirements.py`.

## How to start

To start the interface run:

```bash
python command_panel.py
```

The interface will be open until the user enters ctl+c or ctrl+z.

## Development

To test code quality with isort and pycodestyle run:

```bash
make quality
```

To run tests do:

```bash
make run_tests
```

Running `make run_tests` will test quality as well.
