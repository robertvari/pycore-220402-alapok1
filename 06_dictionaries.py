phonebook = {
    "06205556677": "Robert",
    "06205556678": "Csaba",
    "06205556679": "Kriszta",
}

print(phonebook["06205556678"])

phonebook["06205556677"] = "Tamás"
print(phonebook)

del phonebook["06205556677"]
print(phonebook)