def add_employee(name, salary, age):
    if salary < 0:
        raise TypeError("Salary is not valid")
    if age < 0 or age > 80:
        raise ValueError("age is not valid")

    D={}
    D['name'] = name
    D['salary'] = salary
    D['age'] = age

    return D
