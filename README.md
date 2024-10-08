# Schedule Planning Challenge

This code was made for a challenge I found on LinkedIn, posted by Demcon. The challenge description can be found at the end of this #README.

## Instructions

1. **Input:**  
   Enter a schedule in the `input.csv` file, which can be found in the `input` folder. The input must be comma-separated (`,`) and contain three columns:
   - The first column is the name of the show/band performing.
   - The second column is an integer representing the start time of the performance.
   - The third column is an integer representing the end time of the performance.
   
   **Note:** Do not include headers in the CSV file. For example:  
show_1,1,3  
show_2,1,4  
show_3,1,3  
show_4,1,2  
show_5,1,6  
show_6,3,8  
show_7,4,7  
show_8,5,8  
show_9,6,10

(I will leave an example input in the file itself )

2. **Execution:**  
Once the input is entered, navigate to `main.py` and run the code. Enter the minimum amount of hours there has to be between perfomances on the same stage. Upon completion, the schedule can be found in the `output` folder.

3. **Output:**  
There are three files located in the `output` folder:
- `info.txt` provides extra details of the schedule or lists any errors if they occurred.
- `schema_verticaal.csv` displays the schedule with the stages as columns and times as values in the rows.
- `schema_horizontaal.csv` displays the schedule with the times as columns and stages as values in the rows.
  
 <br>
 <br>
  
  
  
THE CHALLENGE *
Demcon has decided to expand its activities, and to organize a musical festival. After being an expert in mechatronic systems engineering, the move to the entertainment business seems a rather logical choice.

For the festival 30 acts are hired, such as the Demcon band and other popular acts. Unfortunately, each band has a very tight schedule, and is only able to play at a fixed timeslot. This makes the planning difficult, and the festival organizer needs to know how many stages to prepare for the event.

Your job is to help the festival organization. You are given a list of shows, each with a start and end time. The start and end times are provided as an offset from the start of the festival since the festival goes on non-stop. For example, the first three shows are given like this:

show_1 36 39  
show_2 30 33  
show_3 29 36  

show_1 is scheduled from 36 hours after festival start and will play for 4 long hours up to (and including) hour 39 after festival start.

It can be seen that show_1 and show_3 overlap, since they both play at hour 36. Also show_2 and show_3 overlap, so they cannot share a stage.

Your task is to create a planning program which takes the list of shows, and their start and end times, and creates a planning.

Good luck!
SPECIFICS & RULES

    Please write your solution in Python/C++/Matlab.
    Please add information (in the README) on how to execute the code.
    Your solution should be able to output a schedule explaining where and when each show will be. How you do this, is up to you. Just know that we do like a good-looking and well-constructed output ;)
    We’ve included an example list below for you to get started, but your code should be able to handle any schedule. Additionally, feel free to use another input format or file type, as long as you clearly explain what the input should look like.
    We will evaluate your solutions based on inventiveness, efficiency, and good coding practices.
