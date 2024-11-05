\* Source Pyomo model name=linear_programming *\

min 
obj:
+0.59 x
+0.17 y
+1.53 z
+0.17 w

s.t.

c_l_c1_:
+407 x
+79 y
+241 z
+50 w
>= 2618

c_l_c2_:
+72 x
+15 y
+13 w
>= 155

c_l_c3_:
+10 x
+2 y
+15 z
>= 63

c_l_c4_:
+2 x
+1 y
+21 z
>= 18

bounds
   0 <= x <= +inf
   0 <= y <= +inf
   0 <= z <= +inf
   0 <= w <= +inf
end
