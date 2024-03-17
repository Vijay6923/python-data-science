def calculate_love_percentage(boy_name, girl_name):
    combined_names = boy_name.lower() + girl_name.lower()
    love_count = 0
    
    # Count occurrences of letters in the word 'love'
    for letter in 'love':
        love_count += combined_names.count(letter)
    
    # Calculate love percentage
    love_percentage = love_count * 10
    
    return love_percentage

def main():
    boy_name = input("Enter the boy's name: ")
    girl_name = input("Enter the girl's name: ")
    
    love_percentage = calculate_love_percentage(boy_name, girl_name)
    
    print(f"The love percentage between {boy_name} and {girl_name} is {love_percentage}%.")

if __name__ == "__main__":
    main()
