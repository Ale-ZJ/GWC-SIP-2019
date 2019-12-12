import json #Import the JSON library to store the data collected
import os.path #library to find paths

def main():
    myanswers = survey() #call the survey function and store in a list

    #code to open all previous responses (JSON -> PYTHON)
    if os.path.isfile('all_ans.json'):
        with open('all_ans.json', 'r') as survey_data:
            old_data = json.load(survey_data)
            #print("\n old: ", old_data)
            myanswers.extend(old_data)

    #code to save all the responses to json (PYTHON -> JSON)
    with open("all_ans.json", 'w') as survey_data: #open the json file to write and read without deleting the previous contents
        survey_data.write("[\n")
        line = 0
        for entry in myanswers:
            json.dump(entry, survey_data) #Save the responses in a json file
            if (line < len(myanswers) - 1):
                survey_data.write(",\n")
            else:
                survey_data.write("\n")
            line += 1
        survey_data.write("]")

def survey():
    finished = False
    list_responses = [] #new list to store dictionaries

    while not finished:
        answers = {} #creates a new dictionary every time thro the loop
        edit = True

        #questions to be asked
        questions = ['name', 'DOB', 'favorite color', 'hometown', 'favorite animal', 'hobby', 'favorite subject']

        #loop to ASK all those questions w/out typing out every single of them
        for q in questions:
            print("What is your {0}? ". format(q))
            answers[q] = input() #creates a key in the answer dictionary with the users input as the value respectively

        #code to EDIT previous responses b4 storing them
        ask_edit = input("\nDo you want to REVIEW your responses? (yes/no)   ").lower()
        if ask_edit == "yes":
            print("Your responses were \n", answers)
            while edit == True:
                ask_what_edit = input("What field do you want to edit?   ")
                if ask_what_edit in questions:
                    i = questions.index(ask_what_edit) #get the index of the key
                    answers[ questions[i] ] = input(questions[i] +":   ") #ask question again
                elif ask_what_edit == "none":
                    edit == False
                else:
                    print("Sorry, I didn't understand you :c ")

        #STORE the dicionary with respones in the list
        list_responses.append(answers)

        #ask the user if they want to continue a NEW survey
        ask_seguir = input ('\nDo you want to continue a NEW survey? (yes/no)   ').lower()
        if ask_seguir == "no":
            finished = True

    return list_responses


if __name__ == "__main__":
    main()
