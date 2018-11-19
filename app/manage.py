"""
Main module of the server file
"""

# 3rd party modules
import unittest
import argparse
from config.server import app


def run():
    app.run(debug=True)


def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    commands = dict(run=run, test=test)
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=commands.keys())
    commands[parser.parse_args().command]()
