
"""
Name: Sam Dreyfuss
PennID: 16863023

I worked alone on this assignment, but referenced the following additional websites to further improve my understanding
several topics which I implemented in my program

# sources (these are really for my personal references in the future):
# https://www.geeksforgeeks.org/python-string-find/
# https://www.geeksforgeeks.org/python-get-the-string-after-occurrence-of-given-substring/
# https://www.geeksforgeeks.org/python-list-comprehension-using-if-else/
# https://discuss.python.org/t/multiple-if-s-in-comprehensions-vs-and/18872
# https://www.w3schools.com/python/ref_string_join.asp
# https://www.w3schools.com/python/ref_string_splitlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.geeksforgeeks.org/enumerate-in-python/
# https://www.w3schools.com/python/ref_func_isinstance.asp

"""


def open_read_file(file):
    """
    Functionality:
    Opens up file and reads each line of file into a list

    Arguments:
    file: text file name/specific file

    Returns:
    lines: list of string lines from file
    """

    # open file
    f = open(file, 'r')
    # read lines to variable
    lines = f.readlines()
    # close file
    f.close()
    return lines


def detect_the_name(converted_file):
    """
    Functionality:
    Identifies the name included on the resume (which we assume is the first line of each file)

    Arguments:
    converted_file : text file which is the text file to be converted into a list

    Returns:
    lines: str name found
    """

    # extract first line of text
    name = converted_file[0]

    # strip '\n' used for spacing
    name = name.strip()

    # strip empty spaces
    name = name.strip(' ')

    # confirm name is valid (not lowercase) via try/except
    # if name is invalid, return "Invalid Name"  as name variable
    try:
        if name[0].islower():
            name = 'Invalid Name'
            raise ValueError("The first letter in the name is not uppercase.")
    except ValueError as error:
        print(error)

    return name

def detect_the_email(converted_file):
    """
    Functionality:
    Identifies the email address of the resume file (no matter what number of line its found)

    Arguments:
    converted_file : text file which is the text file to be converted into a list

    Returns:
    email_address: str, which is the email address identified
    """

    # for the email list, extract the specific email address by obtaining the word with @ in it via list comprehension
    character_to_find = '@'
    email_address = [s for s in converted_file if character_to_find in s]

    #strip out the '\n' value
    email_address = email_address[0].strip()

    # strip out any white spaces per instructions
    email_address = email_address.strip(' ')

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
        # If found, change email address to blank
        if any(char.isdigit() for char in email_address):
            email_address = ''

        # If the email address looks sufficient tell the user an email was found in an overly excited matter...
        print('The Email Found is Valid!!!')

    except:
        # if there are any other issues with the email address set the email_address to blank and raise error
        email_address = ''
        raise ValueError("There is an error in the email address.")

    return email_address


def detect_the_course(converted_file):
    """
    Functionality:
    Identifies the courses found in the resume file (no matter what number of line its found)

    Arguments:
    converted_file : text file which is the text file to be converted into a list

    Returns:
    final_course_list_punctuation_screened: list of strings, which are the courses found in the resume
    """

    # the below logic searches each line for the @ character and records the line its found on
    count = 0
    for line in converted_file:
        count += 1
        if 'Courses' in line:
            line_found_number = count

    courses_list = converted_file[line_found_number - 1]

    # remove empty spaces
    courses_list = courses_list.strip()

    # remove 'Courses' & ':-' references
    courses_list = courses_list.strip('Courses')
    courses_list = courses_list.strip()
    courses_list = courses_list.strip(':-')
    #courses_list = courses_list.strip()

    # strip out spaces before and after each course:
    courses_list = courses_list.split(',')

    #final_course_list = []
    final_course_list = [course.strip() for course in courses_list]

    # remove any strange punctuation from the course strings:
    punctuation_to_remove = '_#$&^!*()'
    final_course_list_punctuation_screened = [''.join(val for val in course if val not in punctuation_to_remove) for course in final_course_list]

    return final_course_list_punctuation_screened


def detect_the_project(converted_file):
    """
    Functionality:
    Identifies the projects found in the resume file (no matter what number of line they are found)

    Arguments:
    converted_file : text file which is the text file to be converted into a list

    Returns:
    project_list: list of strings, which are the projects found in the resume
    """

    # the below logic searches each line where the - character is greater or equal to 10 and records the line its found on
    count = 0
    for line in converted_file:
        count += 1
        if line[0] == '-':
            if len(line) >= 10:
                end_of_project_dash_count = len(line) - 1

    # the amount of dashes are reconsructed to make a unique string to reference to define where the end of projects is
    end_of_projects = ''.join('-' for _ in range(end_of_project_dash_count))
    end_of_projects = end_of_projects + '\n'

    # start of projects is defined a where 'Projects' is
    start_of_projects = 'Projects\n'

    # the index values of start_of_projects and end_of projects are used to effectiely slice the list of projects via list comprehension
    project_list = [project for project in converted_file if converted_file.index(start_of_projects) < converted_file.index(project) < converted_file.index(end_of_projects)]

    # strip '\n' used for spacing and blank values
    project_list = [' '.join(s.split()) for s in project_list]

    # strip random '\t' value:
    #project_list = [value.strip('') for value in project_list]

    # remove either blank rows other strange values found in the file:
    final_project_list = []
    for i in project_list:
        if i == '\n' or i == '\t\t\t\t\t\n':
            continue
        final_project_list.append(i)

    # provide new reference back to the project list variable
    project_list = final_project_list

    # remove '':
    project_list = [string_to_test for string_to_test in project_list if string_to_test.strip() != '']

    return project_list


def open_html_template(file2):
    """
    Functionality:
    Opens template html file as a starting point for additional customer html code appending/inserting into new html file

    Arguments:
    file2 : a dynamically named html file the function writes its output to

    Returns:
    None (only file manipulation which is technically not a return)
    """

    # define template resume html file
    file1 = 'resume_template.html'

    # open file and declare as input_file
    with open(file1) as input_file:

        # read all lines in file
        text = input_file.read()

        # split out lines into individual strings
        all_lines = text.splitlines()

        # remove the last 2 lines from list
        altered_lines = all_lines[:-2]

        # compile all remaining lines:
        finalized_lines = '\n'.join(altered_lines)

        # open second file in write mode
        with open(file2,"w") as output_file:

            #write single string to second file
            output_file.write(finalized_lines)



def surround_block(tag, text):

    """
    Functionality:
    Surrounds the given text with the given html tag and returns the string.

    Arguments:
    tag : str, html specific string to surround the text argument
    text: str, the text variable which will be surrounded by html code

    Returns:
    converted_html: str, the combined tect and tag variables which will be read as html code
    """
    # suround text with tags
    converted_html = f'<{tag}>{text}</{tag}>'
    return  converted_html

def create_email_link(email_address):
    """
    Functionality:
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Arguments:
    email_address: str, the email address which will be converted into an html ready format

    Returns:
    converted_email: str, the converted email address
    """

    # remove empty/white spaces
    email_address = email_address.strip()

    #retain the original email address by creating referce with new variable
    original_email = email_address



    # if @ is found in the email, display the email address with an [aT] instead of an @
    if '@' in email_address:
        modified_email = email_address.replace('@','[aT]')
        converted_email = f'<a href="mailto:{original_email}">{modified_email}</a>'
        if email_address == '':
            converted_email = ''
    else:
        converted_email = f'<a href="mailto:{original_email}">{original_email}</a>'

    # if email address came in blank - return converted email blank
    if email_address == "":
        converted_email = ""

    return converted_email



def generate_html(txt_input_file, html_output_file):

    """
    Functionality:
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    Arguments:
    txt_input_file: str, which is the file name to convert
    html_output_file: str, which is the file output name to save in file

    Returns:
    None: (but an outputted html file is maniputled and saved)
    """

    converted_file = open_read_file(txt_input_file)
    name = detect_the_name(converted_file)
    formatted_name = surround_block('h1', name)
    email = detect_the_email(converted_file)
    email_link = create_email_link(email)

    # call all necessary functions:
    converted_file = open_read_file(txt_input_file)
    course_list = detect_the_course(converted_file)
    project_list = detect_the_project(converted_file)

    # call output file to write first block of html code (which is the template block)
    open_html_template(html_output_file)

    html_body_0 = f"""
<div id="page-wrap">
</div>
</div>
{formatted_name}
<p>Email: <a
{email_link}
</div>
"""

    html_body_1 = """
<div>
<h2>Projects</h2>
<ul>"""

    # create dictionary for projects:
    html_body_2 = """"""
    project_dict = {}
    for key, value in enumerate(project_list):

        # use surround block function to automatically convert
        value = surround_block('li', value)
        project_dict[key] = value
        # use key in dict to grab each value
        html_body_2 += f"{project_dict[key]}"

    html_body_3 = """
</ul>
</div>
    """

    # combine the differnt static and dynamic html bodies:
    # convert the course_list into only strings
    course_list = ", ".join(course_list)

    html_body_4 = f"""
<div>
<h3>Courses</h3>
<span>{course_list}<span>
<div>
<div>
</body>
</html>"""

    # aggregate html
    html_body = html_body_0.strip() + "\n" + html_body_1.strip() + "\n" + html_body_2.strip() + "\n" + html_body_3.strip() + "\n" + html_body_4.strip()

    # append the created html body above to the previously queries html template
    with open(html_output_file,'a') as output_file:
        output_file.write(html_body)

def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()
