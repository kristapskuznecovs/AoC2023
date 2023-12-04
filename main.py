# main.py

def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            data = file.readlines()

        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def main():
    day_number = 3  # Change this to the desired day number
    input_file_path = f'input/day{day_number}'
    
    data = read_data_from_file(input_file_path)

    if data:
        # Call the process_data function from the corresponding day's solution
        solution_module = __import__(f'solutions.day{day_number}', fromlist=['process_data'])
        result = solution_module.process_data(data)
        print("Result:", result)

if __name__ == "__main__":
    main()
