import pandas


def count_fur_colors():
    data = pandas.read_csv(
        "/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/squirel/Squirrel_Data.csv")
    fur_colors = data["Primary Fur Color"].tolist()
    color_dict = {}
    for color in fur_colors:
        color_dict[color] = 0
    colors = []
    counts = []
    for color in fur_colors:
        color_dict[color] += 1
    for color in color_dict:
        colors.append(color)
        counts.append(color_dict[color])

    new_dict = {"Fur color": colors,
                "Counts": counts}
    data_frame = pandas.DataFrame(new_dict)
    data_frame = data_frame.dropna()  # removes NaN rows
    print(data_frame)
    data_frame.to_csv("Fur color's counts.csv")
def count_fur_colors_v2():
    data = pandas.read_csv("/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/squirel/Squirrel_Data.csv")
    grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
    print(grey_squirrels_count)
    print(red_squirrels_count)
    print(black_squirrels_count)

    data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
    }

    df = pandas.DataFrame(data_dict)
    df.to_csv("squirrel_count.csv")




count_fur_colors()

