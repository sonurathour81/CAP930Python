'''employee={"EmpName":"Sonu Kumar","EmpAge":"22","EmpDepartment":"Computer Science",
          "EmpDesignation":"Web Developer","EmpJoinDate":"24/08/2018","EmpSalary":"30000"}
for k,v in employee.items():
    print(k,":",v)'''

fixed_info=('EmpId---> 0101','EmpName---> sonu Kumar',
            'EmpAge---> 22')
for i in fixed_info:
    print(i)




employee=dict([("EmpDepartment","Computer Science"),
               ("EmpDesignation","Web Developer"),
               ("EmpJoinDate","24/08/2018"),
               ("EmpSalary","30000")])
for k,v in employee.items():
    print(k,":",v)
