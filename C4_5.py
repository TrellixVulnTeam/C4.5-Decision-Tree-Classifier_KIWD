import math
from Node import Node

class C4_5:
    def __init__(self, data):
        self.data = data
        self.classes = ["High Income", "Middle Income", "Low Income"]
        self.tree = None
        self.attributes = list(self.data.keys())  # get all column names

    # Assigned to Kaleigh to filter the data.
    # 1. you may access job type by self.data["Occupation"], and please return filtered list of data
    # classified into one of the classes defined above.
    def filterData(self):
        print("Kaleigh's job")
        self.preprocessData()

    # This should work
    def generateC4_5Tree(self):
        self.tree = self.recursiveBuildC4_5Tree(self.data, self.attributes)

    def recursiveBuildC4_5Tree(self, curData, curAttributes):
        # allSame = self.allSameClass(curData)

        if curData is None or len(curData) == 0:
            # Fail
            return Node(True, "Fail", None)


    def preprocessData(self):
        columns = self.attributes
        numOfEntries = len(self.data[columns[0]]) # get how much rows of data there is
        index = 0

        while index < numOfEntries:
            age = self.data["Age"][index] # grab row index of Age column
            if(age == "" or int(age) < 15): # if no age or less than 15, discard
                for column in columns: # delete that row from each column
                    del self.data[column][index]
                index-=1
                numOfEntries-=1 # we have 1 less row now
            index+=1

    # This should work
    def printTree(self):
        self.printNode(self.tree)

    # This should work
    def printNode(self, node, indent=""):
        if not node.isLeaf:
            if node.gainRatio is None:
                # discrete
                for index, child in enumerate(node.children):
                    if child.isLeaf:
                        print(indent + node.attribute + " = " + self.attributes[index] + " : " + child.attribute)
                    else:
                        print(indent + node.attribute + " = " + self.attributes[index] + " : ")
                        self.printNode(child, indent + "	")
            else:
                # numerical
                leftChild = node.children[0]
                rightChild = node.children[1]
                if leftChild.isLeaf:
                    print(indent + node.attribute + " <= " + str(node.gainRatio) + " : " + leftChild.attribute)
                else:
                    print(indent + node.attribute + " <= " + str(node.gainRatio) + " : ")
                    self.printNode(leftChild, indent + "	")

                if rightChild.isLeaf:
                    print(indent + node.attribute + " > " + str(node.gainRatio) + " : " + rightChild.attribute)
                else:
                    print(indent + node.attribute + " > " + str(node.gainRatio) + " : ")
                    self.printNode(rightChild, indent + "	")