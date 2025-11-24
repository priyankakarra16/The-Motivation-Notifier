
# We need the 'random' module to pick a quote without bias.
import random
import os

# --- GLOBAL SETTINGS ---
# Define the name of the file that holds all our inspirational content.
QUOTE_FILE_NAME = "quotes.txt"

# --- CORE FUNCTIONS ---

def fetch_all_wise_words():
    """
    This function handles the critical task of reading all the quotes 
    from the external text file and putting them into a Python list.
    """
    
    # Check if the file exists before trying to open it. This prevents a crash.
    if not os.path.exists(QUOTE_FILE_NAME):
        print("\n[FILE ERROR] !!! Cannot find the required file:", QUOTE_FILE_NAME, "!!!")
        print("Using a hardcoded fallback message instead.")
        # Return a list containing only the fallback message
        return ["*Motivation is an internal job. Get started!* - The Universe"]
        
    try:
        # Open the file for reading. The 'with' statement ensures the file is
        # automatically closed even if an error occurs.
        with open(QUOTE_FILE_NAME, 'r') as quote_file_handle:
            
            # Read every line in the file and store it in a list.
            # We strip the whitespace (like the newline character at the end) 
            # to make the output clean.
            list_of_all_quotes = [line.strip() for line in quote_file_handle if line.strip()]
            
        # Check if the file was empty
        if not list_of_all_quotes:
            print("\n[FILE WARNING] The quote file is empty.")
            return ["*Empty list detected. Your motivation is the need to fill this file!* - The App"]
            
        # If successful, return the list of quotes
        return list_of_all_quotes
        
    except Exception as e:
        # If any unexpected error happens during file access (permission issue, etc.)
        print(f"\n[CRITICAL ERROR] Failed to read the file: {e}")
        return ["*System failure detected. The motivation is to fix the bug!* - The System"]


def select_a_random_quote(list_of_quotes):
    """
    Given the full list of quotes, this function uses the random module
    to pick one item and return it to the main program.
    """
    # The 'choice' function is a simple, effective way to get one random element.
    the_chosen_quote = random.choice(list_of_quotes)
    return the_chosen_quote


def display_quote(quote_text):
    """
    Formats and prints the selected quote to the console in an appealing way.
    """
    print("\n-----------------------------------------------------------")
    print("✨ YOUR DAILY BOOST OF INSPIRATION ✨")
    print("-----------------------------------------------------------")
    print(quote_text)
    print("-----------------------------------------------------------")


def start_the_motivation_machine():
    """
    This is the main function that runs the program. It handles the menu
    and the continuous loop until the user chooses to quit.
    """
    
    # 1. First, load the data only once when the program starts.
    master_list_of_quotes = fetch_all_wise_words()
    
    if not master_list_of_quotes:
        # If the loading function failed completely and returned an empty list (shouldn't happen), 
        # we stop.
        print("FATAL ERROR: Could not load any motivational content. Exiting.")
        return

    # 2. Enter the continuous running loop.
    while True:
        print("\n--- Motivation Menu ---")
        print("1. Get a new inspirational quote")
        print("2. Exit the program")
        
        user_choice = input("Enter your choice (1 or 2): ")

        if user_choice == '1':
            # 3. Call the function to randomly select a quote
            quote_to_show = select_a_random_quote(master_list_of_quotes)
            
            # 4. Display the result
            display_quote(quote_to_show)
            
        elif user_choice == '2':
            print("\n[EXITING] Always stay motivated! Goodbye for now. 👋")
            break # Exit the loop, ending the program
            
        else:
            print("\n[WARNING] That selection was not on the menu. Please try again.")


# --- PROGRAM ENTRY POINT ---

if __name__ == "__main__":
    # This line ensures that the 'start_the_motivation_machine' function is the 
    # first thing to run when the script is executed directly.
    start_the_motivation_machine()
