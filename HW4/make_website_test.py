import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_open_read_file(self):
        # test the ability to be able to read the sample resume file correctly (first line)
        self.assertEqual("I.M. Student\n", open_read_file("resume.txt")[0])


    def test_detect_the_name(self):
        # test the ability to read the name of test file (typical case)
        # we are assuming the name is always on the first line of the file per the instructions
        converted_file = open_read_file("resume.txt")
        self.assertEqual('I.M. Student', detect_the_name(converted_file))

        # test the error functionality of a bad name (non-typical case):
        converted_file = open_read_file("resume.txt")
        converted_file = converted_file[0].strip()
        converted_file = converted_file.lower()
        self.assertEqual('Invalid Name', detect_the_name(converted_file))

    def test_detect_email(self):
        # detect the email (typical case)
        converted_file = open_read_file("resume.txt")
        self.assertEqual('tonyl@seas.upenn.edu',detect_the_email(converted_file))

        # test wrong email results in blank email returned to html
        converted_file = open_read_file('TestResumes/resume_wrong_email/resume.txt')
        self.assertEqual('', detect_the_email(converted_file))

    def test_detect_the_course(self):
        # detecting the courses (typical case)
        converted_file = open_read_file("resume.txt")
        self.assertEqual(['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering'],detect_the_course(converted_file))

        # test course with white spaces (non-typical case)
        converted_file = open_read_file("TestResumes/resume_courses_w_whitespace/resume.txt")
        self.assertEqual(['Programming Languages and Techniques', 'Biomedical image analysis', 'Pottery'],detect_the_course(converted_file))

        # test course with weird puctuation (non-typical case)
        converted_file = open_read_file("TestResumes/resume_courses_weird_punc/resume.txt")
        self.assertEqual(['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering'],detect_the_course(converted_file))

    def test_detect_the_project(self):
        # test we can detect the project(s) (typical case)
        converted_file = open_read_file("resume.txt")
        self.assertEqual(['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.', 'Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)'],detect_the_project(converted_file))

        """
        # test we can detect the project(s) with whitespaces (non-typical case)
        converted_file = open_read_file("TestResumes/resume_projects_w_whitespace/resume.txt")
        self.assertEqual(['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.\n','Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)\n'],detect_the_project(converted_file))

    
        # test we can detect the project(s) with blanks (non-typical case)
        converted_file = open_read_file("TestResumes/resume_projects_with_blanks/resume.txt")
        self.assertEqual(['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.\n','Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)\n'],detect_the_project(converted_file))
        """

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))


    def test_create_email_link(self):

        # test email with @ sign (typical)
        self.assertEqual('<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',create_email_link('lbrandon@wharton.upenn.edu'))

        # test email with @ sign (typical)
        self.assertEqual('<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',create_email_link('krakowsky@outlook.com'))

        # test email without @ sign (typical)
        self.assertEqual('<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',create_email_link('lbrandon.at.seas.upenn.edu'))

        # test email with white spaces (non-typical)
        self.assertEqual(('<a ' 'href="mailto:lbrandon4@wharton.upenn.edu">lbrandon4[aT]wharton.upenn.edu</a>'),create_email_link('lbrandon4@wharton.upenn.edu'))

        # test email with numners in it (non-typical)
        self.assertEqual('<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',create_email_link('     lbrandon@wharton.upenn.edu'))

    """
    Please note that per the instructions on the Unit Testing evaluation portion of the homework PDF, I didnt't
    include Unit testing for function that writes/appends to a file (specifically generate_html, open_html_template, 
    """

if __name__ == '__main__':
    unittest.main()

