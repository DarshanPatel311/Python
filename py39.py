def read_file(file_path):
    try:
        with open(file_path,'w') as f:
         
            print("File content:")
         
            f.write('helloo brother')
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = input('Enter file name: ')
read_file(file_path)
