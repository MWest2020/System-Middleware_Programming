from loupe.cli import CLI

def test_cli_with_filename_and_blacklist_command(monkeypatch):
    #Arrange the arguments for Monkeypatch
    test_args = [
        'dataset.json', 
        'blacklist', 
        '--blacklist_file',
        'blacklisted.json'
        ]
    
    # use the cli args, the main function into the app and the above args fro Monkeypatch
    monkeypatch.setattr('sys.argv',['loupe.py'] + test_args)
    
    #Act
    cli = CLI() #call the CLI class
    args = cli.parse_args() # call parge_args on itself

    #Assert
    # assert if the args are specified like below
    assert args.filename == 'dataset.json'
    assert  args.command == 'blacklist'
    assert args.blacklist_file == 'blacklisted.json' 