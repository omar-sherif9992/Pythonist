class FileManger:
    def read_file(self, path: str) -> str:
        '''reads a file and returns its content'''
        with open(path, 'r') as f:
            return f.read()
