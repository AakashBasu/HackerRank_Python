if __name__ == '__main__':
    n = int(input())
    if 2 <= n <= 10:
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        query_score = student_marks[query_name]
        print("%.2f" % (sum(query_score)/len(query_score)))
