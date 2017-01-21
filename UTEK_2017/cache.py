import pickle

class cache:

    def __init__(self, file_name):
        self.file_name = file_name
        self.exact_cache = {}

    def save_cache(self):
        with open(self.file_name, 'wb') as f:
            pickle.dump(self.exact_cache, f, pickle.HIGHEST_PROTOCOL)

    def load_cache(self):
        with open(self.file_name, 'rb') as f:
            self.exact_cache = pickle.load(f)
