import sys
import csv

WEIGHTS = {
    'attendance'    :   0.05,
    'cold_calls'    :   0.2,
    'intention'     :   0.1,
    'midpoint'      :   0.15,
    'final_presentation'    :   0.25,
    'final_report'  :   0.25
}

ASSIGNMENTS = ['attendance', 'cold_calls', 'intention', 'midpoint', 'final_presentation', 'final_report']

def compute_grade(grade_map, weights):
    score = 0
    for assign, grade in grade_map.items():
        weight = WEIGHTS[assign]
        score += grade * weight
    return score

def main():
    grades_f = sys.argv[1]
    out = csv.writer(sys.stdout)

    with open(grades_f, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            try:
                name = row[0]
                pid = row[2]
                attendance = float(row[5])
                final_presentation = float(row[6])
                cold_calls = float(row[7])
                intention = float(row[8])
                midpoint = float(row[9])
                final_report = float(row[10])
                
                grade_map = {
                    'attendance'    :   attendance,
                    'cold_calls'    :   cold_calls,
                    'intention'     :   intention,
                    'midpoint'      :   midpoint,
                    'final_presentation'    :   final_presentation,
                    'final_report'      :   final_report
                }
                
                out.writerow([name, pid, compute_grade(grade_map, WEIGHTS)])
            except:
                continue

if __name__ == "__main__":
    main()
