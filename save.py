import pickle

def save_variables(variables, filename):
    with open(filename, 'wb') as f:
        pickle.dump(variables, f, pickle.HIGHEST_PROTOCOL)

def load_variables(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)