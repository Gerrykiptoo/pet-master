from pet import Pet

def main():
    # Created a pet with input validation
    while True:
        pet_name = input("Name your pet: ").strip()
        if pet_name:
            my_pet = Pet(pet_name)
            break
        print("Please enter a valid name for your pet!")

    # Interaction loop with better error handling
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed\n2. Play\n3. Sleep\n4. Train\n5. Check Status\n6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        try:
            if choice == '1':
                my_pet.eat()
                print(f"{my_pet.name} enjoyed the meal!")
                
            elif choice == '2':
                my_pet.play()
                print(f"{my_pet.name} had fun playing!")
                
            elif choice == '3':
                my_pet.sleep()
                print(f"{my_pet.name} is well rested!")
                
            elif choice == '4':
                trick = input("Enter trick to teach: ").strip()
                if trick:
                    my_pet.train(trick)
                else:
                    print("Please enter a valid trick name!")
                    
            elif choice == '5':
                my_pet.get_status()
                my_pet.show_tricks()
                
            elif choice == '6':
                print(f"Goodbye! Take care of {my_pet.name}!")
                break
                
            else:
                print("Invalid choice! Please enter 1-6")
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()