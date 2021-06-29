class CustomIdent(str):
    def __init__(self, ident: str):
        super(CustomIdent, self).__new__(str, ident)
