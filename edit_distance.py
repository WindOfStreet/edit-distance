

class EditDistance:
    def __init__(self, itcost=1, rmcost=1, rpcost=1):
        self.itcost = itcost    # insert cost
        self.rmcost = rmcost    # remove cost
        self.rpcost = rpcost    # replace cost
        self.distance = 0       # edit distance
        self.solution = {}      # best operations for specific str1 and str2. e.g self.solution = {('ti','to'):('replace',o)}
        self.all_steps = []     # procedures to convert str1 to str2

    def calc_distance(self, str1, str2):
        """把str1转换为str2的各个步骤"""
        if not isinstance(str1, str) and isinstance(str2, str):
            raise TypeError("input must be str type")

        if len(str1)==0:
            return self.itcost*len(str2)
        if len(str2)==0:
            return self.rmcost*len(str1)
        if str1 == str2:
            return 0

        tail1 = str1[-1]
        tail2 = str2[-1]

        # 这里犯下一个错误，为了后面排序方便，引入了距离作为dict的key，忘了同一个距离可能对应多个操作！debug好久...
        # candidate = {distance:operation}
        candidate = [(self.calc_distance(str1[:-1], str2) + self.rmcost, ('remove', tail1)),
                     (self.calc_distance(str1, str2[:-1]) + self.itcost, ('insert', tail2))]
        if tail1 == tail2:
            candidate.append((self.calc_distance(str1[:-1], str2[:-1]), ('', '')))
        else:
            score = self.calc_distance(str1[:-1], str2[:-1])+self.rpcost
            candidate.append((score, ('replace', tail2)))

        self.distance, operate = min(candidate, key=lambda x: x[0])
        self.solution[(str1, str2)] = operate
        return self.distance

    def parse_results(self, str1, str2):
        self.solution.clear()
        self.calc_distance(str1, str2)
        self.all_steps.clear()
        curt_step = [str1, str2]
        tmp = (str1, str2)
        already = '' # 字符串末尾已经计算完的相同字符
        while tmp in self.solution:
            if self.solution[tmp][0] == 'insert':
                curt_step[0] += self.solution[tmp][1]
            elif self.solution[tmp][0] == 'remove':
                curt_step[0] = tmp[0][:-1]
            # 'replace' 和 ''操作相同
            else:
                curt_step[0] = tmp[0][:-1]
                # curt_step[0] += self.solution[tmp][1]
                curt_step[1] = tmp[1][:-1]
                already = tmp[1][-1:] + already
            if self.solution[tmp][0] != '':
                self.all_steps.append([self.solution[tmp], curt_step[0] + already])
            tmp = (curt_step[0], curt_step[1])

        return self.all_steps


if __name__ == '__main__':
    Calc = EditDistance(1, 1, 5)
    str1 = 'ting'
    str2 = 'tong'
    dist = Calc.calc_distance(str1, str2)
    # for key,val in Calc.solution.items():
    #     print(key,val)
    Calc.parse_results(str1, str2)
    print('{}和{}的编辑距离为{}。'.format(str1, str2, Calc.distance))
    # 打印操作步骤
    for item in Calc.all_steps:
       print(item)
