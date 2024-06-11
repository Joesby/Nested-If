#Task 1: Code Correction
#request number of attendees and what kind of catering the user is planning
attendees = int(input("Enter number of attendees: "))
vegetarian_option = input("Would you like vegetarian catering? (yes or no): ")

#determine what space is needed based on number of attendees
venue = "large hall" if attendees > 100 else "conference room"

#Task 2: Venue Selection
#determine what equipment is needed based on number of attendees
audio_system = "Yes" if attendees >= 50 else "No"
projector = "Yes" if attendees > 10 else "No"

#Task 3: Catering Choices
#generate catering option based on users choice
catering_option = "Veggie Delight Caterers" if vegetarian_option == "yes" else "Gourmet Meals Caterers"

#display all recommendations based on number of attendees and user choices
print("Type of venue: " + venue)
print("Is an audio system required?: " + audio_system)
print("Is a projector required?: " + projector)
print("Caterers for the event: " + catering_option)