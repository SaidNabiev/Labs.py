import json
from abc import ABC, abstractmethod

class Heroes(ABC):

    def __init__(self, Time: int, Update: bool, Matches: int):
        
        self.Time = Time
        self.Update = Update
        self.Matches = Matches

    def __repr__(self) -> str:
        return f'<\'{self.__class__.__name__}\' Name: {self.name}, Time: {self.Time}, Update: {self.Update}, Matches: {self.Matches}>'

    @abstractmethod
    def AverageMatches(self):
        return f' Average time in the game {self.Name}: {self.Time / self.Matches}'

    @abstractmethod
    def CheckUpdate(self):
        if self.Update:
            return f'{self.Name}- Update required'
        else:
            return f'{self.Name}- Ready to launch'

class Spider(Heroes):
    def __init__(self, Time: int, Update: bool, Matches: int):
        self.name = "Broodmother"
        super().__init__(Time, Update, Matches)

    def AverageMatches(self):
        return super().AverageMatches()
    def CheckUpdate(self):
        return super().CheckUpdate()

class VSG(Heroes):
    def __init__(self, Time: int, Update: bool, Matches: int):
        self.name = "Visage"
        super().__init__(Time, Update, Matches)

    def AverageMatches(self):
        return super().AverageMatches()
    def CheckUpdate(self):
        return super().CheckUpdate()

class BMSTR(Heroes):
    def __init__(self, Time: int, Update: bool, Matches: int):
        self.name = "Beastmaster"
        super().__init__(Time, Update, Matches)

    def AverageMatches(self):
        return super().AverageMatches()
    def CheckUpdate(self):
        return super().CheckUpdate()

class Wolf(Heroes):
    def __init__(self, Time: int, Update: bool, Matches: int):
        self.name = "Lycan"
        super().__init__(Time, Update, Matches)

    def AverageMatches(self):
        return super().AverageMatches()
    def CheckUpdate(self):
        return super().CheckUpdate()


class Axen(Heroes):
    def __init__(self, Time: int, Update: bool, Matches: int):
        self.name = "Axe"
        super().__init__(Time, Update, Matches)
    def AverageMatches(self):
        return super().AverageMatches()
    def CheckUpdate(self):
        return super().CheckUpdate()

class DB(Heroes):
    def __init__(self, Time: int, Update: bool, Matches: int):
        self.name = "Dawnbreaker"
        super().__init__(Time, Update, Matches)

    def AverageMatches(self):
        return super().AverageMatches()
    def CheckUpdate(self):
        return super().CheckUpdate()


def output(file_name, company):
    with open(file_name, "w") as the_file:
        the_file.write(company.to_json())   

def imput(file_name):
    with open("the_file.json", "r") as read_file:
        data = json.load(read_file)
    return data

def write(data):
    jsonstr = json.dumps(ensure_ascii=False, obj=data, indent=4)
    open('output.json', 'w').write(jsonstr)


def read_from_json():
    return json.load(open('output.json', 'r'))


Broodmother = Spider(4000,True,2500)
Visage = VSG(100,False,200)
Lycan = Wolf(606,False,606)
Axe = Axen(100,True,150)
Beastmaster = BMSTR(900,True,808)
Dawnbreaker = DB(10000,False,3000)

objects = [Broodmother, Lycan, Visage, Axe, Beastmaster, Dawnbreaker, ]
data = {
        'heroes': [],
}
for obj in objects:
    data['heroes'].append(obj.__dict__)

write(data)
data.clear()
objects.clear()
data = read_from_json()

for obj in data['heroes']:
    if obj['name'] == "Broodmother":
        obj = Spider(obj['Time'], obj['Update'], obj['Matches'])
    elif obj['name'] == "Lycan":
        obj = Wolf(obj['Time'], obj['Update'], obj['Matches'])
    elif obj['name'] == "Visage":
        obj = VSG(obj['Time'], obj['Update'], obj['Matches'])
    elif obj['name'] == "Beastmaster":
        obj = BMSTR(obj['Time'], obj['Update'], obj['Matches'])
    elif obj['name'] == "Dawnbreaker":
        obj = DB(obj['Time'], obj['Update'], obj['Matches'])
    objects.append(obj)

with open(encoding='utf-8', file='Output.txt', mode='w') as file:
    for obj in objects:
        output = obj.__repr__() + "\n"
        file.write(output)