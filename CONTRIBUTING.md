# Contributing

This guide based on the one in [factory_girl_rails v4.8.0][source]. Thanks Thoughtbot!

## Conduct

We'd love for you to contribute, and we want you to be you while you do it. This project follows a few rules that we hope will make contributing a good experience for everyone. These rules are just a framework; they're here to help you understand how the project works. Each contributor is responsible for their conduct.

* Be professional.
* The project's maintainers manage the project. You (hopefully!) contribute. Don't try to manage the project or the people working on it unless a current maintainer specifically asks you to.
* Only use the project to work on the project. Take non-project conversations and activities somewhere else.
* Contribute your own work. If you use someone else's work:
  * Make sure it has a non-viral (e.g. no GNU) license that allows you to use it on this project.
  * Credit them where you use their work (e.g. with a link in a comment).

## Code

The tests run against several Python versions. Check out [pyenv][pyenv] for an easy way to install them all.

As always, you should use a [venv][venv].

1. [Fork and clone the repo][fork].

1. Create a feature branch:

   ```shell
   git checkout -b my_feature
   ```

1. Use pip's editable mode and install the `testing` extras:

   ```shell
   pip install -e .[testing]
   ```

1. Make your change. Add tests for your change.

1. Run the tests with tox:

   ```shell
   tox
   ```

1. Run the script with its console script (see `setup.py`):

   ```shell
   sample-script-good --help
   ```

1. Push to your fork.

   ```shell
   git push origin my_feature
   ```

1. [Create a Pull Request][pr].

At this point you're waiting on us. Remember, you get the SLA you pay for and we don't get paid so we might not respond
right away. We look for the right fix over a quick fix, and we may suggest some changes or improvements or alternatives.

To increase the chance that your pull request gets accepted:

* Write tests.
* Follow [Simple Style][style].
* Write [good commit messages][commits].
* Organize your commits. "Fix typo" and "work in progress" commits are hard to follow. If you like to commit often,
  check out git's [rebase][rebase]. You can use it to clean up at the end.

## Issues

The issue tracker is for project changes. Bugfixes, improvements, etc. If you need help, check out
[operatingops.org][home] instead of submitting an issue.

Write everything you know. Think of the questions we might ask and write the answers. Some great things to include:

  1. What you expected to happen, and why.
  2. What happened that was different from your expectations, and why, if you have any theories.
  3. Whether or not you can contribute a fix.

Like for pull requests, remember that we don't get paid so there's no SLA. We'll respond quickly if we can, though.

[conduct]: https://www.ubuntu.com/about/about-ubuntu/conduct
[commits]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[fork]: https://help.github.com/articles/fork-a-repo/
[home]: https://operatingops.org
[pr]: https://help.github.com/articles/creating-a-pull-request/
[pyenv]: https://github.com/pyenv/pyenv
[rebase]: https://help.github.com/articles/about-git-rebase/
[source]: https://github.com/thoughtbot/factory_girl_rails/blob/v4.8.0/CONTRIBUTING.md
[style]: https://github.com/operatingops/simple_style/blob/v0.2.1/SIMPLE_STYLE.md
[venv]: https://docs.python.org/3/library/venv.html
