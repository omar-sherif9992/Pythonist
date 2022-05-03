import pandas

def dublicates():
    """Identify how many duplicate rows are in the following file. and remove dublicated rows """
    data=pandas.read_csv("worldcities.csv")
    cities=data["City"].tolist()
    countries=data["Country"].tolist()
    cities_dict={}
    countries_dict={}
    row=[]
    count_dublictaes=0
    for i in range(0,len(countries)):
        countries_dict[countries[i]]=0
        cities_dict[cities[i]] = 0
        if (countries[i],cities[i]) in row:
            count_dublictaes+=1

        else:
            row.append((countries[i],cities[i]))
    print(f"Number of Dublicates: {count_dublictaes}")

    countries=[]
    cities=[]
    for (country,city) in row:
        countries.append(country)
        cities.append(city)

    data={"City":cities,
          "Country":countries}
    df=pandas.DataFrame(data)
    df.to_csv("formated_file.csv")





dublicates()