\* Source Pyomo model name=linear_programming *\

min 
obj:
+14 a
+14 b
+12 c
+10 d
+13 e
+8 f
+9 g
+11 h
+16 i

s.t.

c_u_c1_:
+1 a
+1 b
+1 c
<= 2

c_u_c2_:
+1 d
+1 e
+1 f
<= 2

c_u_c3_:
+1 g
+1 h
+1 i
<= 2

c_e_c4_:
+1 a
+1 d
+1 g
= 1

c_e_c5_:
+1 b
+1 e
+1 h
= 1

c_e_c6_:
+1 c
+1 f
+1 i
= 1

bounds
   0 <= a <= 1
   0 <= b <= 1
   0 <= c <= 1
   0 <= d <= 1
   0 <= e <= 1
   0 <= f <= 1
   0 <= g <= 1
   0 <= h <= 1
   0 <= i <= 1
binary
  a
  b
  c
  d
  e
  f
  g
  h
  i
end
