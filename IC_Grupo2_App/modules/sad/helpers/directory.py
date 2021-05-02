from imutils import paths


class Directory:
    def list_files(self, directory):
        return list(paths.list_files(directory))
