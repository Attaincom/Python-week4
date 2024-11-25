def modify_file_content(content):
    """Modify the content of the file."""
    # Example modification: Make all text uppercase
    return content.upper()

def main():
    try:
        # Ask the user for the filename to read
        input_filename = input("Enter the name of the file to read: ").strip()
        
        # Open the file for reading
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Ask the user for the name of the new file
        output_filename = input("Enter the name of the new file to write: ").strip()
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'. 🎉")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read or write to the file. Please check permissions or file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
