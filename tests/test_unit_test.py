import pytest
from main import *


@pytest.mark.parametrize('num, res', [('11-2', True), ('10006', True), (10006, False), ('666', False)])
def test_check_document_existance_result(num, res):
    assert check_document_existance(num) is res


def test_get_doc_owner_name_type(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10006')
    assert type(get_doc_owner_name()) is str


def test_doc_owner_name_wrong_data(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '666')
    assert TypeError(get_doc_owner_name())


def test_get_all_doc_owners_names_type():
    assert type(get_all_doc_owners_names()) is set


def test_remove_doc_from_shelf(monkeypatch):
    remove_doc_from_shelf('2207 876234')
    new_dir_values = [item for el in directories.values() for item in el]
    assert '2207 876234' not in new_dir_values


def test_remove_doc_from_shelf_wrong_data():
    assert (remove_doc_from_shelf('666')) is None


def test_add_new_shelf():
    add_new_shelf('4')
    assert '4' in directories.keys()


def test_add_new_shelf_existing_shelf():
    assert add_new_shelf('1') == ('1', False)


@pytest.mark.parametrize('doc_num, shelf_num', [('555', '1'), (777, 2), ('10006', '2')])
def test_append_doc_to_shelf(doc_num, shelf_num):
    append_doc_to_shelf(doc_num, shelf_num)
    assert doc_num in directories[shelf_num]


def test_delete_doc(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10006')
    assert delete_doc() == ('10006', True)


def test_get_doc_shelf(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '11-2')
    assert get_doc_shelf() == '1'


def test_move_doc_to_shelf(monkeypatch):
    inputs = iter(['11-2', '3'])
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    assert move_doc_to_shelf() == ('11-2', '3')


def test_show_all_docs_info():
    assert show_all_docs_info() is None


def test_add_new_doc(monkeypatch):
    inputs = iter(['111', 'passport', 'Alex', '1'])
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    assert add_new_doc() == '1'
