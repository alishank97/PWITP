import xlsxwriter


class Person:
    protein_intake = 0.36  # grams
    water_intake1 = 0.5 # ounce
    water_intake2 = 1 # ounce



    def __init__(self, weight):
        self.weight = weight


    def calc_p(self):
        x = str(self.weight * self.protein_intake)
        global x
        print("You need to consume around " + x + " grams of protein daily")

    def calc_w(self):
        y = str(self.weight * self.water_intake1)
        z = str(format(self.weight * self.water_intake2, '.0f'))
        print("You need to drink between " + y + " to " + z + " ounces of water daily")
PI =
WI1 = y
WI2 = z
p_weight = input("How much do you weight? (in pounds): ")
while True:
    try:
        float(p_weight)
    except ValueError:
        print("This is a number. Please enter a numerical value")
        p_weight = input("How much do you weight? (in pounds): ")
        continue
    break

x1 = float(p_weight)




person = Person(x1)
person.calc_p()
person.calc_w()

workbook = xlsxwriter.Workbook('Protein_weight_intake.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Weight')
worksheet.write('B1', 'Protein Intake')
worksheet.write('C1', 'Minimum WI')
worksheet.write('D1', 'Maximum WI')



worksheet.write('A2', x1)
worksheet.write('B2', PI)
worksheet.write('C2', WI1)
worksheet.write('D2', WI2)




workbook.close()





