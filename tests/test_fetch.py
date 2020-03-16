from minerva import Client


def test_fetch_data(variables):
    client = Client(user=variables['user'], password=variables['password'])
    data = client.fetch(
        'marketdata?sector=information_technology&begin=2020-01-10&end=2020-02-20&start=0&size=20')

    assert len(data['hits']) == 20

    data = client.fetch(
        'fundamentaldata?&sector=information_technology&sheet=balance&begin=2018-03-10&end=2020-03-10&start=0&size=10')

    assert len(data['hits']) > 0
