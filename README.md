# About

Production is hard. Even a simple script that looks up queue state and sends it to an API gets complex in prod. Without tests, the divide by zero case you missed will mask queue overloads. Someone won't see that required argument you didn't enforce and break everything when they accidentally publish a null value. You'll forget to timestamp one of your output lines and then when the queue goes down you won't be able to correlate queue status to network events.

Python can help! Out of box it can give you essential but often-skipped features, like these:

* Automated tests for multiple platforms.
* A `--simulate` option.
* Command line sanity like a `--help` option and enforcement of required arguments.
* Informative log output.
* An easy way to build and package.
* An easy way to install a build without a git clone.
* A command that you can just run like any other command. No weird shell setup or invocation required.

It can be a little tricky, though, if you haven't already done it. This project demonstrates it for you. It includes an example of a script that *isn't* ready for prod.

Tracking code coverage and PEP8 compliance can be [bad][coverage] [ideas][pep8]. However, this project is written so you can copy/paste and tweak it. Since many projects enforce coverage and PEP8, this project does the same to minimize the changes needed to get it working in more rigid repos. That's the only reason those features are enabled. It's entirely reasonable to remove them, you'd still meet the production readiness requirements demonstrated here.

[coverage]: https://operatingops.org/2016/11/25/why-i-dont-track-test-coverage/
[pep8]: https://github.com/operatingops/simple_style/blob/v0.1.0/SIMPLE_STYLE.md

# Building and Installing

This is pip-installable so any of the usual Python build and install patterns should work. If you don't want pip-installability it's entirely reasonable to replace the `setup.py` with a `requirements.txt` and the `entry_point()` method with an `if __name__ == '__main__'` condition.

## Development and Testing

Use pip's editable mode and install the `testing` extras:

    pip install -e .[testing]

## Production

One great approach for Python 3 is this:

    pip install wheel
    python setup.py bdist_wheel

That'll create a pip-installable wheel you can distribute, like this:

    dist/python_production_script_recipe-0.2.0-py3-none-any.whl

For a level up beyond just what Python can give you, check out these:

* [PEX](https://github.com/pantsbuild/pex). A tool that'll give you an executable binary you can copy to a system path like `/usr/local/bin`. Useful if you have third party Python dependencies that you want to bundle together so you don't depend on [PyPI](https://pypi.python.org/pypi) for installs.
* [FPM](https://github.com/jordansissel/fpm). A tool that'll help you bundle into a `.deb` or `.rpm`. Useful if your script requires a system package (e.g. `lib-obscure-dev`).

# Running

If you're in a Python environment where this is installed, just use the entry point defined in `setup.py`:

    sample-script-good --help

Like most folks, you will probably install to a [venv](https://docs.python.org/3/library/venv.html) (Python 3) or a [virtualenv](https://virtualenv.pypa.io/en/stable/) (Python 2). If you're are calling this from another script or a `cron` job, you can avoid having to call the `activate` script by running the executable from the env's `bin`:

    /path/to/virtualenv/bin/sample-script-good --help

# Running Tests

The tests run against Python 2.7 and Python 3.6, so you'll need both installed. Check out [pyenv](https://github.com/pyenv/pyenv) for an easy way.

    tox

# Contributing

Check out the [contributing guide](CONTRIBUTING.md).
