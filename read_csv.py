import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader= csv.reader (csvfile, delimiter= ",") #delimiter (separador de datos en el archivo csv)
        header=next(reader)
        data=[]

        for row in reader:
            iterable=zip(header, row) #unir el header con el row
            country_dict={key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == "__main__":
    data=read_csv("./app/data.csv")  #los datos estan solo en forma de lista
    print (data[0])

