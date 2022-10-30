
import matplotlib.pyplot as plt

class drinks:

    def __init__(self, water, tea, coffee, juice):
        self.water = water
        self.tea = tea
        self.coffee = coffee
        self.juice = juice

    def setWater(self, water):
        self.water = water
    def getWater(self):
        return self.water

    def setTea(self, tea):
        self.tea = tea
    def getTea(self):
        return self.tea
    
    def setCoffee(self, coffee):
        self.coffee = coffee
    def getCoffee(self):
        return self.coffee

    def setJuice(self, juice):
        self.juice = juice
    def getJuice(self):
        return self.juice

    def updateGraph(self, water, tea, coffee, juice):
        self.water += water
        self.tea += tea
        self.coffee += coffee
        self.juice += juice

    def displayGraph(self):
        total = self.water + self.tea + self.coffee + self.juice
        percentWater = self.water / total * 100
        percentTea = self.water / total * 100
        percentCoffee = self.water / total * 100
        percentJuice = self.water / total * 100

        labels = 'water', 'tea', 'coffee', 'juice'
        sizes = [percentWater, percentTea, percentCoffee, percentJuice]
        explode = (0.1, 0, 0, 0)

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title("Hydration")
        plt.show()


myGraph = drinks(1, 1, 1, 1)
myGraph.displayGraph()