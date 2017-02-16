from ..document import Paper

def init(subparsers):
    """TODO: Docstring for init.

    :subparser: TODO
    :returns: TODO

    """

    # open parser
    open_parser = subparsers.add_parser("open",
            help="Open paper document from a given library")
    open_parser.add_argument("paper",
            help="Paper search",
            nargs="?",
            default=".",
            action="store")

def main(config, args):
    """
    Main action if the command is triggered

    :config: User configuration
    :args: CLI user arguments
    :returns: TODO

    """
    papersDir = os.path.expanduser(config[args.lib]["dir"])
    printv("Using directory %s"%papersDir)
    paperSearch = args.paper
    folders = getFolders(papersDir)
    folders = filterPaper(folders, paperSearch)
    paper   = Paper(folders[0])
    openFile(paper.getFile(), config)
