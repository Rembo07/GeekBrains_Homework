class Matrix:
    def __init__(self, input_data):
        self.input_data = input_data
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input_data])
    def __add__(self, other_input):
        self.other_input = other_input
        answer = ''
        if len(self.input_data) == len(self.other_input):
            for lin_1, lin_2 in zip(self.input_data, self.other_input):
                if len(lin_1) != len(lin_2):
                    return 'Problems with shape'
                sum_line = [a + b for a, b in zip(lin_1, lin_2)]
                answer = ''.join(map(str, sum_line)) + '\n'
        else:
            return 'Problems with shape'
        return answer

#mat_1 = Matrix([[1, 2], [3, 4], [5, 6]])
#mat_2 = Matrix([[1, 2], [3, 4], [5, 6]])
#print(mat_1.__add__([[1, 2], [3, 4], [5, 1]]))