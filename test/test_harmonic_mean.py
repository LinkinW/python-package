#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from imppkg.harmony import main
from termcolor import colored

import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        (["1", "4", "4"], 2.0),
        ([], 0.0),
        (["xxx"], 0.0),
    ]
)
def test_harmony_happy_path(input, expected, monkeypatch, capsys):
    inputs = input
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)
    main()
    expected_value = expected
    assert capsys.readouterr().out.strip() == colored(
        expected_value,
        "red",
        "on_cyan",
        attrs=["bold"]
    )
