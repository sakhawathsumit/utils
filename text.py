import io


class Text:
    def __init__(self):
        """
        Constructor of Text class.
        """
    def read(self, path=None, strip_by=None, split_by=None, encoding=None):
        """
        Read .txt file.

        Args:
            path (str) : Text file path.
            strip_by (str) : Characters to strip from beginning and the end of the file.
            split_by (str) : Character to separate the file in list.
            encoding (str) : Encoding type (eg. 'utf-8')

        Returns:
            txt : str if 'split_by=None' otherwise list of str. 
        """
        with io.open(path, mode='r', encoding=encoding) as f:
            txt = f.read()
            if strip_by:
                txt = txt.strip(strip_by)
            if split_by:
                txt = txt.split(split_by)
        return txt