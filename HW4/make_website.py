#from doc.pycurl.examples.retriever import filename

# sources:
# https://www.geeksforgeeks.org/python-string-find/
# https://www.geeksforgeeks.org/python-get-the-string-after-occurrence-of-given-substring/


def open_read_file(file):
    """
    Functionality:
    Opens up file and reads each line of file into a list

    Arguments:
    file: text file name

    Returns:
    lines: list of lines
    """

    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines



    """
        f = open(file, "r")

        # create empty dictionary
        my_dict = {}

        cnt = 0

        # reads and prints each line in f (file) while there is a line to read
        line = f.readline()

        while line:
            print(line, end='')
            line = f.readline()

            line_lst = line.strip()

            # skip line if missing value
            if len(line_lst) <= 1:
                continue

            key = line_lst[0].strip()
            value = line_lst[1].strip()

            # add key and value to dictionary
            my_dict[key] = my_dict.get(key, 0) + value

            print("This is the dictionary:", dict)

        f.close()

    # update test
    """


def detect_the_name(converted_file):
    # extract first line of text
    name = converted_file[0]
    # strip '\n' used for spacing
    name = name.strip()

    # strip empty spaces
    name = name.strip(' ')

    # confirm name is valid (not lowercase) via try/except
    # if name is invalid, return "Invalid Name"
    try:
        if name[0].islower():
            first_line = 'Invalid Name'
            raise ValueError("The first letter in the name is not uppercase.")
    except ValueError as error:
        print(error)

    return name




def detect_the_email(converted_file):

    # within the email list, extract the specific email address by obtaining the word with @ in it via list comprehension
    character_to_find = '@'
    email_address = [s for s in converted_file if character_to_find in s]
    #strip out the '\n' value
    email_address = email_address[0].strip()

    # strip out any white spaces per instructions
    email_address = email_address.strip(' ')
    print(email_address)

    try:
        # first, confirm if the email address includes .com or .edu in title, otherwise throw an error
        if not ('.com' in email_address or '.edu' in email_address):
            raise ValueError("The email does not contain a .com or .edu")

        # second, loop through the email adress and confirm if @ is found, then look to the next character to confirm
        # if the value is a lowercase value, otherwise generate an error
        at_char_found = False
        for char in range(len(email_address) - 1):
            if email_address[char] == '@':
                at_char_found = True
                if not email_address[char + 1].islower():
                    raise ValueError("The email does not contain a lowercase letter after @")

        if not at_char_found:
            raise ValueError("The email contains no @ character")

        # third, check if there are any numbers/ints in the email address
        # If found, raise an error
        if any(char.isdigit() for char in email_address):
            raise ValueError("The email is not free of numbers or integers")

        print('The Email Found is Valid!!!')

    except:
        raise ValueError("There Appears to be an error in the email address.")



def detect_the_course(converted_file):

    # the below logic searches each line for the @ character and records the line its found on
    count = 0
    for line in converted_file:
        count += 1
        if 'Courses' in line:
            line_found_number = count

    print("This is the line where it was found", line_found_number)

    print(converted_file[line_found_number - 1])

"""

def detect_the_project(converted_file):
    
"""

def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """

    # insert code
    pass

def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """

    # insert code
    pass

def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """

    # insert code
    pass

def main():

    file = 'resume.txt'
    converted_file = open_read_file(file)
    detect_the_course(converted_file)



    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    #generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    #generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    #generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    #generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    #generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    #generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    #generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()
