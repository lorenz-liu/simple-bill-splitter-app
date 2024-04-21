from individual import Individual
from splitter import Splitter


class CLI:
    def __init__(self) -> None:
        self.__individuals = []
        self.__terminate = False

    @staticmethod
    def __add_contribution(individual: Individual, amount: float):
        individual.add_contribution(amount=amount)

    def display(self):
        while not self.__terminate:
            print("============ SIMPLE BILL SPLITTER ============")
            print("    1. View contributions.                    ")
            print("    2. Add contribution/individual.           ")
            print("    3. Calculate.                             ")
            print("    4. Quit.                                  ")
            print("==============================================")
            opt = int(input("...Option: "))
            if opt == 1:
                print("============ CURRENT INDIVIDUALS =============")
                if len(self.__individuals) == 0:
                    print("    EMPTY!")
                for i, v in enumerate(self.__individuals):
                    print(f"    {i + 1}. {v.get_name()}  -  {v.get_contribution()}")
            elif opt == 2:
                print("============ CURRENT INDIVIDUALS =============")
                if len(self.__individuals) == 0:
                    print("    EMPTY!")
                for i, v in enumerate(self.__individuals):
                    print(f"    {i + 1}. {v.get_name()}  -  {v.get_contribution()}")
                print("==============================================")
                print("    Input the individual's number. ")
                print("    or press 0 to create a new individual...")
                print("==============================================")
                sub_opt = int(input("...Option: "))
                if sub_opt == 0:
                    print("=========== CREATE NEW INDIVIDUAL =============")
                    name = input("...Name: ")
                    email = input("...Email: ")
                    telephone = input("...Telephone: ")
                    contribution = float(input("...Contribution: "))
                    self.__individuals.append(
                        Individual(
                            name=name,
                            email=email,
                            telephone=telephone,
                            contribution=contribution,
                        )
                    )
                elif len(self.__individuals) >= sub_opt > 0:
                    contribution = float(input("...Adding contribution: "))
                    self.__individuals[sub_opt - 1].add_contribution(contribution)
                else:
                    print("========== !!!! INVALID OPTION !!!! ==========")
            elif opt == 3:
                print("=============== APPLY WEIGHTS? ===============")
                print("    1. No (equally split). ")
                print("    2. Yes.")
                sub_opt = int(input("...Option: "))

                weights = []
                if sub_opt == 1:
                    pass
                elif sub_opt == 2:
                    sum_weights = 0
                    for ind in self.__individuals:
                        t = float(input(f"    ...Weight for {ind.get_name()}: "))
                        weights.append(t)
                        sum_weights += t
                    if abs(sum_weights - 1.0) > 0.0001:
                        print("======== !!!! WEIGHTS MUST SUM 1 !!!! ========")
                        continue
                else:
                    print("========== !!!! INVALID OPTION !!!! ==========")
                    continue

                splitter = Splitter(individuals=self.__individuals, weights=weights)
                res = splitter.calculate_owning()
                for i in res:
                    print(i.get_name(), "owns: ")
                    for ii in res[i]:
                        print(f"     {ii.get_name()}: {res[i][ii]}")
                self.__terminate = True
            elif opt == 4:
                self.__terminate = True
            else:
                print("========== !!!! INVALID OPTION !!!! ==========")

            print()

        print("============= made by Lorenz :) ==============")
