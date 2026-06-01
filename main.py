from Methods import server, login_input

if __name__ == "__main__":
    # 1. Boot up the database and ensure secure tables exist
    server()  
    
    # 2. Display the application header
    print("\nBajaj Finance - Online Insurance\n")
    
    # 3. Launch the main terminal menu
    login_input()
