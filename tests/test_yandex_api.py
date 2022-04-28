import pytest
from yandex import YaUploader


def test_create_folder_201():
    assert YaUploader('AQAAAAAJWqZyAADLW3nkQ7gzq0uQhGkeR3fuGEg', 'folder1').create_folder() == 201


@pytest.mark.parametrize('response', [409, 400, 401, 403, 404, 406, 423, 429, 503, 507])
def test_create_folder(response):
    assert YaUploader('AQAAAAAJWqZyAADLW3nkQ7gzq0uQhGkeR3fuGEg', 'folder2').create_folder() != response









