import csv
import pandas


def read_content(filename):
    with open(
            f"{filename}") as file:  # it opens a file without reading it's contents plus the word with it auto matically cose the file after it's body is finished and have the ability only to read
        contents = file.read()  # it reads the content of the file
        return contents


def read_data(filename):
    file = open(f"{filename}", "r")
    content = file.readline()
    data = []
    while content != "":
        data.append(content.strip())
        content = file.readline()

    file.close()
    return data


def read_csv(filename):
    """this method reads each word in the csv seperated by a comma and put it in the same line inside a list """
    with open(f"{filename}") as file:
        data = csv.reader(file)
        temperature = []
        for row in data:
            if row[1] != "temp":
                temperature.append(int(row[1]))
            print(data)


def read_panda(filename):
    "this methode reads the csv file in tabular formuseing Panda library"
    data = pandas.read_csv(filename)  # panda library reading the csv file
    print(data)  # printing the Data Frame
    print(data["temp"])  # printing the series which means a (Column)
    data_dict = data.to_dict()  ## transform it into dictionary
    print(data_dict)
    temperature = data["temp"].tolist()  ## convert a Series into a listen
    print(f"temperature list using .tolist() ==> {temperature}")
    print(data["temp"].mean())  # series mean method
    print(data["temp"].max())  # series max method
    print(data[data["day"] == "Monday"])  # to find a specific row
    print(data[data["temp"] == data["temp"].max()])  # to find a specific row that contains the maximum temperature
    print(32 + 9 / 5 * (int(data[data[
                                     "day"] == "Monday"].temp)))  # find the monday row  and print the temperature attribute !Note : that the headingsof the columns are the attributes


def create_dataframe():
    data_dict = {"students": ["omar", "nour", "jana"],
                 "scores": [22, 9, 100]
                 }
    data=pandas.DataFrame(data_dict)#converts  a dicttionary into a pandas.DataFrame
    print(data)
    data.to_csv("new_data.csv")#it creates a new csv file with a student_score "new_data.csv" and the data of dataframe
    


 #read_panda("weather_data.csv")
create_dataframe()

