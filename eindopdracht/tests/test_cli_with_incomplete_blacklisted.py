from loupe.cli import CLI
import pytest

def test_cli_with_incomplete_blacklisted_command(monkeypatch, capsys):
    # Arrange the arguments for Monkeypatch
    test_args = [
        'dataset.json', 
        'blacklisted',
        '--src',
        '192.168.0.1',
        '--srcport',
        '37664',
        # '--dst', # commented out on purpose for testing
        # '192.168.0.34',
        '--dstport',
        '443'
        ]

    # Use the cli args, the main function into the app and the above args for Monkeypatch
    monkeypatch.setattr('sys.argv', ['loupe.py'] + test_args)

    # Act and Assert
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cli = CLI()  # Call the CLI class
        args = cli.parse_args()  # This should raise a SystemExit due to incomplete arguments

    # Check if system exit was due to incorrect arguments
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2  # exit code 2 is typically due to incorrect arguments

    # Check for correct error message
    out, err = capsys.readouterr()
    assert 'error: the following arguments are required: --dst/-d' in err
