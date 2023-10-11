import datasource

def main():
    cities=datasource.cities_info()
    for city in cities:
        print(city)

if __name__ =="__main__":
    main()