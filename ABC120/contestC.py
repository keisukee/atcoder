# 問題文
# 机の上に 
# N
#  個のキューブが縦に積まれています。長さ 
# N
#  の文字列 
# S
#  が与えられます。

# 下から 
# i
#  番目のキューブの色は、
# S
#  の 
# i
#  文字目が 0 のとき赤色、1 のとき青色です。

# あなたは、赤色のキューブと青色のキューブが隣り合っているような部分を選んで、それら 
# 2
#  個のキューブを取り除く操作を何度でも行えます。

# このとき、取り除いたキューブの上にあったキューブは真下の物体の上に落下します。

# 最大で何個のキューブを取り除けるでしょうか。
string = input()
stack = []

for ele in string:
    num = int(ele)
    if not stack or stack[-1] == num:
        stack.append(num)
    else:
        stack.pop()

print(len(string) - len(stack))