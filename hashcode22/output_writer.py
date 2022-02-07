class OutputWriter:
    def __init__(self):
        pass

    def write(self, solution, file_path: str):
        with open(file_path, "w") as file:
            file.write(str(solution.n_ingredients))
            for ingredient in solution.ingredients:
                file.write(f" {ingredient}")
        
        print("Done!")