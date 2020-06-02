from urlshort import create_app

#create functions to test functionalities
def test_shorten(client):
    response = client.get('/')
    assert b'Shorten' in response.data #where testing happens, assert assumes is true
    