from loupe.cli import CLI

def test_cli_with_scan_command_and_output_file(monkeypatch):
    # Arrange the arguments for Monkeypatch
    test_args = [
        'dataset.json',
        'scan',
        '-o',
        'attacks.json'
        ]

    # Use the cli args, the main function into the app and the above args for Monkeypatch
    monkeypatch.setattr('sys.argv', ['loupe.py'] + test_args)

    # Act
    cli = CLI()  # Call the CLI class
    args = cli.parse_args()  # Call parse_args on itself

    # Assert
    # Assert if the args are specified like below
    assert args.filename == 'dataset.json'
    assert args.command == 'scan'
    assert args.output == 'attacks.json'