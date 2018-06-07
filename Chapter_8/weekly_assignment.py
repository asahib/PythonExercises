def course_grader(test_scores):
    # Your code here
    total_score = 0
    for test_score in test_scores:
        if test_score < 50:
            return "fail"
        else:
            total_score += test_score
            
    return "pass" if total_score/len(test_scores) >= 70 else "fail"

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()

 