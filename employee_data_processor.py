import csv
import matplotlib.pyplot as plt

class Employee:
    """models an Employee record."""
    def __init__(self, first_name, last_name, email, years):
        self.first_name=first_name
        self.last_name=last_name
        self.email = email
        self.years = years

    def __lt__(self, other):
        if self.last_name < other.last_name:
            return True
        elif self.last_name > other.last_name:
            return False
        elif self.first_name < other.first_name:
            return True
        elif self.first_name > other.first_name:
            return False
        else:
            return self.years > other.years

        
    def __eq__(self, other):
        if isinstance(other, Employee):
            return (self.first_name == other.first_name 
                    and self.last_name == other.last_name
                    and self.email == other.email
                    and self.years == other.years)
        return False


    def __str__(self):
        info_str = f'{self.first_name} {self.last_name} {"email:"} {self.email}' \
                    f' {"years:"} {self.years}' 
        return(info_str)  

class EmployeeDataProcessor:

    def __init__(self, data_list=None):
        self.data_list = []

    def get_data_list_from_csvfile(self, file_name):
        """Opens the csv file passed in and 
            creates an Employee object for each row of data
            in the file."""

        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    first_name, last_name, email, years = row
                    employee = Employee(first_name, last_name, email, int(years))
                    self.data_list.append(employee)    
                line_count += 1
        return self.data_list


    def initialize(self, file_name):
        self.data_list = self.get_data_list_from_csvfile(file_name)

    def get_data_size(self):
        return len(self.data_list)

    def get_employee_record(self, first_name, last_name, years):
        """Returns the first Employee object in the data_list that
           matches first_name, last_name, and years."""
        
        for employee in self.data_list:
            if (
                employee.first_name == first_name 
                and employee.last_name == last_name 
                and employee.years == years
                ):
                return employee
        return None


    def get_employee_list(self, start, end, sorted=False):
        """ Returns a list of employee object from data_list that fall
            within a specific range as specified by start and end index parameters."""
        
        if start < 0:
            raise Exception ("Do not meet constraints")
        if start >= end:
            raise Exception ("Do not meet constraints")
        if end > len(self.data_list):
            raise Exception ("Do not meet constraints")
        if start == end:
            raise Exception ("Do not meet constraints")
        
        if 0 <= start < end <= len(self.data_list):
            if sorted:
                emp_list = self.data_list[start:end]
                emp_list.sort()
            else:
                emp_list = self.data_list [start:end]
            return emp_list
        return []
    

    def get_years_list(self):
        """Returns a list that contains only the years from 
            all records on the data_list."""

        yr_list =[]
        for employee in self.data_list:
            yr_list.append (employee.years)
        return yr_list



    def plot_emp_years(self):
        """Creates and displays a histogram plot of all of the years
            that employees in data_list have worked."""
        
        data = self.get_years_list()
        # specify bin start and end points
        bin_ranges = [0,1,2,3,4,5,6,7,8,9,10]
        # creates a histogram with 4 bins
        plt.hist(data, bins=bin_ranges, edgecolor='black')
        plt.title("Years of Employment")
        plt.xlabel("Years")
        plt.ylabel("Frequency")
        plt.show()   

if __name__=="__main__":
    file_name = "C:\\Users\\angel\\Downloads\\employee_data.csv"

    emp_proc = EmployeeDataProcessor()
    emp_proc.initialize(file_name)
    emp_proc.plot_emp_years()