import pickle

class cache:

    def __init__(self, file_name):
        self.file_name = file_name
        self.exact_cache = {}


    def add_distance_and_time(self,p1,p2,d,t):
        if (p1,p2) in self.exact_cache:
            #print(d,t)
            return (d,t)
        else:
            self.exact_cache[(p1,p2)] = (d,t)

    def save_cache(self):
        with open(self.file_name, 'wb') as f:
            pickle.dump(self.exact_cache, f, pickle.HIGHEST_PROTOCOL)

    def load_cache(self):
        with open(self.file_name, 'rb') as f:
            self.exact_cache = pickle.load(f)




y = cache('data.pickle')
y.load_cache()


y.add_distance_and_time(1,2,44,55)
y.add_distance_and_time(11234,331232,42224,55555)
y.add_distance_and_time(1,2,44,55)

for pair in y.exact_cache:
    print(pair)
