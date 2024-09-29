import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_open_read_file(self):
        # test the ability to be able to read the sample resume file correctly
        self.assertEqual("I.M. Student\n", open_read_file("resume.txt")[0])


    def test_detect_the_name(self):
        # test the ability to read the name of test file
        converted_file = open_read_file("resume.txt")
        self.assertEqual('I.M. Student', detect_the_name(converted_file))

        # test the error functionality of a bad name:
        converted_file = open_read_file("resume.txt")
        converted_file = converted_file[0].strip()
        converted_file = converted_file.lower()
        self.assertEqual('Invalid Name', detect_the_name(converted_file))

    def test_detect_email(self):
        converted_file = open_read_file("resume.txt")
        self.assertEqual('tonyl@seas.upenn.edu',detect_the_email(converted_file))


    def test_detect_the_course(self):
        converted_file = open_read_file("resume.txt")
        self.assertEqual(['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering'],detect_the_course(converted_file))


    def test_detect_the_project(self):
        converted_file = open_read_file("resume.txt")
        self.assertEqual(['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.\n', 'Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)\n'],detect_the_project(converted_file))

    '''
    def test_open_html_tamplate(self):
        with open('resume.html', 'r') as file1:
            lines = file1.readlines()
            file1.close()

        print(lines)

        # remove the last 2 lines
        file1 = lines[:-2]
        #print(file1)
        file2 = 'resume.html'
        open_html_template(file2)
        #file1 = open('resume_template.html', 'r', encoding='cp1252')
        file2 = open('resume.html','r',encoding='cp1252')
        self.assertAlmostEquals(file1,file2.read())
    '''

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




# contents_file_2 = open('resume.html','r',encoding='cp1252')
# print(contents_file_2.read())


    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )


if __name__ == '__main__':
    unittest.main()
