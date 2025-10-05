import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_anonymizer_replaces_person():
    text = "My name is Bond."
    start, end = 11, 15

    result = sample_run_anonymizer(text, start, end)

    assert result.text == "My name is BIP."
    assert len(result.items) == 1
    item = result.items[0]
    assert item.start == 11
    assert item.end == 14
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
