# Dataset Management and Basic Analysis System

class DataSet:
    def __init__(self, data_file, category_file):
        self.data_file = data_file
        self.category_file = category_file
        self.data = []
        self.categories = set()
        self.total = 0
        self.average = 0
        self.minimum = None
        self.maximum = None

    # 1 & 2. Variables, File Handling & Error Handling
    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        try:
                            self.data.append(float(line))
                        except ValueError:
                            print("Invalid (non-numeric) value found and skipped.")

            if not self.data:
                raise ValueError("File is empty or contains no valid numeric data.")

        except FileNotFoundError:
            print("Error: Data file not found.")
            exit()
        except ValueError as e:
            print(e)
            exit()

        # Load categorical data using set
        try:
            with open(self.category_file, 'r') as file:
                for line in file:
                    self.categories.add(line.strip())
        except FileNotFoundError:
            print("Error: Category file not found.")
            exit()

    # 3 & 4. Functions, Operators & Loops
    def calculate_total(self):
        total = 0
        for value in self.data:
            total += value
        return total

    def calculate_average(self):
        return self.total / len(self.data)

    def calculate_minimum(self):
        minimum = self.data[0]
        for value in self.data:
            if value < minimum:
                minimum = value
        return minimum

    def calculate_maximum(self):
        maximum = self.data[0]
        for value in self.data:
            if value > maximum:
                maximum = value
        return maximum

    # 7. OOP Method
    def calculate_statistics(self):
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.minimum = self.calculate_minimum()
        self.maximum = self.calculate_maximum()

    # 5 & 6. Conditional Statements & Sets
    def display_results(self):
        print("Total:", self.total)
        print("Average:", self.average)
        print("Minimum:", self.minimum)
        print("Maximum:", self.maximum)

        if self.average >= 70:
            print("Performance: High Performance")
        else:
            print("Performance: Needs Improvement")

        print("Unique Categories:", self.categories)
        print("Number of Unique Categories:", len(self.categories))

    # 8. Saving Results to File
    def save_report(self):
        with open("report.txt", "w") as report:
            report.write("DATASET ANALYSIS REPORT\n")
            report.write("------------------------\n")
            report.write(f"Total: {self.total}\n")
            report.write(f"Average: {self.average}\n")
            report.write(f"Minimum: {self.minimum}\n")
            report.write(f"Maximum: {self.maximum}\n")
            report.write(f"Unique Categories Count: {len(self.categories)}\n")

            if self.average >= 70:
                report.write("Performance: High Performance\n")
            else:
                report.write("Performance: Needs Improvement\n")


# Main Program Execution
dataset = DataSet("data.txt", "categories.txt")
dataset.load_data()
dataset.calculate_statistics()
dataset.display_results()
dataset.save_report()
