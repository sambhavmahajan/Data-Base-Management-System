import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

column_names = []
Data = []
IndexT = []
commands_and_syntax = [
    "clear",
    "command0;command1;command2;........"
    "create:<column_name1>:<column_name2>:...",
    "insert:<row_name>:<value1>:<value2>:...",
    "delete_row:<row_name>",
    "save:<filename>",
    "open:<filename>",
    "show",
    "sum:<column_name>",
    "avg:<column_name>",
    "shape",
    "plot:title:xlabel:ylabel:xcolumn:columntoplot",
    "modify:<row_name>:<column_name>:<new_value>",
    "quit",
    "help"
]


def main():
    global IndexT, commands_and_syntax
    print("Type help to get commands")
    while True:
        comm = input("Write Command: ")
        if comm == "quit":
            print("Program Exited successfully")
            break
        if comm == "help":
            for t in commands_and_syntax:
                print(t)
            continue
        arr = comm.split(';')
        for x in arr:
            if x == '':
                continue
            tkns = tokens(x)
            command = removespace(tkns[0])
            tkns.pop(0)
            for i in range(0, len(tkns)):
                tkns[i].strip()
            if command == "clear":
                choice = input("Are you sure you want to clear database?(y/n): ")
                if choice == 'y':
                    column_names.clear()
                    Data.clear()
                    IndexT.clear()
                    print("Database Cleared Successfully")
                elif choice == 'n':
                    print("Operation canceled")
                else:
                    print("Invalid Choice")
            elif command == "create":
                CreateTable(tkns)
                print("Created table")
            elif command == "insert":
                if tkns[0] in IndexT:
                    print("Error:", tkns[0], "Index already exists")
                else:
                    IndexT += tkns[0]
                    tkns.pop(0)
                    Insert(tkns)
            elif command == "delete_row":
                for s in tkns:
                    DeleteRow(s)
            elif command == "save":
                SaveToFile(tkns[0])
            elif command == "open":
                OpenFile(tkns[0])
                Show()
            elif command == 'show':
                Show()
            elif command == 'sum':
                print("Sum:", Sum(tkns[0]))
            elif command == 'avg':
                print("Avg:", Avg(tkns[0]))
            elif command == 'shape':
                print(np.array(Data).shape)
            elif command == "modify":
                modify(tkns[0], tkns[1], tkns[2])
            elif command == "plot":
                plt.title(tkns[0])
                plt.xlabel(tkns[1])
                plt.ylabel(tkns[2])
                toplot = []
                xcolumn = []
                i = column_names.index(tkns[3])
                for j in range(len(Data)):
                    xcolumn.append(Data[j][i])
                i = column_names.index(tkns[4])
                for j in range(len(Data)):
                    toplot.append(Data[j][i])
                plt.plot(xcolumn, toplot)
                plt.show()
            else:
                print("Error: Command \'" + command + '\'' + " Does not exist")

    return 0


def tokens(li):
    return removespace(li).split(':')


def removespace(s):
    return s.replace(" ", "")


def CreateTable(li):
    global column_names, Data, IndexT
    print("Confirm table override (y for yes, any key for no):")
    t = input()
    if t == 'y':
        column_names = li
        Data = []
        IndexT = []

    else:
        print("Table creation canceled")


def Insert(li):
    if len(column_names) != len(li):
        print("Number of inserted values must match the number of columns in a row")
        return -1
    Data.append(li)
    return 0


def GetIndex(arr, Indexname):
    i = 0
    for ele in arr:
        if str(ele) == str(Indexname):
            return i
        i += 1
    return -1


def DeleteRow(Row_Name):
    global IndexT, Data
    i = GetIndex(IndexT, Row_Name)
    if i == -1:
        print("Error: Row with index \'" + Row_Name + "\' does not exist")
        return
    IndexT.pop(i)
    Data.pop(i)
    print("Row " + '\'' + Row_Name, "deleted successfully")
    return


def Generate_DF():
    global Data, IndexT
    df = pd.DataFrame(Data, columns=column_names, index=IndexT)
    return df


def SaveToFile(filename):
    global column_names, IndexT
    df = Generate_DF()
    df.to_csv(filename)
    print("Saved file to " + filename + " successfully")


def OpenFile(filename):
    global Data, IndexT, column_names
    df = pd.read_csv(filename, header=0, index_col=0)
    column_names = df.columns.tolist()
    IndexT = df.index.tolist()
    Data = []
    t = df.values.tolist()
    for x in t:
        Data.append(x)


def Show():
    global Data, column_names, IndexT
    df = Generate_DF()
    print(df)


def modify(i, c, newVal):
    global IndexT, column_names, Data
    i0 = GetIndex(IndexT, i)
    c0 = GetIndex(column_names, c)
    Data[i0][c0] = newVal
    return 0


def Sum(columnName):
    r = 0
    columnindex = column_names.index(columnName)
    for x in Data:
        r += int(x[columnindex])
    return r


def Avg(columnName):
    return Sum(columnName) / len(IndexT)


if __name__ == '__main__':
    main()
