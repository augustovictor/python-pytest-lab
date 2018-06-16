import pytest
import os
import json

def read_cheese_prefs():
    full_path = os.path.expanduser('~/python-pytest-lab/.cheese.json')
    
    with open(full_path, 'r') as f:
        prefs = json.load(f)
        return prefs