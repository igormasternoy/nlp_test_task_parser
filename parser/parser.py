import sys

LPR = '('
RPR = ')'
SPACE = ''


class Node(object):
    def __init__(self, nodeName):
        self.nodeName = nodeName
        self.child = list()
        self.parent = None

    def add_child(self, child):
        self.child.append(child)
        return self

    def __str__(self):
        return self.nodeName

    def __repr__(self):
        return self.nodeName


def parseTree(tokens):
    stack = list()  # Stack
    temp = ''
    for char in tokens:
        if char == LPR:
            stack.append(LPR)
        elif char == RPR:
            if temp:
                stack.append(Node(temp))
            temp = ''
            found = False
            nodes = list()
            while not found:
                # format nodes
                element = stack.pop()
                if element == LPR:
                    node = nodes.pop()
                    for el in nodes:
                        node.add_child(el)
                    stack.append(node)
                    found = True
                else:
                    nodes.append(element)
        elif char == ' ':
            if temp:
                stack.append(Node(temp))
            temp = ''
        else:
            temp += char
            # print char
    return stack


def printTree(node, indentation, isLast):
    if indentation == 0:
        print node
        node.child.reverse()
        counter = 0
        for child in node.child:
            counter += 1
            if counter == len(node.child):
                printTree(child, indentation + 1,True)
            else:
                printTree(child, indentation + 1,False)
    elif indentation == 1:
        print ' ' + '+--' + ' ' + str(node)
        node.child.reverse()
        for child in node.child:
            printTree(child, indentation + 1,isLast)
    elif indentation > 1:
        node.child.reverse()
        if isLast :
            print ' ' + '  ' + ' ' * indentation  + '+--' + ' ' + str(node)
        else:
            print ' ' + '| ' + ' ' * indentation + '+--' + ' ' + str(node)
        for child in node.child:
            printTree(child, indentation + 4,isLast)


def main():
    tokens = sys.argv[1]
    stack = parseTree(tokens)
    node = stack.pop()
    printTree(node, 0, None)


if __name__ == '__main__':
    main()
