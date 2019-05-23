import pytest
import requests
import re

id=None

def test_create():
    emp_data = {"name":"હર્ષિલ","salary":"70000","age":"29"} 

    r = requests.post("http://dummy.restapiexample.com/api/v1/create", json=emp_data)
    assert r.status_code == 200

    rdata = r.json()
    global id
    id = rdata['id']
    p = re.compile("^[0-9]+$")
    assert p.search(id)

    r = requests.get("http://dummy.restapiexample.com/api/v1/employee/{}".format(id))
    assert r.status_code == 200
    expected_data = {'id': id, 'employee_name': 'હર્ષિલ', 'employee_salary': '70000', 'employee_age': '29', 'profile_image': ''}
    rdata = r.json()

    assert rdata == expected_data

def test_update():
    emp_data = {"name":"qwerty","salary":"15000","age":"25"} 
    r = requests.put("http://dummy.restapiexample.com/api/v1/update/{}".format(id), json=emp_data)
    assert r.status_code == 200

    r = requests.get("http://dummy.restapiexample.com/api/v1/employee/{}".format(id))
    assert r.status_code == 200

    expected_data = {'id': id, 'employee_name': 'qwerty', 'employee_salary': '15000', 'employee_age': '25', 'profile_image': ''}
    rdata = r.json()

    assert rdata == expected_data


def test_delete():
    r = requests.delete("http://dummy.restapiexample.com/api/v1/delete/{}".format(id))
    assert r.status_code == 200

    r = requests.get("http://dummy.restapiexample.com/api/v1/employee/{}".format(id))
    assert r.status_code == 200

    assert r.json() == False
