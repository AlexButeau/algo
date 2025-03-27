import pytest
from needleman_wunsch import needleman_wunsch


@pytest.mark.parametrize(
    "seq1, seq2, expected_alignment1, expected_alignment2, expected_score",
    [
        ("ACG", "AG", "ACG", "A-G", 2),
        ("AG", "ACG", "A-G", "ACG", 2),
        ("GATT", "GTA", "GATT", "G-TA", 2),
        ("AAA", "GGG", "AAA", "GGG", 0),
    ],
)
def test_needleman_wunsch(
    seq1, seq2, expected_alignment1, expected_alignment2, expected_score
):
    alignment1, alignment2, score = needleman_wunsch(seq1, seq2)
    assert alignment1 == expected_alignment1
    assert alignment2 == expected_alignment2
    assert score == expected_score


def test_empty_sequences():
    seq1 = ""
    seq2 = ""
    aligned_seq_1, aligned_seq_2, score = needleman_wunsch(seq1, seq2)
    assert aligned_seq_1 == ""
    assert aligned_seq_2 == ""
    assert score == 0


def test_with_mismatch_penalty():
    seq1 = "GATTACA"
    seq2 = "GACTATA"
    aligned_seq_1, aligned_seq_2, score = needleman_wunsch(seq1, seq2, mismatch=-1)
    assert aligned_seq_1 == "GA-T-TACA"
    assert aligned_seq_2 == "GACTAT--A"
    assert score == 5


def test_custom_scores():
    seq1 = "AGCT"
    seq2 = "CGT"
    aligned_seq_1, aligned_seq_2, score = needleman_wunsch(
        seq1, seq2, match=2, mismatch=-1, gap=-2
    )
    assert aligned_seq_1 == "AGCT"
    assert aligned_seq_2 == "CG-T"
    assert score == 1
