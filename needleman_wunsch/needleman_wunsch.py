def needleman_wunsch(seq1, seq2, match=1, mismatch=0, gap=0):
    """
    Basic implementation of Needleman-Wunsch.
    Returns an alignment and a score.
    A version using numpy will be written later.
    This function returns one example of a possible alignment, but several optimal alignments may be possible.
    """
    m, n = len(seq1), len(seq2)

    # TODO: this is a basic approach using a list of lists and can be improved
    matrix = [[0] * (m + 1) for index in range(n + 1)]

    for i in range(n + 1):
        matrix[i][0] = i * gap
    for j in range(m + 1):
        matrix[0][j] = j * gap

    # Scoring
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score_i_j = match if seq2[i - 1] == seq1[j - 1] else mismatch
            max_score = max(
                matrix[i - 1][j] + gap,
                matrix[i][j - 1] + gap,
                matrix[i - 1][j - 1] + score_i_j,
            )
            matrix[i][j] = max_score

    final_score = matrix[n][m]

    # Backtracking
    i = n
    j = m

    aligned_seq_1 = ""
    aligned_seq_2 = ""

    while i > 0 and j > 0:
        current_score = matrix[i][j]
        diag_score = matrix[i - 1][j - 1]
        left_score = matrix[i][j - 1]
        up_score = matrix[i - 1][j]
        match_score = match if seq2[i - 1] == seq1[j - 1] else mismatch

        if current_score == diag_score + match_score:
            aligned_seq_1 = seq1[j - 1] + aligned_seq_1
            aligned_seq_2 = seq2[i - 1] + aligned_seq_2
            i = i - 1
            j = j - 1
        elif current_score == left_score + gap:
            aligned_seq_1 = seq1[j - 1] + aligned_seq_1
            aligned_seq_2 = "-" + aligned_seq_2
            j = j - 1
        elif current_score == up_score + gap:
            aligned_seq_1 = "-" + aligned_seq_1
            aligned_seq_2 = seq2[i - 1] + aligned_seq_2
            i = i - 1
    # TODO: a better logic could be written to avoid code duplication
    while i > 0:
        aligned_seq_1 = "-" + aligned_seq_1
        aligned_seq_2 = seq2[i - 1] + aligned_seq_2
        i = i - 1
    while j > 0:
        aligned_seq_1 = seq1[j - 1] + aligned_seq_1
        aligned_seq_2 = "-" + aligned_seq_2
        j = j - 1

    return aligned_seq_1, aligned_seq_2, final_score
