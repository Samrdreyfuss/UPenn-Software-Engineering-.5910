#from doc.pycurl.examples.retriever import filename
#from openai import project

# sources:
# https://www.geeksforgeeks.org/python-string-find/
# https://www.geeksforgeeks.org/python-get-the-string-after-occurrence-of-given-substring/
# https://www.geeksforgeeks.org/python-list-comprehension-using-if-else/
# https://discuss.python.org/t/multiple-if-s-in-comprehensions-vs-and/18872
# https://www.w3schools.com/python/ref_string_join.asp
# https://www.w3schools.com/python/ref_string_splitlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.geeksforgeeks.org/enumerate-in-python/
# https://www.w3schools.com/python/ref_func_isinstance.asp


def open_read_file(file):
    """
    Functionality:
    Opens up file and reads each line of file into a list

    Arguments:
    file: text file name/specific file

    Returns:
    lines: list of lines from file
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
    Identifies the name included on the resume

    Arguments:
    converted_file : text file name/specific file

    Returns:
    lines: list of lines from file
    """

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
            name = 'Invalid Name'
            raise ValueError("The first letter in the name is not uppercase.")
    except ValueError as error:
        print(error)

    return name

def detect_the_email(converted_file):

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
        # If found, raise an error
        if any(char.isdigit() for char in email_address):
            email_address = ''

        print('The Email Found is Valid!!!')

    except:
        email_address = ''
        raise ValueError("There is an error in the email address.")

    return email_address


def detect_the_course(converted_file):

    # the below logic searches each line for the @ character and records the line its found on
    count = 0
    for line in converted_file:
        count += 1
        if 'Courses' in line:
            line_found_number = count

    courses_list = converted_file[line_found_number - 1]
    #remove empty spaces
    courses_list = courses_list.strip()

    #remove 'Courses' & ':-'
    courses_list = courses_list.strip('Courses')
    courses_list = courses_list.strip()
    courses_list = courses_list.strip(':-')
    courses_list = courses_list.strip()
    # strip out spaces before and after each course:
    courses_list = courses_list.split(',')
    #final_course_list = []
    final_course_list = [course.strip() for course in courses_list]

    # remove any strange punctuation from the course strings:

    punctuation_to_remove = '_#$&^!*()'

    final_course_list_punctuation_screened = [''.join(val for val in course if val not in punctuation_to_remove) for course in final_course_list]

    return final_course_list_punctuation_screened


def detect_the_project(converted_file):

    count = 0
    for line in converted_file:
        count += 1
        if line[0] == '-':
            if len(line) >= 10:
                end_of_project_dash_count = len(line) - 1

    end_of_projects = ''.join('-' for _ in range(end_of_project_dash_count))
    end_of_projects = end_of_projects + '\n'

    start_of_projects = 'Projects\n'

    project_list = [project for project in converted_file if converted_file.index(start_of_projects) < converted_file.index(project) < converted_file.index(end_of_projects)]

    # strip '\n' used for spacing and blank values
    project_list = [value.strip(' ') for value in project_list]

    final_project_list = []
    for i in project_list:
        if i == '\n' or i == '\t\t\t\t\t\n':
            continue
        final_project_list.append(i)

    project_list = final_project_list

    return project_list


def open_html_template(file2):
    file1 = 'resume_template.html'

    with open(file1) as input_file:

        # reads all lines as a single string
        text = input_file.read()

        # split out lines
        all_lines = text.splitlines()

        # remove the last 2 lines
        altered_lines = all_lines[:-2]

        # compile all remaining lines:
        finalized_lines = '\n'.join(altered_lines)

        # open second file in write mode
        with open(file2,"w") as output_file:

            # contents_file_2 = open('resume.html','r',encoding='cp1252')
            # print(contents_file_2.read())

            #write single string to second file
            output_file.write(finalized_lines)



def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """

    converted_html = f'<{tag}>{text}</{tag}>'
    return  converted_html

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
    # display the email address with an [aT] instead of an @
    original_email = email_address

    if email_address == "":
        converted_email = ""

    if '@' in email_address:
        modified_email = email_address.replace('@','[aT]')
        converted_email = f'<a href="mailto:{original_email}">{modified_email}</a>'
    else:
        converted_email = f'<a href="mailto:{original_email}">{original_email}</a>'

    return converted_email


    #txt_input_file, html_output_file
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

    converted_file = open_read_file(txt_input_file)
    name = detect_the_name(converted_file)
    formatted_name = surround_block('h1', name)
    email = detect_the_email(converted_file)
    email_link = create_email_link(email)

    # call all necessary functions:
    converted_file = open_read_file(txt_input_file)
    course_list = detect_the_course(converted_file)
    project_list = detect_the_project(converted_file)
    #open_html_template()
    #surrounded_block = surround_block(tag, text)
    #create_email_link(email)

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
        value = surround_block('li', value)
        project_dict[key] = value
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
