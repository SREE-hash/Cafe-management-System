import pandas as pd 
import os  # For checking if file exists  

# Initialize an empty DataFrame to hold menu items 
menu_df = pd.DataFrame(columns=["Item ID", "Name", "Category", "Price", "Availability"]) 

# Load existing menu items from CSV if available   
def load_menu():   
    global menu_df   
    if os.path.exists("menu.csv"):  # Check if the file exists   
        menu_df = pd.read_csv("menu.csv")   
        menu_df["Availability"] = menu_df["Availability"].astype(bool)  # Convert availability back to boolean
    # If file does not exist, menu_df remains an empty DataFrame   

# Save menu items to CSV   
def save_menu():   
    menu_df.to_csv("menu.csv", index=False)   

def main_menu():   
    print('\t', '-' * 15, 'MENU', '-' * 27)   
    print('\t', '*' * 48)   
    print('\t', '|', ' ' * 10, 'CAFE MANAGEMENT SYSTEM', ' ' * 10, '|')   
    print('\t', '*' * 48)   
    print('\t', '|', ' ' * 10, '1. INPUT ITEMS', ' ' * 19, '|')   
    print('\t', '|', ' ' * 10, '2. UPDATE ITEMS', ' ' * 18, '|')   
    print('\t', '|', ' ' * 10, '3. DELETE ITEMS', ' ' * 18, '|')   
    print('\t', '|', ' ' * 10, '4. VIEW ITEMS', ' ' * 20, '|')   
    print('\t', '|', ' ' * 10, '5. ORDER', ' ' * 25, '|')   
    print('\t', '|', ' ' * 10, '6. EXIT', ' ' * 26, '|')   
    print('\t', '*' * 48)   
    print()   

def input_items():   
    item_id = input("Enter Item ID: ")   
    name = input("Enter Item Name: ")   
    category = input("Enter Category (e.g., Coffee, Tea, Pastry): ")  
    price = float(input("Enter Price: "))   
    availability = input("Is the item available? (yes/no): ").strip().lower() == "yes"   
     
    menu_df.loc[len(menu_df)] = [item_id, name, category, price, availability]   
    print("Item added successfully!\n")   
    save_menu()   

def update_items():   
    item_id = input("Enter Item ID to update: ")   
    item_index = menu_df[menu_df["Item ID"] == item_id].index   
     
    if not item_index.empty:   
        print("Current details:", menu_df.loc[item_index[0]])   
        name = input("Enter new Item Name (or press Enter to skip): ")   
        category = input("Enter new Category (or press Enter to skip): ")   
        price = input("Enter new Price (or press Enter to skip): ")   
        availability = input("Is the item available? (yes/no): ").strip().lower()   

        if name:   
            menu_df.at[item_index[0], "Name"] = name   
        if category:   
            menu_df.at[item_index[0], "Category"] = category   
        if price:   
            menu_df.at[item_index[0], "Price"] = float(price)   
        if availability in ["yes", "no"]:   
            menu_df.at[item_index[0], "Availability"] = availability == "yes"   
         
        print("Item updated successfully!\n")   
        save_menu()   
    else:   
        print("Item not found!\n")   

def delete_items():   
    item_id = input("Enter Item ID to delete: ")   
    item_index = menu_df[menu_df["Item ID"] == item_id].index   
     
    if not item_index.empty:   
        menu_df.drop(item_index, inplace=True)
        print("Item deleted successfully!\n")   
        save_menu()   
    else:   
        print("Item not found!\n")   

def view_items():   
    if menu_df.empty:   
        print("No items in the menu.\n")   
    else:   
        print("Current Menu:")   
        print(menu_df.to_string(index=False), "\n")   

def order():   
    order_list = []   
    view_items()   

    while True:   
        item_id = input("Enter Item ID to order (or type 'done' to finish): ")   
        if item_id.lower() == "done":   
            print()   
            break   
         
        item_index = menu_df[(menu_df["Item ID"] == item_id) & 
                             (menu_df["Availability"] == True)].index   
        if not item_index.empty:   
            item = menu_df.loc[item_index[0]]   
            order_list.append(item)   
            print(f"Added {item['Name']} to order.\n")   
        else:   
            print("Item not available or not found.\n")   

    if order_list:   
        print("Your Order:")   
        order_df = pd.DataFrame(order_list, columns=menu_df.columns)   
        print(order_df[["Name", "Price"]].to_string(index=False))   
        total = order_df["Price"].sum()   
        print(f"\nTotal: Rs. {total:.2f}\n")   
    else:   
        print("No items ordered.\n") 

def main():   
    load_menu()   
    while True:   
        main_menu()   
        choice = input("Choose an option (1-6): ")   
        print()   
 
        if choice == '1':   
            input_items()   
        elif choice == '2':   
            update_items()   
        elif choice == '3':   
            delete_items()   
        elif choice == '4':   
            view_items()   
        elif choice == '5':   
            order()   
        elif choice == '6':   
            print("Exiting Cafe Management System. \nTHANK YOU FOR VISITING")   
            break   
        else:   
            print("Invalid choice! Please choose again.\n")   

# Run the main program   
if __name__ == "__main__":   
    main()
