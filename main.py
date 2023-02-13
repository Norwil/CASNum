from chemical import Chemical
from database import Database
from data import chemicals_data


def main():
    db = Database()
    
    while True:
        print("1. Insert Chemical")
        print("2. Fetch Chemical")
        print("3. Remove Chemical")
        print("4. Update Chemical")
        print("5. Show All Chemicals")
        print("6. Insert Default Data")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        counter = 0

        if choice == 1:
            name = input("Enter Chemical Name: ")
            cas_number = input("Enter Chemical CAS Number: ")
            banned = int(input("Enter 0 if Chemical is not banned, 1 if Chemical is banned: "))
            classification = input("Enter Chemical Classification: ")
            melting_point = float(input("Enter Chemical Melting Point: "))
            boiling_point = float(input("Enter Chemical Boiling Point: "))
            flashpoint = float(input("Enter Chemical Flash Point: "))
            storage_temp = float(input("Enter Chemical Storage Temperature: "))
            chemical = Chemical(name, cas_number, banned, classification, melting_point, boiling_point, flashpoint, storage_temp)
            db.insert(chemical)

        elif choice == 2:
            id = int(input("Enter Chemical ID to fetch: "))
            chemical = db.fetch(id)
            if chemical:
                print("Chemical: ", chemical)
            else:
                print("Chemical not found")

        elif choice == 3:
            id = int(input("Enter Chemical ID to remove: "))
            db.remove(id)
            print("Chemical removed successfully")

        elif choice == 4:
            id = int(input("Enter Chemical ID to update: "))
            chemical = db.fetch(id)
            if chemical:
                name = input("Enter Chemical Name: ")
                cas_number = input("Enter Chemical CAS Number: ")
                banned = int(input("Enter 0 if Chemical is not banned, 1 if Chemical is banned: "))
                classification = input("Enter Chemical Classification: ")
                melting_point = float(input("Enter Chemical Melting Point: "))
                boiling_point = float(input("Enter Chemical Boiling Point: "))
                flashpoint = float(input("Enter Chemical Flash Point: "))
                storage_temp = float(input("Enter Chemical Storage Temperature: "))
                chemical = Chemical(name, cas_number, banned, classification, melting_point, boiling_point, flashpoint, storage_temp)
                db.update(id, chemical)
                print("Chemical updated successfully")
            else:
                print("Chemical not found")

        elif choice == 5:
            db.show()

        elif choice == 6:
            counter += 1
            if counter < 2:
                db.add_data(chemicals_data)
            else:
                print("You already inserted the default data!")
            
        elif choice == 7:
            db.close()
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
