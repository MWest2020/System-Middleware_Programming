from loupe.cli import CLI


def test_cli_with_get_flags_command(monkeypatch):
    # Arrange the arguments for Monkeypatch
    test_args = [
        'dataset.json',
        'get',
        '--flags',
        '--src',
        '192.168.0.1',
        '--srcport',
        '37664',
        '--dst',
        '192.168.0.34',
        '--dstport',
        '443'
        ]

    # Use the cli args, the main function into the app and the above args for Monkeypatch
    monkeypatch.setattr('sys.argv', ['loupe.py'] + test_args)

    # Act
    cli = CLI()  # Call the CLI class
    args = cli.parse_args()  # Call parse_args on itself

    # Assert
    # Assert if the args are specified like below
    assert args.filename == 'dataset.json'
    assert args.command == 'get'
    assert args.flags == True
    assert args.src == '192.168.0.1'
    assert args.srcport == '37664'
    assert args.dst == '192.168.0.34'
    assert args.dstport == '443'