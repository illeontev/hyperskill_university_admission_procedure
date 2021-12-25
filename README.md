# hyperskill_university_admission_procedure
The program that takes the list of students with their marks and returns the lists of the best sudents of their departments

Input file should be called "applicants.txt".

The only input is the number of the best students the program should count.

The result lists are contained in the files.

The algorythm:

1. Read an N integer from the input. This integer represents the maximum number of students for each department.
2. Read the file named applicants.txt once again. Mind one additional column, right after the last exam's result. This column represents the special exam's score. For example, Willie McBride 76 45 79 80 100 Physics Engineering Mathematics(where 100 is the admission exam's score).
3. Choose the best score for a student in the ranking: either the mean score for the final exam(s) or the special exam's score. Use the same set of finals for each Department as in the previous stage. Note that you may need to compare the values several times: for example, if a student doesn't get accepted to the Department of the first priority, compare the finals mean score and the special exam's score once again (but this time, for the second priority department).
4. Output the names and the student's best score, either the mean finals score or the special exam's score to the file
