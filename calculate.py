from itertools import permutations
import math
from collections import Counter
import typing 

class convertTxtToList:
    def convert(self, route:str):
        with open(route) as f:
            self.list_of_int = [int(i.strip()) for i in f.readlines()]
        f.close()
        return self.list_of_int

class SumAndMutiplicationOfNumbers:
    def view_data(self,route:str,permutation_of_numbers:int):
        self.list_of_int = convertTxtToList().convert(route)
        sum_solutions = [pair for pair in permutations(self.list_of_int, permutation_of_numbers) if sum(pair) == 2020]
        Multiple_sum = math.prod(sum_solutions[0])
        return sum_solutions[0],Multiple_sum

class convertTxtToDict:
    def convert(self, route):
        # Reformating to this structure {c:{str:[lower_limit_n,upper_limit_n]}}
        self.new_dict={}
        with open(route) as f:
            embed_dict = list([i.strip() for i in f.readlines()])
            for i in range(len(embed_dict)):
                list_of_alphabets = [ele for ele in list(embed_dict[i]) if ele.isalnum()]
                new_key=''.join(list_of_alphabets[3:len(list_of_alphabets)+1])
                self.new_dict.update({list_of_alphabets[2]:{new_key:list_of_alphabets[:2]}})
        f.close()
        return self.new_dict

class stringConstraints:
    def view_data(self, route):
        self.new_dict = convertTxtToDict().convert(route)
        sum_of_occurence = 0
        sum_of_constraint_position = 0
        for key in self.new_dict.keys():
            convert_dict_key_to_list =list(self.new_dict[key].keys())
            current_value = convert_dict_key_to_list[0].count(key)
            for inner_key,inner_value in self.new_dict[key].items():
                lower_limit=int(inner_value[0])
                upper_limit=int(inner_value[1])
                split_inner_key=[*inner_key]
                if current_value in range(lower_limit, upper_limit+1):
                    sum_of_occurence += 1
                if split_inner_key[lower_limit-1] == key and split_inner_key[upper_limit-1] == key:
                    pass
                elif split_inner_key[lower_limit-1] != key and split_inner_key[upper_limit-1] != key:
                    pass
                else:
                    sum_of_constraint_position +=1
        return sum_of_occurence,sum_of_constraint_position

    
# print(SumAndMutiplicationOfNumbers().view_data('simons-test/input/input1.txt',2))
# print(SumAndMutiplicationOfNumbers().view_data('simons-test/input/input1.txt',3))
# print(stringConstraints().view_data('simons-test/input/input2.txt'))
