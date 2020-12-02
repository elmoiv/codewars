class FileNameExtractor:
    def extract_file_name(d):
        return d.split('_', 1)[1].rsplit('.', 1)[0]
