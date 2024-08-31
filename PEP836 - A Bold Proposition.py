def first_letters(words):
    fl = ""
    for i in range(len(words)):
        if (words[i] == " " and words[i + 1] != "\n") or words[i] == "\n":
            fl += words[i + 1]
        if words[i] == "<":
            return fl

problem_html = """""<p>Let $A$ be an <b>affine plane</b> over a <b>radically integral local field</b> $F$ with residual 
characteristic $p$.</p><p>We consider an <b>open oriented line section</b> $U$ of $A$ with normalized Haar measure $m$.
</p> <p>Define $f(m, p)$ as the maximal possible discriminant of the <b>jacobian</b> associated to the <b>orthogonal 
kernel embedding</b> of $U$ <span style="white-space:nowrap;">into $A$.</span></p>" \"<p>Find $f(20230401, 57)$. Give as
your answer the concatenation of the first letters of each bolded word.</p>"""""

concatenation = ""
for i in range(2,len(problem_html)):
    if problem_html[i - 2:i + 1] == "<b>":
        concatenation += first_letters(" " + problem_html[i + 1:])

print(concatenation)

#answer = aprilfoolsjoke
#כמובן שכשפתרתי את השאלה לא כתבתי קוד בשבילה...