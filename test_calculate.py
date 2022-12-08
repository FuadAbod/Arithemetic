
from calculate import convertTxtToList,SumAndMutiplicationOfNumbers,convertTxtToDict, stringConstraints

def test_convertTxtToList():
    conversion = convertTxtToList().convert('testfiles/tester1.txt')
    assert conversion == [1721,979,366,299,675,1456]

def test_SumAndMutiplicationOfNumbers():
    obj_call = SumAndMutiplicationOfNumbers()
    permuation_with_two_numbers= obj_call.view_data('testfiles/tester1.txt',2)
    permuation_with_three_numbers=obj_call.view_data('testfiles/tester1.txt',3)
    
    assert permuation_with_two_numbers[0][0] + permuation_with_two_numbers[0][1] == 2020
    assert permuation_with_two_numbers[0][0] * permuation_with_two_numbers[0][1] == 514579
    assert permuation_with_three_numbers[0][0] + permuation_with_three_numbers[0][1]+permuation_with_three_numbers[0][2] == 2020
    assert permuation_with_three_numbers[0][0] * permuation_with_three_numbers[0][1] *permuation_with_three_numbers[0][2] == 241861950

def test_convertTxtToDict():
    obj_call = convertTxtToDict().convert('testfiles/tester2.txt')
    
    assert obj_call == {'a': {'abcde': ['1', '3']}, 'b': {'cdefg': ['1', '3']}, 'c': {'ccccccccc': ['2', '9']}}

def test_stringConstraints():
    obj_call = stringConstraints()
    constraints = obj_call.view_data('testfiles/tester2.txt')
    sum_of_string_constraints = constraints[0]
    sum_constraints_position = constraints[1]

    assert sum_of_string_constraints == 2
    assert sum_constraints_position == 1

