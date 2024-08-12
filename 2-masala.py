import os
os.system("cls")

class Car:
    def __init__(self, id: int, firs_name:str, last_name:str, gender:str, brand: str, year:int, color:str,country:str):
        self.id = id
        self.firs_name = firs_name
        self.last_name = last_name
        self.gender = gender
        self.brand = brand
        self.year = year
        self.color = color
        self.country = country
    
    def info(self):
        print(f"""
Id:                 {self.id}
Ism:                {self.firs_name}
Familiya:           {self.last_name}
Jins:               {self.gender}
Brend:              {self.brand}
Yil:                {self.year}
Rang:               {self.color}
Mamlakat:           {self.country}
              """)
    
    def Jins(cars):
        erkak = 0
        ayol = 0
        for car in cars:
            if car.gender == "erkak":
                erkak += 1
            else:
                ayol += 1
        sum = len(cars)
        erkak_foizi = (erkak*100) / sum 
        Ayollar_foizi = (ayol*100) / sum 
        return erkak_foizi, Ayollar_foizi
    
    def Year(cars):
        for car in cars:
            if car.year <= 2005:
                print(f"""
Kimdan:            Auto Test Corp
Kimga:             {car.firs_name} {car.last_name}
Joriy davlat:      {car.country}

        ************
Hurmatli {car.firs_name} {car.last_name}! {car.brand} tomonidan {car.year}da ishlab chiqarilgan {car.color} rangli avtoulovingiz Texnik Holatini tekshirtirsh 
maqsadida mahalliy Auto Test Corp. ofisiga murojaat qilishingizni so'raymiz!

""")
        
man1= Car(25863, "Karim", "Odilov", "erkak", "gentra", 2019, "qora", "O'zbekiston")
man2= Car(25462, "Odina", "Salimova", "ayol", "spark", 2015, "oq", "O'zbekiston")
man3 = Car(45781, "Dilbar", "Karimova", "ayol", "nexia", 2018, "ko'k", "O'zbekiston")
man4 = Car(32546, "Madina", "Ismoilova", "ayol", "malibu", 2020, "qizil", "O'zbekiston")
man5= Car(28180, "Sarvar", "Hasanov", "erkak", "monza", 2019, "qora", "Xitoy")
man6= Car(25863, "Jamshid", "aliyev", "erkak", "Matiz", 2004, "oq", "O'zbekiston")
man7 = Car(38912, "Nigora", "Shodmonova", "ayol", "cobalt", 2021, "kulrang", "O'zbekiston")
man8 = Car(25864, "Aziz", "Rahimov", "erkak", "Cobalt", 2018, "qora", "O'zbekiston")
man9 = Car(25865, "Gulnoza", "Karimova", "ayol", "Lacetti", 2017, "oq", "O'zbekiston")
man10 = Car(25866, "Ulug'bek", "Xolmatov", "erkak", "Malibu", 2021, "ko'k", "O'zbekiston")
print("****************")


man1.info()
man2.info()
man3.info()
man4.info()
man5.info()
man6.info()
man7.info()
man8.info()
man9.info()
man10.info()

cars = [man1, man2, man3, man4,man5,man6,man7,man8,man9,man10]

erkak_foizi, Ayollar_foizi = Car.Jins(cars)
print(f"Ayol: {erkak_foizi:.0f}% da, Erkak: {Ayollar_foizi:.0f}% da. Erkaklar soni ham ayollar soni ham bir biriga teng")

Car.Year(cars)