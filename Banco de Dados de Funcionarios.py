class Employee:
    def __int__(self, name, job):
        self.name = name
        self.job = job

    def tasks(self):
        print('Tasks are: ')

class Maneger(Employee):
    def __int__(self, name, job, staff):
        super().__int__(name, job)
        self.staff = staff

    def tasks(self):
        print('Oversees: ')
        print(staff)

class Associate(Employee):
    def tasks(self):
        print('Take orders from manager')
