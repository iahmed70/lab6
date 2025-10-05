import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_anonymizer_replaces_person():
    # Given / When
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Then
    assert result.text == "My name is BIP."
    assert len(result.items) == 1
    assert result.items[0].start == 11
    assert result.items[0].end == 14
    assert result.items[0].entity_type == "PERSON"
    assert result.items[0].text == "BIP"
    assert result.items[0].operator == "replace"
