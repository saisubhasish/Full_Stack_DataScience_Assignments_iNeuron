# This file contains 10 each examples related to the concepts (1) Class, (2) Object, (3)  Consrtuctor, (4) Inheritance, (5) Private,
# (6) Public, (7) Protected, (8) Abstraction, (9) Encapsulation, (10) Polimorphism, (11) Packages, (12) Modules, (13) MethodOverriding
# Using ineuron, studnets, class, class type, number of courses, affiliates, blog, internship, jobs as a reference example

import logging
logging.basicConfig(filename='Task.log', level=logging.INFO)
logging.info("----------------------------------------------------------------------------")



class StudentData:

    """
        concepts : Class, Object & Constructor - 1

        This is my StudentData class which defines
        about student data required to create an
        account in iNeuron portal.

        This class is the example of a constructor by passing positional arguments.

    """
    logging.info('Class Name : StudentData')

    try:
        def __init__(self, first_name, last_name, email, phone):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.phone = phone
    except Exception as e:
        logging.exception(e)

try:
    s = StudentData('Sai Subhasish', 'Rout', 'saisubhasishrout777@gmail.com', 9556332113)

except Exception as e:
    logging.exception(e)

logging.info(s.first_name)
logging.info(s.last_name)
logging.info(s.email)
logging.info(s.phone)

logging.info('----------------------------------------------------------------------------')

class CoursesOffered:

    """
        concepts : Class, Object & Constructor - 2

        This is my CoursesOffered class which defines
        about major Courses Offered in iNeuron

        This class is the example of a constructor without passing any argument.

    """
    logging.info('Class Name : CoursesOffered')

    try:
        def __init__(self):
            self.data_science = 'Full Stack Data Science Bootcamp'
            self.data_analytics = "Full Stack Data Analytics"
            self.developmant = "Full Stack Development"
            self.frontend_development = "Full Stack Web Development"
            self.cloud = "AWS Cloud Masters"
            self.progrsmming = "Data Structure & Algorithms"
            self.marketing = "Digital Marketing Bootcamp"
            self.devops = "GIT-HUB"
            self.teaching = 'Aptitude & Mathematics'
            self.block_chain = 'Full Stack Blockchain Development'

    except Exception as e:
        logging.exception(e)

try:
    c = CoursesOffered()

except Exception as e:
    logging.exception(e)

logging.info(c.data_science)
logging.info(c.data_analytics)
logging.info(c.developmant)
logging.info(c.frontend_development)
logging.info(c.cloud)
logging.info(c.progrsmming)
logging.info(c.marketing)
logging.info(c.devops)
logging.info(c.teaching)
logging.info(c.block_chain)

logging.info('----------------------------------------------------------------------------')

class Products:

    """
        concepts : Class, Object & Constructor - 3

        This is my Products class which defines
        about Products and Services provided
        in iNeuron

        This class is the example of a constructor without passing any argument and logging the output
        in next line by using '\n'

    """
    logging.info('Class Name : Products')

    try:
        def __init__(self):
            self.productsNServices = """ Product and Services : \nCourses,\nInternships, 
            \nJob guarantee and assistance,\nResume Building,\nHack-A-Thon, \nPaymentr,
            \nUI color picker,\nAffiliate Marking """

    except Exception as e:
        logging.exception(e)

try:
    p = Products()

except Exception as e:
    logging.exception(e)

logging.info(p.productsNServices)

logging.info('----------------------------------------------------------------------------')

class Project_Technologies:

    """
        concepts : Class, Object & Constructor - 4

        This is my Project_Technologies class which
        defines different projects for internship
        in iNeuron

        This class is the example of a constructor by passing positional arguments.

    """
    logging.info('Class Name : Project_Technologies')

    try:
        def __init__(self, t1, t2,t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
            self.t1= t1
            self.t2 = t2
            self.t3 = t3
            self.t4 = t4
            self.t5 = t5
            self.t6 = t6
            self.t7 = t7
            self.t8 = t8
            self.t9 = t9
            self.t10 = t10
            self.t11 = t11
            self.t12 = t12

    except Exception as e:
        logging.exception(e)

try:
    p = Project_Technologies('Big Data', 'Bisuness Intelligence', "Computer Vision", "Deep Learning",
                         "Deep Reinforcement Learning", "Development", 'Hackathon KIET', 'NLP',
                         'Machine Learning', "Projectathon", 'Virtual Reality', "Web Development")

except Exception as e:
    logging.exception(e)
logging.info(p.t1)
logging.info(p.t2)
logging.info(p.t3)
logging.info(p.t4)
logging.info(p.t5)
logging.info(p.t6)
logging.info(p.t7)
logging.info(p.t8)
logging.info(p.t9)
logging.info(p.t10)
logging.info(p.t11)
logging.info(p.t12)

logging.info('----------------------------------------------------------------------------')

class Domain:

    """
        concepts : Class, Object & Constructor - 5

        This is my Project_Technologies class which
        defines different projects for internship
        in iNeuron

        This class is the example of a constructor by passing keyword arguments.

    """
    logging.info('Class Name : Domain')

    try:
        def __init__(self,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16):
            self.d1 = d1
            self.d2 = d2
            self.d3 = d3
            self.d4 = d4
            self.d5 = d5
            self.d6 = d6
            self.d7 = d7
            self.d8 = d8
            self.d9 = d9
            self.d10 = d10
            self.d11 = d11
            self.d12 = d12
            self.d13 = d13
            self.d14 = d14
            self.d15 = d15
            self.d16 = d16

    except Exception as e:
        logging.exception(e)

try:
    d = Domain(d15="Telecom",d1="Aggriculture",d14="Technology",d3="Banking, Insurance & Finance",
               d9="Food Industry",d2="Aviation",d6="Education",d12="Retail & Sales",d13="Sports",
               d5="Ecommerce",d8="Film & Entertainment",d10="Health Care",d7="Energy & Petroleum",
               d11="Human Resource",d4="Business Analytics",d16="Transportation & Communication")

except Exception as e:
    logging.exception(e)

logging.info(d.d1)
logging.info(d.d2)
logging.info(d.d3)
logging.info(d.d4)
logging.info(d.d5)
logging.info(d.d6)
logging.info(d.d7)
logging.info(d.d8)
logging.info(d.d9)
logging.info(d.d10)
logging.info(d.d11)
logging.info(d.d12)
logging.info(d.d13)
logging.info(d.d14)
logging.info(d.d15)
logging.info(d.d16)

logging.info('----------------------------------------------------------------------------')

class FSDSSyllabus:

    """
        concepts : Class, Object & Constructor - 6

        This is my FSDSSyllabus class which defines
        the course content of FSDS

        This class is the example of constructor which is executing without passing any argument.

    """
    logging.info('Class Name : FSDSSyllabus')

    try:
        def __init__(self):
            self.c1 = "Python"
            self.c2 = "Stats"
            self.c3 = "Machine learning"
            self.c4 = "Deep learning"
            self.c5 = "Computer vision"
            self.c6 = "Natural language processing"
            self.c7 = "Data analytics"
            self.c8 = "Big data"
            self.c9 = "Ml ops"
            self.c10 = "Cloud"
            self.c11 = "Data structure and algorithm"
            self.c12 = "Architecture"
            self.c13 = "Databases"

    except Exception as e:
        logging.exception(e)

try:
    f = FSDSSyllabus()

except Exception as e:
    logging.exception(e)

logging.info(f.c1)
logging.info(f.c2)
logging.info(f.c3)
logging.info(f.c4)
logging.info(f.c5)
logging.info(f.c6)
logging.info(f.c7)
logging.info(f.c8)
logging.info(f.c9)
logging.info(f.c10)
logging.info(f.c11)
logging.info(f.c12)
logging.info(f.c13)

logging.info('----------------------------------------------------------------------------')

class  Instructors:

    """
        concepts : Class, Object & Constructor - 7

        This is my FSDSSyllabus class which defines
        the course content of FSDS

        This class is the example of constructor which is executing a  by passing keyword arguments.

    """
    logging.info('Class Name : Instructors')

    try:
        def __init__(self,i1,i2,i3,i4,i5,i6):
            self.i1 = i1
            self.i2 = i2
            self.i3 = i3
            self.i4 = i4
            self.i5 = i5
            self.i6 = i6

    except Exception as e:
        logging.exception(e)

try:
    ins = Instructors(i1 = "Sudhanshu Kumar", i2 = "Krish Naik", i3 = "Sunny Savita",
                      i4 = "Mukesh Otwani", i5 = "Navin Reddy", i6 = "Shivan Kumar")

except Exception as e:
    logging.exception(e)

logging.info(ins.i1)
logging.info(ins.i2)
logging.info(ins.i3)
logging.info(ins.i4)
logging.info(ins.i5)
logging.info(ins.i6)

logging.info('----------------------------------------------------------------------------')

class ClassFeatures:

    """
        concepts : Class, Object & Constructor - 8

        This is my ClassFeatures class which defines
        the features and functionality a student get
        in the iNeuron website after enrolling for a
        course

        This class is the example of a constructor without passing any argument.

    """
    logging.info('Class Name : ClassFeatures')

    try:
        def __init__(self):
            self.f1 = "Live class"
            self.f2 = "Pre-uploaded videos"
            self.f3 = "Assignments"
            self.f4 = "Quizzes"

    except Exception as e:
        logging.exception(e)

try:
    c = ClassFeatures()

except Exception as e:
    logging.exception(e)

logging.info(c.f1)
logging.info(c.f2)
logging.info(c.f3)
logging.info(c.f4)

logging.info('----------------------------------------------------------------------------')

class CommunityClasses:

    """
        concepts : Class, Object & Constructor - 9

        This is my CommunityClasses class which defines
        the different community classes conducted by
        instructors of iNeuron

        This class is the example of constructor which is executing by passing keyword arguments.

    """
    logging.info('Class Name : CommunityClasses')

    try:
        def __init__(self, cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10):
            self.cc1 = cc1
            self.cc2 = cc2
            self.cc3 = cc3
            self.cc4 = cc4
            self.cc5 = cc5
            self.cc6 = cc6
            self.cc7 = cc7
            self.cc8 = cc8
            self.cc9 = cc9
            self.cc10 = cc10

    except Exception as e:
        logging.exception(e)

try:
    cc = CommunityClasses(cc1='Block Chain', cc10="Web Automation", cc9="System Design",
                          cc4="Digital Marketing", cc5="Java", cc6="Machine Learning",
                          cc8="SQL", cc2="Cyber Security", cc3="Deep Learning",cc7="NLP")

except Exception as e:
    logging.exception(e)

logging.info(cc.cc1)
logging.info(cc.cc2)
logging.info(cc.cc3)
logging.info(cc.cc4)
logging.info(cc.cc5)
logging.info(cc.cc6)
logging.info(cc.cc7)
logging.info(cc.cc8)
logging.info(cc.cc9)
logging.info(cc.cc10)

logging.info('----------------------------------------------------------------------------')

class AchieversCompanies:

    """
        concepts : Class, Object & Constructor 10

        This is my AchieversCompanies class which defines
        about the companies where students got placed in
        different positions

        This class is the example of constructor which is executing without passing any
        argument and logging the output in next line by using '\n'.

    """
    logging.info('Class Name : AchieversCompanies')

    def __init__(self):
        self.companies = """Name of Companies : \nMicrosoft , \nvmware, \nsalesForce, \nAdobe, \nEY,
        \nDeloitte, \nKPMG, \npwc, \ntcs, \nIBM, \nCapgemini, \naccenture", \nJPMorgan Chase & Co.,
        \nWalmart, \namazon, \nfactal,  \nSWIGGY, \nzomato, \nInfosys, \nwipro, \nMyntra, \npaytm,
        \nSAMSUNG, \nOYO, \nTVS """

try:
    a = AchieversCompanies()

except Exception as e:
    logging.exception(e)

logging.info(a.companies)

logging.info('----------------------------------------------------------------------------')

class StudentDetails(StudentData):

    """

        concepts : Inheritance(Multilevel)

        This is my StudentDetails class which defines
        about student details inherited from parent
        class StudentData

        This class is the example of Multilevel Inheritance
    """
    logging.info('Class Name : StudentDetails')

    def additionalInformation(self):
        logging.info("assignmentSubmitted = 2")
        logging.info("assignmentScore = 100 %")
        logging.info("quizzesScore = 0")
        logging.info("isPlaced = False")

try:
    sd = StudentData('Sai Subhasish', 'Rout', 'saisubhasishrout777@gmail.com', 9556332113)

except Exception as e:
    logging.exception(e)

logging.info(sd.first_name)
logging.info(sd.last_name)
logging.info(sd.email)
logging.info(sd.phone)

logging.info('----------------------------------------------------------------------------')

logging.info('Polymerphism : One object in multiple form is the concept of polymorphism.')
logging.info('Example : Overriding(Constructor, Method), Overloading(Operator)')

logging.info('----------------------------------------------------------------------------')

class ClassAccessibility(ClassFeatures):

    """
        concepts : Inheritance(Multilevel) & Polymorphism: Constructor Overriding

        This is my ClassAccessibility class which defines
        about accessibility of class.

        This class is the example of Constructor Overriding which logging the child class
        constructor's information by using child class object.
    """
    logging.info('Class Name : ClassAccessibility')

    def __init__(self):
        logging.info("A student can access these features after logging in to the website")

try:
    ca = ClassAccessibility()

except Exception as e:
    logging.exception(e)

logging.info('----------------------------------------------------------------------------')

class ClassMode(CoursesOffered):

    """
        concepts : Inheritance(Multilevel) & Polymorphism: Constructor Overriding

        This is my ClassMode class which defines
        about mode of class.

        This class is the example of Constructor Overriding which logging both the parent
        class & child class constructor's information by using child class object.
    """
    logging.info('Class Name : ClassMode')

    try:
        def __init__(self):
            super().__init__()
            logging.info("All these classes are available in iNeuron OTT platform")

    except Exception as e:
        logging.exception(e)

try:
    c = ClassMode()

except Exception as e:
    logging.exception(e)

logging.info('----------------------------------------------------------------------------')

class StudentDetailedInfo(StudentDetails):

    """
        concepts : Inheritance(Multilevel) & Polymorphism: Method Overriding

        This is my StudentDetailedInfo class which defines
        about detailed student information

        This class is the example of Polymorphism which covers Method overriding.
    """
    logging.info('Class Name : StudentDetailedInfo')

    def studentInfo(self):
        logging.info("Please provide the mandatory informations of a student to get registered.")

class StudentDetailedInformation(StudentDetailedInfo):

    """
        concepts : Inheritance(Multilevel) & Polymorphism: Method Overriding

        This is my StudentDetailedInformation class which defines
        about detailed student information

        This class is the example of Polymorphism which covers Method overriding.
    """
    logging.info('Class Name : StudentDetailedInfo')

    def studentInfo(self):
        logging.info("Please provide the mandatory informations like : Name, Phone Number & Email-Id "
                     "of a student to get registered.")

try:
    sdi = StudentDetailedInfo('Sai Subhasish', 'Rout', 'saisubhasishrout777@gmail.com', 9556332113)
    sdim = StudentDetailedInformation('Sai Subhasish', 'Rout', 'saisubhasishrout777@gmail.com', 9556332113)

except Exception as e:
    logging.exception(e)

logging.info(sdi.additionalInformation())

logging.info(sdi.studentInfo())
logging.info(sdim.studentInfo())

logging.info('----------------------------------------------------------------------------')

class StudentCertificate():

    """
        concepts : Inheritance(Multiple) & Polymorphism: Method Overriding

        This is my StudentCertificate class which defines
        number of certificates the student has.

        This class is the example of Polymorphism which covers Method overriding.

    """
    logging.info('Class Name : StudentCertificate')

    try:
        def regulatory(self):
            logging.info("Regulatory : Student must complete 80% of videos to get the certificate")

    except Exception as e:
        logging.exception(e)


    def certificate(self):
        logging.warning("Student is not eligible to generate a certificate as he has not watched "
                        "at-least 75% of the videos")

class StudentInfo(StudentData, StudentCertificate):

    """
        concepts : Inheritance(Multiple) & Polymorphism: Method Overriding

        This is my StudentInfo class which defines
        details of student including Student Data
        and Certification details

        This class is the example of Polymorphism which covers Method overriding.

    """
    logging.info('Class Name : StudentInfo')

    try:
        def regulatory(self):
            logging.info("Regulatory : As per new regulatory a Student must complete at-least 75% of "
                        "videos to get the certificate")

    except Exception as e:
        logging.exception(e)

try:
    si = StudentInfo('Sai', 'Subhasish', "sai@123", 9556332113)
    sc = StudentCertificate()

except Exception as e:
    logging.exception(e)

logging.info(si.first_name)
logging.info(si.last_name)
logging.info(si.email)
logging.info(si.phone)
logging.info(si.certificate())

logging.info(sc.regulatory())
logging.info(si.regulatory())

logging.info('----------------------------------------------------------------------------')


class One_Neuron:
    """
        concepts : Inheritance(Multiple) & Polymorphism: Operator Overloading

        This is my One_Neuron class which defines
        the specification of One_Neuron

        This class is the example of Polymorphism which covers Operator Overloading

    """
    logging.info('Class Name : One_Neuron')

    try:
        def additionOperatorOverloading(self,v1,v2):
            return v1 + v2

    except Exception as e:
        logging.exception(e)

    try:
        def multiplicationOperatorOverloading(self,n1,n2):
            return n1*n2

    except Exception as e:
        logging.exception(e)

    def one_Neuron(self):
        logging.info("It is the branch of iNeuron where all the instructors come together to "
                     "contribute some value to our society free of cost")


class HackAThon:
    """
        concepts : Inheritance(Multiple) & Polymorphism: Operator Overloading

        This is my HackAThon class which defines
        why iNeuron conducts a HackAThon

        This class is the example of Polymorphism which covers Operator Overloading

    """
    logging.info('Class Name : HackAThon')

    try:
        def additionOperatorOverloading(self,v1,v2):
            return v1 + v2

    except Exception as e:
        logging.exception(e)

    try:
        def multiplicationOperatorOverloading(self,n1,n2):
            return n1*n2

    except Exception as e:
        logging.exception(e)

    def hack_a_thon(self):
        logging.info("A HackAThon is conducted by iNeuron to identify the real talent "
              "even the students who are not a part of iNeuron, they also can join it"
              "and the most advantage is the companies who are hunting for real talent "
              "it makes east to them, so as to students")

class Hall_Of_fame:
    """
        concepts : Inheritance(Multiple) & Polymorphism: Operator Overloading

        This is my Hall_Of_fame class which defines
        about the students of iNeuron who successfully
        got placed after studied from iNeuron.
    """
    logging.info('Class Name : Hall_Of_fame')

    def hall_of_fame(self):
        logging.info("In Hall_Of_fame iNeuron posts about th")

class Ineuron(One_Neuron,HackAThon,Hall_Of_fame):
    """
        concepts : Inheritance(Multiple) & Polymorphism: Operator Overloading

        This is my Ineuron class which defines
        the branches of iNeuron

        This class is the example of Polymorphism which covers Operator Overloading

    """
    logging.info('Class Name : Ineuron')

    try:
        def ineuron(self):
            logging.info("Root company")

    except Exception as e:
        logging.exception(e)
try:
    i = Ineuron()
    on = One_Neuron()
    h = HackAThon()

except Exception as e:
    logging.exception(e)

logging.info(i.one_Neuron())
logging.info(i.hack_a_thon())
logging.info(i.hall_of_fame())
logging.info(i.ineuron())

logging.info(on.additionOperatorOverloading('One ', 'Neuron'))
logging.info(on.additionOperatorOverloading(6,12))
logging.info(on.multiplicationOperatorOverloading(5,20))
logging.info(on.multiplicationOperatorOverloading(5,'One_Neuron '))

logging.info(h.additionOperatorOverloading(55,45))
logging.info(h.additionOperatorOverloading('Hack ', 'A Thon'))
logging.info(h.multiplicationOperatorOverloading('Hack_A_Thon ',3))
logging.info(h.multiplicationOperatorOverloading(7,3))

logging.info(i.additionOperatorOverloading(100,18))
logging.info(i.additionOperatorOverloading('i', 'Neuron'))
logging.info(i.multiplicationOperatorOverloading('iNeuron ',7))
logging.info(i.multiplicationOperatorOverloading(7,9))


logging.info('----------------------------------------------------------------------------')

class IneuronCourses:
    """
        concepts : Inheritance(Multilevel) & Encapsulation

        This is my IneuronCourses class which defines
        the courses provided by iNeuron

        This class is the example of Multilevel Inheritance & Encapsulation.

    """
    logging.info('Class Name : IneuronCourses')

    def ineuron_Courses(self):
        logging.info("Here we provide the most demanded course"
                     "'Data Science'")

class FullStackDataScience(IneuronCourses):
    """
        concepts : Inheritance(Multilevel) & Encapsulation

        This is my FullStackDataScience class which defines
        the Full Stack Data Science course.

        This class is the example of Multilevel Inheritance & Encapsulation where '__course'
        value is changed.

    """
    logging.info('Class Name : FullStackDataScience')

    __course = "Data Science Master Class"

    try:
        def newCourse(self, updateCourse):
            self.__course = updateCourse

    except Exception as e:
        logging.exception(e)


    def fullStackDataScience(self):
        logging.info("This course majorly covers the topics Python, "
                     "Statistics, Machine learning, Deep learning, cloud,"
                     "Big data, Databases")

class MachineLearning(FullStackDataScience):
    """
        concepts : Inheritance(Multilevel) & Encapsulation

        This is my MachineLearning class which defines
        the MachineLearning course.

        This class is the example of Multilevel Inheritance & Encapsulation

    """
    logging.info('Class Name : MachineLearning')

    def machineLearning(self):
        logging.info("Machine Learning is the basic pillar of"
                     "Data Science")

try:
    m = MachineLearning()

except:
    logging.exception(e)

logging.info(m.ineuron_Courses())
logging.info(m.fullStackDataScience())
logging.info(m.machineLearning())
logging.info(m._FullStackDataScience__course)
m.newCourse("Full Stack Data Science")
logging.info(m._FullStackDataScience__course)

logging.info('----------------------------------------------------------------------------')

class OH_CEO:
    """
        concepts : Inheritance(Multiple) & Abstraction

        This is my OH_CEO class which defines
        OrganisationHierarchy of iNeuron.

        This class is the example of Multilevel Inheritance & Abstraction where value of '__salary'
        is hidden from outside person.

    """
    logging.info('Class Name : OH_CEO')

    emailIdCEO = 'sudhanshu@ineuron.ai'
    _phoneNumberCEO = 8671525256
    __salaryCEO = 80000000

    def ceo(self):
        logging.info("CEO : Sudhanshu Kumar")

class OH_CoFounder:
    """
            concepts : Inheritance(Multiple) & Abstraction

            This is my OH_CoFounder class which defines
            OrganisationHierarchy of iNeuron.

            This class is the example of Multilevel Inheritance & Abstraction where value of '__salary'
            is hidden from outside person.

        """
    logging.info('Class Name : OH_CoFounder')

    emailIdCoFounder = 'krish@ineuron.ai'
    _phoneNumberCoFounder = 965812453
    __salaryCoFounder = 60000000

    def coFounder(self):
        logging.info("Co-Founder : Krish Naik")

class OH_CTO:
    """
            concepts : Inheritance(Multiple) & Abstraction

            This is my OH_CTO class which defines
            OrganisationHierarchy of iNeuron.

            This class is the example of Multilevel Inheritance & Abstraction where value of '__salary'
            is hidden from outside person.

        """
    logging.info('Class Name : OH_CTO')

    emailIdCTO = 'hitesh@ineuron.ai'
    _phoneNumberCTO = 7054689524
    __salaryCTO = 40000000

    def cto(self):
        logging.info("CTO : Hitesh Choudhary")

class OrganisationHierarchy(OH_CEO,OH_CoFounder,OH_CTO):
    pass

try:
    o = OrganisationHierarchy()
    ceo = OH_CEO()
    cof = OH_CoFounder()
    cto = OH_CTO()

except Exception as e:
    logging.exception(e)

logging.info(o.ceo())
logging.info(o.coFounder())
logging.info(o.cto())

logging.info(o.emailIdCEO)
logging.info(o._phoneNumberCEO)
logging.info(o._OH_CEO__salaryCEO)

logging.info(o.emailIdCoFounder)
logging.info(o._phoneNumberCoFounder)
logging.info(o._OH_CoFounder__salaryCoFounder)

logging.info(o.emailIdCTO)
logging.info(o._phoneNumberCTO)
logging.info(o._OH_CTO__salaryCTO)



logging.info('----------------------------------------------------------------------------')

class StudentDataVariables:

    """
        concepts : Private, Public, Protected & Encapsulation

        This is my StudentDataVariables class which defines
        about the student details with three different
        type of variables.

        This class is the example of Private, Public, Protected, & Encapsulation where
        '__mark' value is changed.

    """
    logging.info('Class Name : StudentDataVariables')

    firstName = "Sai Subhasish"
    lastName = 'Rout'
    __phoneNo = 9556332113
    _email = "saisubhasishrout777@gmail.com"
    __marks = 98

    try:
        def updateMarks(self, newMark):
            self.__marks = newMark

    except Exception as e:
        logging.exception(e)

try:
    sdv = StudentDataVariables()

except Exception as e:
    logging.exception(e)

logging.info(sdv.firstName)
logging.info(sdv.lastName)
logging.info(sdv._StudentDataVariables__phoneNo)
logging.info(sdv._email)
logging.info(sdv._StudentDataVariables__marks)
sdv.updateMarks(99)
logging.info(sdv._StudentDataVariables__marks)

logging.info('----------------------------------------------------------------------------')

class StudentDetailsVariablesType:

    """
        concepts : Private, Public, Protected, & Encapsulation

        This is my StudentDetailsVariablesType class which
        defines about the student details and the functions
        are returning their age & changing the number

        This class is the example of Private, Public, Protected, & Encapsulation where
        '__phoneNo1' value is changed.

    """
    logging.info('Class Name : StudentDetails')


    Name1 = "Pragati Parida"
    _yob1 = 1997
    __phoneNO1 = 7978555555

    def age(self, current_year):
        return current_year-self._yob1
    try:
        def changeNumber(self, newNumber):
            self.__phoneNO1 = newNumber

    except Exception as e:
        logging.exception(e)

try:
    sdvt = StudentDetailsVariablesType()

except Exception as e:
    logging.exception(e)

logging.info(sdvt.Name1)
logging.info(sdvt._yob1)
logging.info(sdvt._StudentDetailsVariablesType__phoneNO1)
logging.info(sdvt.age(2022))
sdvt.changeNumber(7504750522)
logging.info(sdvt._StudentDetailsVariablesType__phoneNO1)

logging.info('----------------------------------------------------------------------------')

class Data:

    """
        concepts : Private, Public, Protected,Abstraction

        This is my Data class which
        defines about variable type.

        This class is the example of Private, Public, Protected, & Abstraction

    """
    logging.info('Class Name : Data')

    __v1 = "Data"
    _v2 = "Master"
    v3 = "Class"

class DataScience(Data):

    """
        concepts : Private, Public, Protected, Abstraction

        This is my DataScience class which
        defines about variable type.

        This class is the example of Private, Public, Protected, & Abstraction where the data
        members of both parent and child class is used and in 'dataScience' method the
        concatenation of all is returned.

    """
    logging.info('Class Name : DataScience')

    __v4 = "Science"
    try:
        def dataScience(self):
            global v5
            v5 = "by iNeuron"
            return self._Data__v1 +" "+ self.__v4 +' '+ Data._v2 +' '+ Data.v3 +" "+ v5

    except Exception as e:
        logging.exception(e)

try:
    ds = DataScience()

except Exception as e:
    logging.exception(e)

logging.info(ds._Data__v1)
logging.info(ds._v2)
logging.info(ds.v3)
logging.info(ds._DataScience__v4)
#logging.info(ds.v5)
logging.info(ds.dataScience())

logging.info('----------------------------------------------------------------------------')

logging.info("Module : Collection of classes is called as a module (eg- This file)")
logging.info("Package : Collection of modules is called as a package")

logging.info('----------------------------------------------------------------------------')















