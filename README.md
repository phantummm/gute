# gute

A friendly tool for static content generation.

## usage

```bash
gute [--template templatepath] source target
```

This will take all `*.md` files in `source` directory, and output them as `.html` files in `target` directory. The `--template` or `-t` argument is an optional [jinja2](http://jinja.pocoo.org/) template file into which the files will be inserted.

## installation

To install the command-line program, just run `./install.sh`.

To run the tests:

```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
bin/test
```

## note

This is a silly project started to learn Python.