# import sineAndCosine as Q1
import Q1

# NOTE: IF you edit this file, your scores will not be considered.



TEST_CASES = {
    1: ([3, 2, 1, 1, 2, 2, 1], [3, 3, 3, 2, 3, 2, 1]),
    2: ([3, 3, 3, 2, 3, 2, 1], [4, 3, 3, 2, 4, 3, 1]),
    3: ([4, 3, 3, 2, 3, 3, 1], [5, 4, 3, 3, 4, 4, 1]),
    4: ([5, 4, 3, 3, 4, 3, 1], [5, 5, 4, 3, 4, 4, 1]),
    5: ([5, 5, 4, 3, 5, 4, 1], [6, 5, 4, 3, 5, 4, 1]),
    6: ([6, 6, 4, 3, 5, 4, 1], [6, 6, 5, 4, 5, 5, 1]),
    7: ([7, 6, 5, 4, 6, 5, 1], [7, 6, 5, 4, 6, 5, 1]),
    8: ([7, 7, 5, 4, 6, 5, 1], [8, 7, 6, 5, 6, 6, 1]),
    9: ([8, 8, 6, 5, 6, 6, 1], [8, 7, 6, 6, 7, 6, 1]),
    10: ([8, 7, 6, 5, 7, 6, 1], [9, 8, 6, 5, 8, 6, 1]),
    11: ([9, 8, 6, 5, 7, 7, 1], [9, 9, 7, 6, 8, 7, 1]),
    12: ([9, 8, 7, 6, 8, 7, 1], [10, 9, 7, 6, 8, 7, 1]),
    13: ([9, 9, 7, 6, 8, 7, 1], [10, 9, 8, 6, 9, 8, 1]),
    14: ([10, 9, 7, 6, 9, 8, 1], [10, 9, 8, 7, 9, 8, 1]),
    15: ([10, 9, 8, 6, 9, 8, 1], [11, 10, 8, 7, 10, 8, 1]),
}

DEGREES = [90, 69, 41, 21, 61, -44, 0]

def test_sine_1():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=1)
    assert result == TEST_CASES[1][0]

def test_sine_2():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=2)
    assert result == TEST_CASES[2][0]

def test_sine_3():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=3)
    assert result == TEST_CASES[3][0]

def test_sine_4():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=4)
    assert result == TEST_CASES[4][0]

def test_sine_5():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=5)
    assert result == TEST_CASES[5][0]

def test_sine_6():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=6)
    assert result == TEST_CASES[6][0]

def test_sine_7():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=7)
    assert result == TEST_CASES[7][0]

def test_sine_8():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=8)
    assert result == TEST_CASES[8][0]

def test_sine_9():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=9)
    assert result == TEST_CASES[9][0]

def test_sine_10():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=10)
    assert result == TEST_CASES[10][0]

def test_sine_11():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=11)
    assert result == TEST_CASES[11][0]

def test_sine_12():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=12)
    assert result == TEST_CASES[12][0]

def test_sine_13():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=13)
    assert result == TEST_CASES[13][0]

def test_sine_14():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=14)
    assert result == TEST_CASES[14][0]

def test_sine_15():
    result = Q1.calculateSine(degrees=DEGREES, accuracy=15)
    assert result == TEST_CASES[15][0]

def test_cos_1():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=1)
    assert result == TEST_CASES[1][1]

def test_cos_2():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=2)
    assert result == TEST_CASES[2][1]

def test_cos_3():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=3)
    assert result == TEST_CASES[3][1]

def test_cos_4():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=4)
    assert result == TEST_CASES[4][1]

def test_cos_5():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=5)
    assert result == TEST_CASES[5][1]

def test_cos_6():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=6)
    assert result == TEST_CASES[6][1]

def test_cos_7():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=7)
    assert result == TEST_CASES[7][1]

def test_cos_8():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=8)
    assert result == TEST_CASES[8][1]

def test_cos_9():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=9)
    assert result == TEST_CASES[9][1]

def test_cos_10():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=10)
    assert result == TEST_CASES[10][1]

def test_cos_11():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=11)
    assert result == TEST_CASES[11][1]

def test_cos_12():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=12)
    assert result == TEST_CASES[12][1]

def test_cos_13():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=13)
    assert result == TEST_CASES[13][1]

def test_cos_14():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=14)
    assert result == TEST_CASES[14][1]

def test_cos_15():
    result = Q1.calculateCos(degrees=DEGREES, accuracy=15)
    assert result == TEST_CASES[15][1]