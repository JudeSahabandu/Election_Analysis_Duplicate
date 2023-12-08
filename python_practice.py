counties = ["Arapahoe", "Denver", "Jefferson"]

if "El Paso" in counties:
    print("El Paso in counties list")
else:
    print("El Paso not in counties list")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])