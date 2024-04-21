from typing import List

from individual import Individual


class Splitter:
    def __init__(self, individuals: List[Individual] = None, weights=None) -> None:
        self.__contributions = {}
        self.__weights = {}

        for i, ind in enumerate(individuals):
            self.__contributions[ind] = ind.get_contribution()
            self.__weights[ind] = 1 / len(individuals) if not weights else weights[i]

    def calculate_owning(self):
        res = {}
        for i in self.__contributions:
            res.setdefault(i, {})
            for ii in self.__contributions:
                res[i].setdefault(ii, 0)
                t = self.__contributions[ii] * self.__weights[i]
                res[i][ii] += t
                if ii in res:
                    if res[i][ii] > res[ii][i]:
                        res[i][ii] -= res[ii][i]
                        res[ii][i] = 0
                    else:
                        res[ii][i] -= res[i][ii]
                        res[i][ii] = 0

        return res
