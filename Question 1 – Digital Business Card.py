def create_business_card():
    """
    Asks the user to input data for their business card
    Limits phone number to one character
    Ensures names and job title are capitalised correctly
    Email address is always in lowercase
    :return:
    """
    business_card = {}
    business_card["Name"] = input(str("Please enter your name: ")).title()
    while True:
        business_card["Email"] = input(str("Please enter your email: ")).lower()
        if '@' not in business_card["Email"]:
            print(f"Error: You did not enter a valid email. Please try again.")
            continue
        else:
            break
    while True:
        business_card["Phone Number"] = input(str("Please enter your phone number: "))
        if len(business_card["Phone Number"]) != 10:
            print(f"Error: You entered {len(business_card["Phone Number"])} characters. Please enter exactly 10.")
            continue
        else:
            break
    business_card["Job Title"] = input(str("Please enter your job title: ")).title()
    print('---Business Card---')
    for key, value in business_card.items():
        print(f"{key}: {value}")

create_business_card()