# About

Production is hard. Even a simple script that looks up queue state and sends it to an API gets complex in prod. Without
tests, the divide by zero case you missed will mask queue overloads. Someone won't see that required argument you didn't
enforce and break everything when they accidentally publish a null value. You'll forget to timestamp one of your output
lines and then when the queue goes down you won't be able to correlate queue status to network events.

Python can help! Out of box it can give you essential but often-skipped features, like these:

* Automated tests for multiple platforms.
* A `--simulate` option.
* Command line sanity like a `--help` option and enforcement of required arguments.
* Informative log output.
  * Prefixes on your log events showing when you're in simulate mode.
  * Log events from other libraries (e.g. boto3) filtered to the same log level set for your script.
* An easy way to build and package.
* An easy way to install a build without a git clone.
* A command that you can just run like any other command. No weird shell setup or invocation required.

It can be a little tricky, though, if you haven't already done it. This project demonstrates it for you. It includes an
example of a script that *isn't* ready for prod.

Tracking code coverage and PEP8 compliance can be [bad][coverage] [ideas][pep8]. However, this project is written so you
can copy/paste and tweak it. Since many projects enforce coverage and PEP8, this project does the same to minimize the
changes needed to get it working in more rigid repos. That's the only reason those features are enabled. It's entirely
reasonable to remove them, you'd still meet the production readiness requirements demonstrated here.

# User Guide

This is pip-installable so any of the usual Python build and install patterns should work. If you don't want
pip-installability it's entirely reasonable to remove it:

* Replace `setup.py` with a `requirements.txt`.
* Update the tox config to [install from `requirements.txt`][tox requirements].
* Replace the `entry_point()` method with an `if __name__ == '__main__'` condition.

## Development

The tests run against Python 2.7 and Python 3.6, so you'll need both installed to run the tests. Check out
[pyenv][pyenv] for an easy way.

As always, you should use a [venv][venv] (Python 3) or a [virtualenv][virtualenv] (Python 2).

1. Use pip's editable mode and install the `testing` extras:

   ```shell
   pip install -e .[testing]
   ```

1. Run the tests with tox:

   ```shell
   tox
   ```

1. Run the script with its console script (see `setup.py`):

   ```shell
   sample-script-good --help
   ```

Check out the [contributing guide](CONTRIBUTING.md)!

## Production

One great approach for Python 3 is this:

1. Build a [wheel][wheel].

   ```shell
   pip install wheel
   python setup.py bdist_wheel
   ```

1. Distribute the wheel file from the `dist` folder:

   ```shell
   dist/python_production_script_recipe-0.2.0-py3-none-any.whl
   ```

1. Install the wheel with pip.

   ```shell
   pip install python_production_script_recipe-0.2.0-py3-none-any.whl
   ```

1. Run the script with its console script:

   ```shell
   sample-script-good --help
   ```

You should use a [venv][venv] or a [virtualenv][virtualenv] in production, and if you need to call this from another
script (or maybe a `cron` job), you can avoid having to `activate` the env by calling the executable directly from the
env's `bin` (one of the awesome reasons to use `console_scripts`):

   ```shell
   /path/to/env/bin/sample-script-good --help
   ```

For a level up beyond just what Python can give you, check out these:

* [PEX][pex]. A tool that'll give you an executable binary you can copy to a system path like `/usr/local/bin`.
  Useful if you have third party Python dependencies that you want to bundle together so you don't depend on
  [PyPI][pypi] for installs.
* [FPM][fpm]. A tool that'll help you bundle into a `.deb` or `.rpm`. Useful if your script requires a system package
  (e.g. `lib-obscure-dev`).


[coverage]: https://operatingops.org/2016/11/25/why-i-dont-track-test-coverage/
[fpm]: https://github.com/jordansissel/fpm
[pep8]: https://github.com/operatingops/simple_style/blob/v0.1.0/SIMPLE_STYLE.md
[pex]: https://github.com/pantsbuild/pex
[pyenv]: https://github.com/pyenv/pyenv
[pypi]: https://pypi.python.org/pypi
[tox requirements]: http://tox.readthedocs.io/en/2.7.0/example/basic.html#depending-on-requirements-txt
[venv]: https://docs.python.org/3/library/venv.html
[virtualenv]: https://virtualenv.pypa.io/en/stable/
[wheel]: http://pythonwheels.com
