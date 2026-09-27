# VIT SGPA Calculator

## Overview

A simple command-line program that helps a student enter their exam marks
and find out their SGPA for the semester.

## Features

- Enter subjects and their credits.
- Enter marks for CAT1, CAT2, TEE, and Internal Assessment.
- See percentage in each exam.
- See how much each exam adds to the final 100 marks.
- See your strongest and weakest subject.
- Calculate SGPA once all exams are done.
- Enter a target SGPA and see what marks you need in the exams left.

## Technologies Used

- Python 3
- Only built-in libraries (`math`) — nothing extra to install

## Project Files

```
vit_sgpa_project/
├── main.py            
├── input_handler.py   
├── calculations.py    
├── display.py         
├── README.md
└── statement.md
```

## How to Install & Run

1. Make sure Python 3 is installed:
  
2. Download or clone this repository.

3. Run the program:
   ```bash
   python3 main.py
   ```
   
4. Follow the on-screen instructions — enter subjects, credits, exams
   conducted, and marks, then pick an option from the menu (1–7).

## How to Test It

- Enter a few subjects and marks, then check option 2 (percentage) gives
  the correct math.
- Try typing a wrong value (like a letter, or a number too big) — the
  program should show an error and ask again, not crash.
- Enter marks for all 3 exams, then check option 4 gives an SGPA.
- Try option 4 with exams still pending — it should say SGPA can't be
  calculated yet.
- Try option 6 (target SGPA) with an exam pending, and check the numbers
  make sense.
- Choose option 7 to make sure the program exits properly.
