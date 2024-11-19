
import hw5

example = [[{'r': 10, 'g': 23, 'b': 52}, {'r': 82, 'g': 3, 'b': 215}],
           [{'r': 30, 'g': 181, 'b': 101}, {'r': 33, 'g': 45, 'b': 205}]]

def test_negate():
    assert hw5.negate(example) == [[{'r': 245, 'g': 232, 'b': 203}, {'r': 173, 'g': 252, 'b': 40}],
                                   [{'r': 225, 'g': 74, 'b': 154}, {'r': 222, 'g': 210, 'b': 50}]]


def test_greyscale():
    assert hw5.greyscale(example) == [[{'r': 28, 'g': 28, 'b': 28}, {'r': 100, 'g': 100, 'b': 100}],
                                      [{'r': 104, 'g': 104, 'b': 104}, {'r': 94, 'g': 94, 'b': 94}]]


def test_upsideDown():
    assert hw5.upsideDown(example) == [[{'r': 30, 'g': 181, 'b': 101}, {'r': 33, 'g': 45, 'b': 205}],
                                       [{'r': 10, 'g': 23, 'b': 52}, {'r': 82, 'g': 3, 'b': 215}]]


def test_mirrorImage():
    assert hw5.mirrorImage(example) == [[{'r': 82, 'g': 3, 'b': 215}, {'r': 10, 'g': 23, 'b': 52}],
                                        [{'r': 33, 'g': 45, 'b': 205}, {'r': 30, 'g': 181, 'b': 101}]]


def test_compress():
    assert hw5.compress(example) == [[{'r': 10, 'g': 23, 'b': 52}]]


def test_decompress():
    assert hw5.decompress([[{'r': 10, 'g': 23, 'b': 52}]]) == [[{'r': 10, 'g': 23, 'b': 52}, {'r': 10, 'g': 23, 'b': 52}],
                                                               [{'r': 10, 'g': 23, 'b': 52}, {'r': 10, 'g': 23, 'b': 52}]]
