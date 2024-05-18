import pyodbc
from colorama import init, Fore, Style
import getpass

# Initialize colorama
init(autoreset=True)

# Database connection parameters

try:
    DRIVER_NAME = "SQL SERVER"
    SERVER_NAME = "DESKTOP-OMN4JS0"
    DB = "CarShowRoom"
    # UID=""
    # PWD=""
    connection_string = f'DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};DATABASE={DB};Trust_Connection=yes'
    # Connect to the database
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
except pyodbc.Error as e:
    print("Error connecting to database:", e)
    
            
            
def authenticate(username, password):
    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False            

# Create a car entry
def create_car(brand, model, year, price):
    cursor.execute("INSERT INTO Cars (Brand, Model, Year, Price) VALUES (?, ?, ?, ?)", (brand, model, year, price))
    conn.commit()
    print(Fore.GREEN + "Car added successfully")

# Read car entries
def read_cars():
    cursor.execute("SELECT * FROM Cars")
    rows = cursor.fetchall()
    print(Fore.CYAN + "Current Cars in Showroom:")
    print(Fore.YELLOW + "{:<10} {:<15} {:<15} {:<10} {:<10}".format("CarID", "Brand", "Model", "Year", "Price"))
    print(Fore.YELLOW + "-"*60)
    for row in rows:
        print(Fore.WHITE + "{:<10} {:<15} {:<15} {:<10} {:<10}".format(row.CarID, row.Brand, row.Model, row.Year, row.Price))

# Update a car entry
def update_car(car_id, brand, model, year, price):
    cursor.execute("UPDATE Cars SET Brand = ?, Model = ?, Year = ?, Price = ? WHERE CarID = ?", (brand, model, year, price, car_id))
    conn.commit()
    print(Fore.GREEN + "Car updated successfully")

# Delete a car entry
def delete_car(car_id):
    cursor.execute("DELETE FROM Cars WHERE CarID = ?", (car_id,))
    conn.commit()
    print(Fore.RED + "Car deleted successfully")

# Search for cars by make
def search_car_by_brand(brand):
    cursor.execute("SELECT * FROM Cars WHERE Brand = ?", (brand,))
    rows = cursor.fetchall()
    if rows:
        print(Fore.CYAN + f"Cars matching '{brand}':")
        print(Fore.YELLOW + "{:<10} {:<15} {:<15} {:<10} {:<10}".format("CarID", "Brand", "Model", "Year", "Price"))
        print(Fore.YELLOW + "-"*60)
        for row in rows:
            print(Fore.WHITE + "{:<10} {:<15} {:<15} {:<10} {:<10}".format(row.CarID, row.Brand, row.Model, row.Year, row.Price))
    else:
        print(Fore.RED + f"No cars found for brand '{brand}'")
        
        
def search_car_by_model(model):
    cursor.execute("SELECT * FROM Cars WHERE Model = ?", (model,))
    rows = cursor.fetchall()
    if rows:
        print(Fore.CYAN + f"Cars matching '{model}':")
        print(Fore.YELLOW + "{:<10} {:<15} {:<15} {:<10} {:<10}".format("CarID", "Brand", "Model", "Year", "Price"))
        print(Fore.YELLOW + "-"*60)
        for row in rows:
            print(Fore.WHITE + "{:<10} {:<15} {:<15} {:<10} {:<10}".format(row.CarID, row.Brand, row.Model, row.Year, row.Price))
    else:
        print(Fore.RED + f"No cars found for model '{model}'")
        



def count_cars():
   cursor.execute("SELECT COUNT(*) FROM Cars")
   
   
   row_count = cursor.fetchone()[0]
   
   
   print(f'The Number of Cars is: {row_count}')




def get_int_input(prompt):
    while True:
        try:
            return int(input(Fore.CYAN + prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integer.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(Fore.CYAN + prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a float.")

def get_non_empty_string(prompt):
    while True:
        result = input(Fore.CYAN + prompt).strip()
        if result:
            return result
        else:
            print(Fore.RED + "Input cannot be empty. Please enter a valid string.")





# Main menu
def main():
    
    try:
        while True:
            print(Fore.BLUE + Style.BRIGHT + "\nCar Showroom Management System")
            print(Fore.BLUE + Style.BRIGHT + "================================")
            print(Fore.MAGENTA + "1. Add Car")
            print(Fore.MAGENTA + "2. View Cars")
            print(Fore.MAGENTA + "3. Update Car")
            print(Fore.MAGENTA + "4. Delete Car")
            print(Fore.MAGENTA + "5. Search Car by Brand")
            print(Fore.MAGENTA + "6. Search Car by Model")
            print(Fore.MAGENTA + "7. To View Number of Cars")
            print(Fore.MAGENTA + "8. Exit")
            print(Fore.BLUE + "================================")
            choice = input(Fore.CYAN + "Enter your choice: ")
          
            if choice == '1':
                brand = get_non_empty_string("Enter brand: ")
                model = get_non_empty_string("Enter model: ")
                year = get_int_input("Enter year: ")
                price = get_float_input("Enter price: ")
                create_car(brand, model, year, price)
          
            elif choice == '2':
                read_cars()
          
            elif choice == '3':
                car_id = get_int_input("Enter car ID to update: ")
                brand = get_non_empty_string("Enter new brand: ")
                model = get_non_empty_string("Enter new model: ")
                year = get_int_input("Enter new year: ")
                price = get_float_input("Enter new price: ")
                update_car(car_id, brand, model, year, price)
          
            elif choice == '4':
                car_id = int(input(Fore.CYAN + "Enter car ID to delete: "))
                delete_car(car_id)
          
            elif choice == '5':
                brand = get_non_empty_string(Fore.CYAN + "Enter the brand to search for: ")
                search_car_by_brand(brand)
              
            elif choice == '6':
                model = get_non_empty_string(Fore.CYAN + "Enter the Model to search for: ")
                search_car_by_model(model)    
          
          
            elif choice == '7':
                count_cars()
                
            elif choice == '8':
                print(Fore.BLUE + "Exiting the system...")
                break    
          
            
          
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
                
    except pyodbc.Error as e:
        print("Error:", e)            

# Run the main menu


    

def login():
    
        print(Fore.BLUE + Style.BRIGHT + "Car Showroom Management System Login")
        
        print(Fore.BLUE + "====================================")
        username = input(Fore.CYAN + "Username: ")
        password = getpass.getpass(Fore.CYAN + "Password: ")
        if authenticate(username, password):
            print(Fore.GREEN + "Login successful!")
            main()
            
        else:
           
            print(Fore.RED + "Invalid username or password. Please try again.")
            login()
            
                
                
        




login()

# Close the connection
conn.close()
