import re

s = "He1llo, abbby n_A_a A_D_R a_b a_s_0 asabababljk_n a_b a_bb"
pattern = r"[a-z]+_+[a-z].*"
ss = re.findall(pattern,s)
print(ss)