# About

In production, even simple scripts are hard. If you miss a divide by zero case, everything will break when that case happens. Someone won't see that one argument you forgot to make required on the CLI and everything will break when a null value gets pushed. You'll forget to timestamp some of your output lines and then, when something goes wrong, you won't be able to correlate logs to real events and you'll be stuck guessing.

Python can help! It's easy to write Python scripts that have the features to support the rigor of production:

* Automated tests for multiple platforms.
* A command that runs on the shell like any other command. No specific working directory or special invocation required.
* Command line sanity like a `--help` option and enforcement of required arguments.
* A `--simulate` option.
* Informative log output.
  * Prefixes on your log events showing when you're in simulate mode.
  * Log events from other libraries (e.g. boto3) filtered to the same log level set for your script.
  * Output structured in JSON objects. JSON is cleaner to ingest than formatted strings and modern logging tools all support it (including AWS CloudWatch Logs).
* An easy way to build and package.
* An easy way to install without a git clone.

This project provides a demo of how to write production-ready scripts with these features. It also includes an example of a script that *isn't* ready, so you can compare them.

I've found that [tracking code coverage can hurt projects][coverage] and that [Python's style guide (PEP8) can be wasteful][pep8], especially for scripts (vs applications). However, this demo is written so you can copy/paste and tweak it. Many projects enforce coverage and PEP8, so this does the same to minimize the changes you'll need to implement.

# User Guide

This is pip-installable so any of the usual Python build and install patterns should work.

## Contributing

Check out the [contributing guide](CONTRIBUTING.md).

## Pip-Installability

This project is pip-installable because that's the way I write all my Python projects. I find it's a clean standard to follow. However, it would be entirely reasonable to use a `requirements.txt` file and a flat module instead:

* Replace `setup.py` with a `requirements.txt`.
* Update the tox config to [install from `requirements.txt`][tox requirements].
* Replace the `entry_point()` method with an `if __name__ == '__main__'` condition in the script module.

## Packaging, Distributing, and Installing

Here's an approach I like:

1. Build a [wheel][wheel].

   ```shell
   pip install wheel
   python setup.py bdist_wheel
   ```

1. Distribute the wheel file from the `dist` folder:

   ```shell
   dist/python_production_script_recipe-1.0.0-py3-none-any.whl
   ```

1. Install the wheel with pip.

   ```shell
   pip install python_production_script_recipe-1.0.0-py3-none-any.whl
   ```

1. Run the script with its console script:

   ```shell
   sample-script-good --help
   ```

You should use a [venv][venv], and if you need to call this from another script (or maybe a `cron` job), you can avoid having to `activate` the env by calling the executable directly from the env's `bin` (one of the awesome reasons to use `console_scripts`):

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
[pep8]: https://github.com/operatingops/simple_style/blob/v0.2.0/SIMPLE_STYLE.md
[pex]: https://github.com/pantsbuild/pex
[pyenv]: https://github.com/pyenv/pyenv
[pypi]: https://pypi.python.org/pypi
[tox requirements]: http://tox.readthedocs.io/en/2.7.0/example/basic.html#depending-on-requirements-txt
[venv]: https://docs.python.org/3/library/venv.html
[wheel]: http://pythonwheels.com
