# Test Suite

This is a smart contract test suite.

## Usage

To run the tests for the first time, run the following:

```
$ make all
$ pip install -r requirements.txt
$ pytest
```

Note: we *strongly* recommend you use Python virtual environments.
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) is an
excellent package for easily managing virtualenvs.

If you're running Arch you'll need to install libsecp256k1 or `pip install...`
will fail. Install it with:

```
$ pacman -S libsecp256k1
```

### Compiling

This project uses a Makefile to compile smart contracts.

In the Makefile, `SOLIDITY_CONTRACTS` is a list of filenames to be compiled.
These contracts should be found in the `SOURCE_DIR` and the artifacts from
their compilation will be placed in the `BUILD_DIR` (which is generally
`./build`).

If you need to compile (or re-compile) the smart contracts, simply run:

`$ make all`.

### Running Tests

It is not necessary to compile the contracts before each test. To run a set of
tests, simply run:

```
$ pytest
```

Check out the [pytest package](https://docs.pytest.org/en/latest/) for more
info.

## Notes

By default, pytest hides the output of print statements. To see them during
testing, use the `-s` switch: `$ pytest -s`.

For a more detailed test output, use the `-v` switch.


