# tests/test_app.py
# import io
# import sys
# import pytest

from app import main


def test_main_output(capsys):
    # Capture stdout from main()
    main()
    captured = capsys.readouterr()
    assert "Hello from GitHub Secure CI/CD POC!" in captured.out
