import pytest
import json

@pytest.mark.smoke
def test_author_1_from_boston(author_file_json):
    with author_file_json.open() as f:
        authors = json.load(f)
        assert authors['Author1']['city'] == 'Boston'

def test_all_have_city_attribute(author_file_json):
    with author_file_json.open() as f:
        authors = json.load(f)

        for a in authors:
            print(authors[a])
            assert len(authors[a]['city']) > 0