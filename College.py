from typing import List


class College:
    course_name = ["collegeName", "calcI", "calcII", "linearAlgebra", "physics", "csI", "csII",
                   "discreteMathOrStructure", "assemblyAndComputerArchitecture"]

    roadmap_template = r"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Welcome to Overleaf --- just edit your LaTeX on the left,
% and we'll compile it for you on the right. If you open the
% 'Share' menu, you can invite other users to edit at the same
% time. See www.overleaf.com/learn for more info. Enjoy!
%
% Note: you can export the pdf to see the result at full
% resolution.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\documentclass[tikz, border=10pt]{standalone}
%%%<
\usepackage{verbatim}
%%%>
\begin{comment}
:Title: Basic Philosophy concepts
:Tags: Diagrams;Graphs;Philosophy
% :Author: Vilson Vieira
% :Slug: philosophy

This graph diagram presents the basic Philosophy concepts of dialectics,
opposition and innovation.
\end{comment}

\tikzset{
    vertex/.style = {
        circle,
        fill = black,
        outer sep = 2pt,
        inner sep = 1pt,
    }
}
\begin{document}
% •  CS 100 - Programming for Everyone Units: 3
% •  CS 100A - Programming for Everyone Workshop Units: 1
% •  CS 101 - Computer Science I Units: 4
% •  CS 180 - Computers in Action Units: 3
% •  CS 200 - Advanced Programming for Everyone Units: 3
% •  CS 201 - Computer Science II Units: 4
% •  CS 211 - Discrete Structures Units: 3
% •  CS 221 - Computer Organization and Assembly Language Units: 3
% •  CS 230 - Computing and Social Responsibility Units: 3 ; G.E./G.R. Area: D1-3
% •  CS 250 - Introduction to Web Programming Units: 3
% •  CS 300 - Data Structures for Everyone Units: 3 ; G.E./G.R. Area: B6
% •  CS 301 - Data Structures and Algorithms Units: 3
% •  CS 311 - Programming Language Concepts Units: 3
% •  CS 321 - Computer Architecture Units: 3
% •  CS 350 - Website Development for Everyone Units: 3
% •  CS 351 - Website Development Units: 3
% •  CS 370 - Databases for Social and Health Sciences Units: 3
% •  CS 398 - Internship Units: 1-3
% •  CS 400 - Computer Programming for Science Units: 3
% •  CS 401 - Software Engineering Units: 3
% •  CS 411 - Automata and Computation Units: 3
% •  CS 413 - Analysis of Algorithms Units: 3
% •  CS 421 - Operating Systems Units: 3
% •  CS 431 - Database Architecture Units: 3
% •  CS 441 - Computer Networks Units: 3
% •  CS 453 - Mobile Programming Units: 3
% •  CS 455 - Computer Graphics Units: 3
% •  CS 461 - Artificial Intelligence Units: 3
% •  CS 471 - Security and Information Assurance Units: 3
% •  CS 490 - Independent Study Units: 1-4
% •  CS 497 - Topics in Computer Science Units: 3
% •  CS 498 - Internship Units: 1-3


\def\ccrowone{-2}
\def\ccrowtwo{\ccrowone+2}

\begin{tikzpicture}
  % Dialectics
%   \node[draw] (CS100) at (0,0) {CS100};
%   \node[draw] (B4) at (3,-3) {Mathematics/QR Placement Category I or II, or successful completion of GE area B4};
  \node[draw] (B4) at (0,-4) {Courses in green are taken at \collegeName \ prior to transferring to California State University East Bay.};
  \node[draw] (B4) at (0,-5) {*Note: The course is not taught at \collegeName.};
  \node[draw,fill=green!20] (CS101) at (1,\ccrowone) {\csI};

%   \draw[->,draw=blue] (B4) to (CS101);

%   \node[draw] (CS180) at (-3,0) {CS180};
% •  CS 200 - Advanced Programming for Everyone Units: 3
%   \node[draw] (CS200) at (0,3) {CS200};

%   \draw[->,draw=blue] (CS100) to (CS200);

  \node[draw,fill=green!20] (CS201) at (2,\ccrowtwo) {\csII};

  \draw[->,draw=blue] (CS101) to (CS201);

  \node[draw,fill=green!20] (lowerdiv) at (-10,2) {\collegeName \ Classes};
  \node[draw,fill=red!20] (lowerdiv) at (-10,3) {CSUEB Lower Division Required Coursework};
  \node[draw,fill=yellow!20] (upperdiv) at (-10,4) {CSUEB Upper Division Required Coursework};
  \node[draw,fill=blue!20] (breadth) at (-10,5) {CSUEB Breadth Coursework (need 2)};


  \node[draw,fill=green!20] (CS211) at (7.5,\ccrowtwo) {\discreteMathOrStructure};

  \node[draw,fill=yellow!20] (STAT316) at (13.25,4.5) {Stat316};
  \node[draw,fill=green!20] (Math130) at (6,\ccrowone) {\calcI};
  \node[draw,fill=green!20] (Math131) at (12,\ccrowone) {\calcII};
  \node[draw,fill=green!20] (Math225) at (16,\ccrowone) {\linearAlgebra};
  \node[draw,fill=green!20] (Phys135) at (20,\ccrowone) {\physics};
  \draw[->,draw=blue] (Math130) to (CS211);
  \draw[->,draw=blue] (Math131) to (STAT316);
  \draw[->,draw=blue] (Math130) to (Math131);
  \draw[->,draw=blue,bend right] (Math130) to (Phys135);
  \draw[->,draw=blue,bend right] (Math130) to (Math225);

  \node[draw,fill=red!20] (CS230) at (-5,3) {CS230};
  \node[draw,fill=green!20] (CS221) at (-2,\ccrowtwo) {\assemblyAndComputerArchitecture};
  \draw[->,draw=blue] (CS101) to (CS221);

   \node[draw,fill=yellow!20] (CS301) at (3,6) {CS301};
   \draw[->,draw=blue] (CS201) to (CS301);
   \draw[->,draw=blue] (CS211) to (CS301);

   \node[draw,fill=yellow!20] (CS311) at (0,6) {CS311};
   \draw[->,draw=blue] (CS201) to (CS311);
   \draw[->,draw=blue] (CS221) to (CS311);

   \node[draw,fill=yellow!20] (CS321) at (-5,6) {CS321};
   \draw[->,draw=blue] (CS221) to (CS321);
   \draw[->,draw=blue,right] (CS211) to (CS321);

   \node[draw,fill=blue!20] (CS351) at (6,6) {CS351};
   \draw[->,draw=blue] (CS301) to (CS351);

   \node[draw,fill=yellow!20] (CS401) at (-10,9) {CS401};
   \node[draw,fill=yellow!20] (CS411) at (-8,9) {CS411};
   \node[draw,fill=yellow!20] (CS413) at (-6,9) {CS413};
   \node[draw,fill=yellow!20] (CS421) at (-4,9) {CS421};
   \node[draw,fill=blue!20] (CS431) at (-2,9) {CS431};
   \node[draw,fill=yellow!20] (CS441) at (0,9) {CS441};
   \node[draw,fill=blue!20] (CS453) at (2,9) {CS453};
   \node[draw,fill=blue!20] (CS455) at (4,9) {CS455};
   \node[draw,fill=blue!20] (CS461) at (6,9) {CS461};
   \node[draw,fill=blue!20] (CS471) at (8,9) {CS471};
   \node[draw] (CS497) at (10,9) {CS490};
   \node[draw] (CS498) at (12,9) {CS497};
   \node[draw] (CS490) at (14,9) {CS498};

   \node[draw] (Consent) at (18,6) {Department Consent and GPA$>2.0$};

   \draw[->,draw=blue] (CS301) to (CS401);
   \draw[->,draw=blue]  (CS211) to (CS411);
   \draw[->,draw=blue] (CS301) to (CS413);
   \draw[->,draw=blue] (CS301) to (CS421);
   \draw[->,draw=blue] (CS301) to (CS431);
   \draw[->,draw=blue] (CS301) to (CS441);
   \draw[->,draw=blue] (CS301) to (CS453);
   \draw[->,draw=blue] (CS301) to (CS455);
   \draw[->,draw=blue] (CS301) to (CS461);
   \draw[->,draw=blue] (CS301) to (CS471);
   \draw[->,draw=blue] (Consent) to (CS490);
   \draw[->,draw=blue] (CS301) to (CS497);


%   \draw[->,draw=blue] (CS101) to (CS498);
%   \draw[->,draw=blue] (CS201) to (CS498);
   \draw[->,draw=blue] (CS301) to (CS498);
   \draw[->,draw=blue] (CS211) to (CS498);
   \draw[->,draw=blue] (CS221) to (CS498);
%   \draw[->,draw=blue] (CS230) to (CS498);
   \draw[->,draw=blue] (Math130) to (CS498);
   \draw[->,draw=blue] (Math131) to (CS498);
   \draw[->,draw=blue] (Math225) to (CS498);
   \draw[->,draw=blue] (Phys135) to (CS498);
%   \draw[->,draw=blue] (CS301) to (CS498);

% •  CS 398 - Internship Units: 1-3
% •  CS 400 - Computer Programming for Science Units: 3
% •  CS 401 - Software Engineering Units: 3
% •  CS 411 - Automata and Computation Units: 3
% •  CS 413 - Analysis of Algorithms Units: 3
% •  CS 421 - Operating Systems Units: 3
% •  CS 431 - Database Architecture Units: 3
% •  CS 441 - Computer Networks Units: 3
% •  CS 453 - Mobile Programming Units: 3
% •  CS 455 - Computer Graphics Units: 3
% •  CS 461 - Artificial Intelligence Units: 3
% •  CS 471 - Security and Information Assurance Units: 3
% •  CS 490 - Independent Study Units: 1-4
% •  CS 497 - Topics in Computer Science Units: 3
% •  CS 498 - Internship Units: 1-3
%   \node[draw,fill=black,text=white] (Antithesis) at (2.3,0) {Antithesis};
%   \node[draw,fill=gray,text=white] (Synthesis) at (1,2) {Synthesis};

%   \draw node[vertex] (Joint) at (1,0) {};

%   \draw[-,draw=blue] (Thesis) to (Joint);
%   \draw[-,draw=blue] (Antithesis) to (Joint);
%   \draw[->,draw=blue] (Joint) to (Synthesis);
%   \draw[->,draw=blue] (Synthesis) to[in=180,out=180] (Thesis);

%   \node at (1.0, -1.0) {\textit{a) Dialectics}};

%   % Opposition
%   \node[draw] (ArgumentA) at (5,0) {Argument};
%   \node[draw,fill=black,text=white] (ArgumentB) at (7.5,0) {Opposition};

%   \draw[->,draw=blue] (ArgumentA) to (ArgumentB);

%   \node at (6., -1.0) {\textit{b) Opposition}};

%   % Innovation
%   \node[draw] (ArgumentA) at (10.1,0) {Argument};
%   \node[draw,fill=black,text=white] (ArgumentB) at (13,0) {Opposition};
%   \node[draw,fill=yellow] (ArgumentC) at (12,2) {Innovation};

%   \draw node[vertex] (Joint) at (11.5,0) {};

%   \draw[-] (ArgumentA) to (Joint);
%   \draw[-] (ArgumentB) to (Joint);
%   \draw[->,draw=blue] (Joint) to (ArgumentC);

%   \node at (11.5, -1.0) {\textit{c) Innovation}};
\end{tikzpicture}
\end{document}
"""

    def __init__(self):
        self.name = ""
        self.calcI = []
        self.calcII = []
        self.linearAlgebra = []
        self.physics = []
        self.csI = []
        self.csII = []
        self.discreteMathOrStructure = []
        self.assemblyAndComputerArchitecture = []

    def getNameCommand(self):
        return r"\newcommand{\collegeName}{" + self.name + "}\n"

    def getCalcICommand(self):
        value = " or ".join(self.calcI) + "}\n" if len("".join(self.calcI)) > 0 else "CalcI Required*}\n"
        return r"\newcommand{\calcI}{" + value.replace(" or }", "}")

    def getCalcIICommand(self):
        value = " or ".join(self.calcII) + "}\n" if len("".join(self.calcII)) > 0 else "CalcII Required*}\n"
        return r"\newcommand{\calcII}{" + value.replace(" or }", "}")

    def getLinearAlgebraCommand(self):
        value = " or ".join(self.linearAlgebra) + "}\n" if len("".join(self.linearAlgebra)) > 0 else "Linear Algebra Required*}\n"
        return r"\newcommand{\linearAlgebra}{" + value.replace(" or }", "}")

    def getPhysicsCommand(self):
        value = " or ".join(self.physics) + "}\n" if len("".join(self.physics)) > 0 else "Physics Required*}\n"
        return r"\newcommand{\physics}{" + value.replace(" or }", "}")

    def getCSICommand(self):
        value = " or ".join(self.csI) + "}\n" if len("".join(self.csI)) > 0 else "Computer Science I Required*}\n"
        return r"\newcommand{\csI}{" + value.replace(" or }", "}")

    def getCSIICommand(self):
        value = " or ".join(self.csII) + "}\n" if len("".join(self.csII)) > 0 else "Computer Science II Required*}\n"
        return r"\newcommand{\csII}{" + value.replace(" or }", "}")

    def getDiscreteMathOrStructureCommand(self):
        value = " or ".join(self.discreteMathOrStructure) + "}\n" if len("".join(self.discreteMathOrStructure)) > 0 else "Discrete Structures Required*}\n"
        return r"\newcommand{\discreteMathOrStructure}{" + value.replace(" or }", "}")


    def getAssemblyAndComputerArchitectureCommand(self):
        value = " or ".join(self.assemblyAndComputerArchitecture) + "}\n" if len("".join(self.assemblyAndComputerArchitecture)) > 0 else "Computer Architecture Required*}\n"
        return r"\newcommand{\assemblyAndComputerArchitecture}{" + value.replace(" or }", "}")
