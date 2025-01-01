import Employee

def test_emplyess():
    
    dhruvi = Employee.Employee("Dhruvi", "Arulkar", 200000)
    print(dhruvi.long_name())
    dhruvi.custom_raise(10000)

    deepak = Employee.Employee("Deepak", "Katote", 200000)
    print(deepak.long_name())
    deepak.give_raise()
    assert 'Dhruvi Arulkar'
    assert 'The annual salary of Dhruvi Arulkar is 210000'
    assert 'Deepak Katote'
    assert 'The annual salary of Deepak Katote is 205000'