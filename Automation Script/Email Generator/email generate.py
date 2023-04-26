import datetime
run = True
arc_colab = {"a": "ARC Cluster", "g": "Google Colab"}
while run:
    reminder_or_email = input("Reminder or Email (r/e)? ")
    type = input("Series or Independent (s/i)? ")
    if type == "s":
        arc_or_colab = input("ARC or Google Colab (a/g)? ")
    where = input("Online or In-person (o/i)? ")
    instructor = input("Instructor name? Nhat Nguyen (n), Dhruv Singh (d), Kranthi Yellugari (k), Baru Yogesh (b): ")
    instructor_name = {"n": "Nhat Nguyen", "d":"Dhruv Singh", "k":"Kranthi Yellugari", "b":"Baru Yogesh"}
    instructor_email = {"n": "nguye2hq@mail.uc.edu", "d":"singhdv@mail.uc.edu", "k":"yellugki@mail.uc.edu", "b":"yogeshbv@mail.uc.edu"}
    start_time = input("Start time? ")
    end_time = input("End time? ")
    def supplemental(workshop_type):
        if workshop_type == "arc":
            return f"""For supplemental information, please see the instructions for connecting to the ARC Cluster on our Python guide, which can be accessed through this link: http://guides.libraries.uc.edu/python. The instructions can be found under the "Accessing ARC Cluster" tab, and we highly recommend reviewing them prior to the workshop."""
        else:
            return "For supplemental information, see http://guides.libraries.uc.edu/" + workshop_type + "."
    browser_remind = "Please have Google Chrome (preferred) or Mozilla Firefox web browser installed."
    game = f"""In this workshop, participants will explore PyGame, a Python module used for building 2D games. In this workshop, attendees will learn about the workflow of a game, the terminology of game development, and building a simple game.

Prior to the workshop, attendees are required to have Python 3.7 or higher installed on their laptops. Need help installing python? Contact engrlib2@ucmail.uc.edu or bring your questions to the front desk at the CEAS Library. {supplemental("python")}  """
    discord = f"""This is a standalone Python workshop taught on the Google Colab platform. Attending the CEAS Library's Introduction to Python workshops and experience with Python or any other programming language is strongly recommended. This workshop goes over the creation of bots for Discord, a popular text messaging platform, for task automation, server management, and miscellaneous fun applications. Both a Google account and Discord account are required for this workshop.
{browser_remind} {supplemental("python")}"""
    julia = f"""Julia is general purpose programming language with a wide range of applications, including data science, complex linear algebra, data mining, and machine learning. It has evolved quickly since its inception in 2012 and its user base has grown significantly with high-profile users like NASA, BlackRock, Aviva and INPE to name a few. This workshop will introduce the basics of the Julia programming language with a focus on Variables and Types, Functions, Data Structurers and Control Flow. Beginners are encouraged to attend, and no prior programming experience is required.
{browser_remind} {supplemental("julia")}"""
    matlab = f"""Come and learn the basics of this Technical Computing language.  MATLAB is often used as a scripting language for applications such as data processing, operating on matrices and data plotting. This workshop will cover variables, data types, arrays, operators, conditions, loops, functions and plotting.  The focus will be on the hands-on exercises to help provide a better understanding of MATLAB.  No programming experience is necessary, and beginners are encouraged to attend.  Registration is required. {supplemental("matlab")}. Due to licensing restrictions, only CEAS users may register and attend."""
    latex = f"""LaTeX is an open-source document preparation system widely used in Engineering, Mathematics, natural sciences and other disciplines. Using LaTeX, you can write articles and reports faster and easier than by using word processors such as MS Word especially when using mathematical symbols, equations and when generating bibliographies. This introductory workshop is aimed at getting familiar with the bare bones features of LaTeX and will include a brief introduction to tools such as BiBTeX.
{browser_remind} {supplemental("latex")}"""
    introduction_python_p1 = f"""This is the first workshop in a series of five Python workshops being taught on {arc_colab[arc_or_colab]}. Learn the basics of Python, a widely used and general-purpose programming language. Python is useful for a wide range of applications, including data processing, parsing, web services, and more. This workshop is on the basics of Python, including strings, lists, tuples, sets, dictionaries, and comparators.  Beginners are encouraged to attend, and no prior programming experience is required. 
{browser_remind}"""
    introduciton_python_p2 = f"""This is the second workshop in a series of five Python workshops being taught on {arc_colab[arc_or_colab]}. This workshop deals with more basics of Python, which includes control flow, loops, functions and variable scope. Beginners are encouraged to attend, and Introduction to Python - Part 1 is recommended.  
{browser_remind}"""
    intermediate_python = f"""This is the third workshop in a series of five Python workshops being taught on {arc_colab[arc_or_colab]}. Intermediate Python builds on the topics of the "Introduction to Python" workshops. Basic knowledge of Python or attending the "Introduction to Python" beginner workshops is strongly recommended.  Topics will include: Modules, Imports, Classes/Objects, Packages, Libraries, and File I/O.   
{browser_remind}"""
    data_analysis_series = f"""The Python workshops being taught on {arc_colab[arc_or_colab]}. Basic knowledge of Python or attendance of the previous workshops is strongly recommended. We will work with a data file using the Pandas and Numpy packages. Some topics that will be covered include exploring a Pandas dataframe object, dataframe and series slicing and indexing, querying dataframes, running statistics on dataframes, grouping and aggregations on dataframes and making basic plots with Pandas.  
{browser_remind}"""
    data_visualization_series = f"""This is the fifth workshop in the series of five Python workshops being taught on {arc_colab[arc_or_colab]}. Attending the prior workshops and experience with Python or any other programming language is strongly encouraged. This workshop focuses on three visualization libraries, matplotlib, pandas, and seaborn. Beginners are encouraged to attend the first four workshops, before attending the Data Visualization. 
{browser_remind}"""
    data_analysis_standalone = data_analysis_series
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    workshop_standalone = {"d": discord, "j": julia, "m": matlab, "l": latex, "p": data_analysis_standalone}
    workshop_name = {"d": "Discord Bot Development with Python", "j": "Introduction to Julia", "m": "Introduction to MATLAB", "l": "Introduction to LaTeX", "p": "Data Analysis with Python"}
    workshop_series = ["Introduction to Python - Part 1", "Introduction to Python - Part 2", "Intermediate Python", "Data Analysis with Python", "Data Visualization with Python"]
    workshop_series_content = [introduction_python_p1, introduciton_python_p2, intermediate_python, data_analysis_series, data_visualization_series]
    colab_link_python = ["https://colab.research.google.com/github/The-CEAS-Library/Introduction_to_Python_Part1", "https://colab.research.google.com/github/The-CEAS-Library/Introduction_to_Python_Part2", "https://colab.research.google.com/github/The-CEAS-Library/Intermediate_Python", "https://colab.research.google.com/github/The-CEAS-Library/Data_Analysis_with_Python", "https://colab.research.google.com/github/The-CEAS-Library/Data_Visualization_with_Python"]
    binder_link_python = ["https://mybinder.org/v2/gh/The-CEAS-Library/Introduction_to_Python_Part1.git/master","https://mybinder.org/v2/gh/The-CEAS-Library/Introduction_to_Python_Part2.git/master", "https://mybinder.org/v2/gh/The-CEAS-Library/Intermediate_Python.git/master", "https://mybinder.org/v2/gh/The-CEAS-Library/Data_Analysis_with_Python.git/master", "https://mybinder.org/v2/gh/The-CEAS-Library/Data_Visualization_with_Python.git/master"]
    # dat_visualization_standalone
    if reminder_or_email == "e":
        today_or_not = "today, "
    elif reminder_or_email == "r":
        today_or_not = ""
    match where:
        case "o":
            match type:
                case "s":
                    date = input("Date? (MM/DD/YYYY): ")
                    date_obj = datetime.datetime.strptime(date, "%m/%d/%Y")
                    with open('link_id.txt', 'r') as file:
                    # Initialize lists to store the values for link and id
                        link = []
                        id = []

                        # Loop through each line in the file
                        for line in file:
                            # Strip the newline character from the end of the line
                            line = line.strip()

                            # Append the value to the appropriate list
                            if line.startswith("https"):
                                link.append(line)
                            else:
                                id.append(line)
                        # id = [id1, id2, id3, id4, id5]
                        # link = [link1, link2, link3, link4, link5]
                    with open("email.txt", "w") as f:
                        for i in range(5):
                            workshop_date = date_obj + datetime.timedelta(days=i)
                            # determine the number of days in the month
                            month = workshop_date.month
                            if month in [4, 6, 9, 11]:
                                num_days = 30
                            elif month == 2:
                                if workshop_date.year % 4 == 0 and (workshop_date.year % 100 != 0 or workshop_date.year % 400 == 0):
                                    num_days = 29
                                else:
                                    num_days = 28
                            else:
                                num_days = 31
                            
                            # ensure the day is within range
                            day = min(workshop_date.day, num_days)  
                            # f.write the workshop information
                            f.write(f"""Hello everyone,\n\n""")
                            f.write(f"""Thanks for registering for the ‘{workshop_series[i]}’ workshop, scheduled for {today_or_not}{weekday[i]}, {month}/{day}/{workshop_date.year}, from {start_time} to {end_time} online. The workshop will be taught by {instructor_name[instructor]}.\n""")                        
                            f.write(f"""{workshop_series_content[i]}\n""")
                            f.write(f"""We will use Google Colab Notebooks - an interactive web-based tool, to run Python code online in a “Jupyter notebook” environment on a web browser. You don’t need any additional installations.\n\n""")
                            f.write("Workshop notebook Links:\n") 
                            f.write(f"""{colab_link_python[i]}\n""")
                            f.write(f"""{binder_link_python[i]}\n""")
                            f.write(f"""
Note: This workshop will be hosted online through Zoom. 
Meeting: {link[i]}
Meeting ID: {id[i]}
If you have any further questions, do not hesitate to reach out to me or our instructor, {instructor_name[instructor]} ({instructor_email[instructor]}). \n\n""")

        case "i":
            location = input("Location? ")
            match type:
                case "s":
                    if "Digital Future Building" in location:
                        parking_location = f"""Please note that there is a parking garage under the Digital Futures building , rates begin at $4 for a half hour.
If you have an existing parking permit to another garage on campus, you have full reciprocity to park across the street at the Winslow Lot across 1819 Innovation Hub. See attached map for reciprocity lot location.

Digital Futures is also serviced by two UC Campus Shuttles during the grand opening: CCM Plaza and MainStreet/1819. These shuttles can be tracked in real time using the Transloc App or visiting: http://uc.doublemap.com/map/.\n\n"""
                        instruction = "To get there, you can take the elevator to the 2nd floor, turn right, walk down the hallway, the classroom will be on the left.\n\n"
                    else:
                        parking_location = ""
                        instruction = ""
                    date = input("Date? (MM/DD/YYYY): ")
                    date_obj = datetime.datetime.strptime(date, "%m/%d/%Y")
                    with open("email.txt", "w") as f:
                    
                        for i in range(5):
                            workshop_date = date_obj + datetime.timedelta(days=i)
                            # determine the number of days in the month
                            month = workshop_date.month
                            if month in [4, 6, 9, 11]:
                                num_days = 30
                            elif month == 2:
                                if workshop_date.year % 4 == 0 and (workshop_date.year % 100 != 0 or workshop_date.year % 400 == 0):
                                    num_days = 29
                                else:
                                    num_days = 28
                            else:
                                num_days = 31
                            
                            # ensure the day is within range
                            day = min(workshop_date.day, num_days)  
                            # f.write the workshop information
                            f.write(f"""Hello everyone,\n\n""")
                            f.write(f"""Thanks for registering for the ‘{workshop_series[i]}’ workshop, scheduled for {today_or_not}{weekday[i]}, {month}/{day}/{workshop_date.year}, from {start_time} to {end_time} at {location}. The workshop will be taught by {instructor_name[instructor]}.\n\n""")
                            if parking_location != "":
                                f.write(f"""{instruction}""")
                                f.write(f"""{parking_location}""")
                                
                            f.write(f"""{workshop_series_content[i]}\n""")
                            
                            if arc_or_colab == "g":
                                f.write(f"""\n{supplemental("python")}""")
                                f.write(f""" We will use Google Colab Notebooks - an interactive web-based tool, to run Python code online in a “Jupyter notebook” environment on a web browser. You don’t need any additional installations.\n\n""")
                                f.write("Workshop notebook Links:\n") 
                                f.write(f"""{colab_link_python[i]}\n""")
                                f.write(f"""{binder_link_python[i]}\n""")
                                f.write(f"""Following are a few important points associated with the workshop,
    1. Please bring your laptop to the workshop.
    2. Please have Google Chrome (preferred) or Mozilla Firefox web browser installed on your computer.
    3. Installing python is not required for this workshop.   

You may install Python using the guides below.  

    Python installation guide can be found at https://wiki.python.org/moin/BeginnersGuide/Download
    Python installation is also found at - http://guides.libraries.uc.edu/python
    You can also use the online compiler - https://replit.com/languages/python3\n\n""")
                            else:
                                f.write(f"""\n{supplemental("arc")}\n\n""")
                            f.write(f"""If you have any further questions, do not hesitate to reach out to me or our instructor, {instructor_name[instructor]} ({instructor_email[instructor]}). \n\n""")
                case i:
                    date = input("Date? (weekday, MM/DD/YYYY): ")
                    name = input("What workshop? Discord (d), Julia (j), MATLAB (m), LaTeX (l), Data Analysis with Python (p)? ")
                    f.write(f"""Hello everyone,\n\n""")
                    f.write(f"""Thanks for registering for the ‘{workshop_name[name]}’ workshop, scheduled for {today_or_not}{date}, from {start_time} to {end_time} at {location}. The workshop will be taught by {instructor_name[instructor]}.\n""")
                    f.write(f"""{workshop_standalone[name]}\n""")
                    f.write(f"""We will use Google Colab Notebooks - an interactive web-based tool, to run Python code online in a “Jupyter notebook” environment on a web browser. You don’t need any additional installations.\n""")
                    f.write(f"""If you have any further questions, do not hesitate to reach out to me or our instructor, {instructor_name[instructor]} ({instructor_email[instructor]}. \n\n""")

                    
    close = input("Run the program again to generate another email? (y/n): ")
    if close == "n":
        run = False     

