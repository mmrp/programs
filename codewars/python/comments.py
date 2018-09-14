def solution(string,markers):
    for s in string.split("\n"):
        print(s.split("#")) #"".join(markers))[0])
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) #, "apples, pears\ngrapes\nbananas")

