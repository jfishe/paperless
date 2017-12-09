#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `paperless` package."""

import pytest # type: ignore

from click.testing import CliRunner # type: ignore

from paperless import paperless
from paperless import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    response = 'Usage: main [OPTIONS] XML_INPUT'
    assert response in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    response = """Usage: main [OPTIONS] XML_INPUT

  Console script for paperless.

Options:
  --output TEXT           Todoist CSV task file
  --template TEXT         Todoist exported template
  --drop_duplicates TEXT  Remove duplicate Paperless tasks
  --help                  Show this message and exit."""
    assert help_result.exit_code == 0
    assert response in help_result.output
