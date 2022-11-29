import os.path
from tkinter import *
from tkinter import ttk, filedialog
from typing import List

from CSUEBTransferCourses.College import College


class GUI:
    def __init__(self, college_data: List[List[str]]):
        self.college_data = college_data

        self.root = Tk()
        self.root.title("CSUEB Transfer Courses")

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.option_add('*tearOff', FALSE)

        Label(self.mainframe, text="Script to generate LaTeX course roadmaps for CC CS schools.").grid(column=1, row=1,
                                                                                                columnspan=2, sticky=W)
        self.selectedCollege = StringVar(self.mainframe)
        self.selectedCollege.set("All")

        college_dict = self.createCollegeDictHelper(college_data)
        college_names = sorted(college_dict.keys())
        college_names.insert(0, "All")

        OptionMenu(self.mainframe, self.selectedCollege, *college_names).grid(column=1, row=4, columnspan=2, sticky=W)

        self.listBox = Listbox(self.mainframe, height=10, width=65)
        self.listBox.grid(column=1, row=2, columnspan=3, sticky=W)

        Label(self.mainframe, text="Destination Folder").grid(column=1, row=3, sticky=E)
        self.filepath = StringVar()
        ttk.Entry(self.mainframe, width=30, textvariable=self.filepath).grid(column=2, row=3, sticky=E)
        self.filepath.set(os.path.expanduser("~/Desktop/CSUEB_Topology/"))

        ttk.Button(self.mainframe, text="Browse", command=self.openFolder).grid(column=3, row=3, sticky=W)

        ttk.Button(self.mainframe, text="Cancel", command=self.root.quit).grid(column=2, row=4,
                                                                               sticky=E)  # sticky aligns to east
        ttk.Button(self.mainframe, text="Generate",
                   command=lambda: self.generateLaTexCommandsFiles(self.college_data)).grid(
            column=3,
            row=4,
            sticky=W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.root.bind("<Return>", self.openFolder)

        self.root.mainloop()

    def openFolder(self, *args):
        filename = filedialog.askdirectory()
        if filename != "":
            print("selected folder")
            self.filepath.set(filename)
        else:
            print("empty")
            os.path.expanduser("~/Desktop/CSUEB_Topology/")

    def quit(self):
        self.root.destroy()

    def generateLaTexCommandsFiles(self, college_data: List[List[str]]):
        college_dict = self.createCollegeDictHelper(college_data)

        self.listBox.delete(0, 'end')

        if self.selectedCollege.get() == "All":
            # 1. Create dictionary of College objects
            college_names = sorted(college_dict.keys())
            for name in college_names:
                self.listBox.insert("end", name + ".tex")

            # 2. Write latex commands for each college
            for _, college in college_dict.items():
                self.createLaTexFile(college)

        else:
            self.listBox.insert("end", self.selectedCollege.get() + ".tex")
            self.createLaTexFile(college_dict[self.selectedCollege.get()])

        print("Done generating LaTex commands.")

    # Helper function to convert college spreadsheet into a map of College objects.
    def createCollegeDictHelper(self, college_data: List[List[str]]) -> dict:
        d = {}

        # 1. Loop through colleges
        for college in college_data:
            college_name = college[0]

            # First time seeing this college, initalize it
            if college_name not in d:
                d[college_name] = College()

            # 2. Add courses to College
            d[college_name].name = college[0]
            d[college_name].calcI.append(college[1])
            d[college_name].calcII.append(college[2])
            d[college_name].linearAlgebra.append(college[3])
            d[college_name].physics.append(college[4])
            d[college_name].csI.append(college[5])
            d[college_name].csII.append(college[6])
            d[college_name].discreteMathOrStructure.append(college[7])
            d[college_name].assemblyAndComputerArchitecture.append(college[8])

        return d

    # Create LaTex command for college.
    # TODO: Deal with multiple courses
    def createLaTexFile(self, college: College) -> None:
        course_name = College.course_name

        # newpath = os.path.expanduser("~/Desktop/colleges/")  # folder location to add colleges
        # If directory doesn't exist, create it
        if not os.path.exists(self.filepath.get()):
            print("Folder doesn't exist, creating one")
            os.makedirs(self.filepath.get())

        # create file in directory (if file exist, replace it)
        with open(os.path.expanduser(self.filepath.get() + "/" + college.name + ".tex"), 'w') as f:
            # Write latex commands to file: \newcommand{\course}{course}
            name_command = college.getNameCommand()
            calcI_command = college.getCalcICommand()
            calcII_command = college.getCalcIICommand()
            linearAlgebra_command = college.getLinearAlgebraCommand()
            physics_command = college.getPhysicsCommand()
            csI_command = college.getCSICommand()
            csII_command = college.getCSIICommand()
            discrete_command = college.getDiscreteMathOrStructureCommand()
            assembly_command = college.getAssemblyAndComputerArchitectureCommand()

            f.write(name_command)
            f.write(calcI_command)
            f.write(calcII_command)
            f.write(linearAlgebra_command)
            f.write(physics_command)
            f.write(csI_command)
            f.write(csII_command)
            f.write(discrete_command)
            f.write(assembly_command)

            f.write(College.roadmap_template)

        # Close file
        f.close()
