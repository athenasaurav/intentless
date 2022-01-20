import pytest
from pathlib import Path

from haystack.utils.preprocessing import convert_files_to_dicts, tika_convert_files_to_dicts
from haystack.utils.cleaning import clean_wiki_text
from haystack.utils.augment_squad import augment_squad
from haystack.utils.squad_data import SquadData


def test_convert_files_to_dicts():
    print(Path(__file__).parent/"samples")
    documents = convert_files_to_dicts(dir_path=(Path(__file__).parent/"samples").absolute(), clean_func=clean_wiki_text, split_paragraphs=True)
    assert documents and len(documents) > 0

@pytest.mark.tika
def test_tika_convert_files_to_dicts():
    documents = tika_convert_files_to_dicts(dir_path=Path(__file__).parent/"samples", clean_func=clean_wiki_text, split_paragraphs=True)
    assert documents and len(documents) > 0

def test_squad_augmentation():
    input_ = Path(__file__).parent/"samples"/"squad"/"tiny.json"
    output = Path(__file__).parent/"samples"/"squad"/"tiny_augmented.json"
    glove_path = Path(__file__).parent/"samples"/"glove"/"tiny.txt" # dummy glove file, will not even be use when augmenting tiny.json
    multiplication_factor = 5
    augment_squad(model="distilbert-base-uncased", tokenizer="distilbert-base-uncased", squad_path=input_, output_path=output,
                    glove_path=glove_path, multiplication_factor=multiplication_factor)
    original_squad = SquadData.from_file(input_)
    augmented_squad = SquadData.from_file(output)
    assert original_squad.count(unit="paragraph") == augmented_squad.count(unit="paragraph") * multiplication_factor
