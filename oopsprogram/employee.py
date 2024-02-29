class Employee :
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchiveTarget(self):
            if (self.salesMadeThisWeek >= 5) :
                  print("target has been achived")
            else:
                  print("target has not been achived")

employeeOne = Employee()
print (employeeOne.name)
print (employeeOne.salesMadeThisWeek)
