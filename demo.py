# this program has 2 faults
# 1 . check of equations to be solvable
# 2 . Coefficients problem

import streamlit as st
import math

def gauss_seidel(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3):
    x = 0
    y = 0
    z = 0
    prev_x, prev_y, prev_z = x, y, z
    run = True
    while run:
        x = (d1 - b1 * y - c1 * z) / a1
        y = (d2 - a2 * x - c2 * z) / b2
        z = (d3 - a3 * x - b3 * y) / c3

        run = not(
            math.isclose(prev_x, x, rel_tol=0.00001) or
            math.isclose(prev_y, y, rel_tol=0.00001) or
            math.isclose(prev_z, z, rel_tol=0.00001))
        prev_x, prev_y, prev_z = x, y, z

    return x, y, z


st.title("Gauss-Seidel Equation Solver")

# Input fields for coefficients
# st.sidebar.title("Coefficients")
# a1 = st.sidebar.number_input('a1', value=20)
# a2 = st.sidebar.number_input('a2', value=3)
# a3 = st.sidebar.number_input('a3', value=2)
# b1 = st.sidebar.number_input('b1', value=1)
# b2 = st.sidebar.number_input('b2', value=20)
# b3 = st.sidebar.number_input('b3', value=-3)
# c1 = st.sidebar.number_input('c1', value=-2)
# c2 = st.sidebar.number_input('c2', value=-1)
# c3 = st.sidebar.number_input('c3', value=20)
# d1 = st.sidebar.number_input('d1', value=17)
# d2 = st.sidebar.number_input('d2', value=-18)
# d3 = st.sidebar.number_input('d3', value=25)

def input_column(column_num):
    # st.write(f"Column {column_num}")
    a = []
    for i in range(3):
        a.append(st.number_input(f"Input {i+1}" , key=f"col{column_num}_input{i+1}"))
    return a

col1, col2, col3, col4 = st.columns(4)

with col1:
    inputs_col1 = input_column(1)

with col2:
    inputs_col2 = input_column(2)

with col3:
    inputs_col3 = input_column(3)

with col4:
    inputs_col4 = input_column(4)

all_inputs = [*inputs_col1, *inputs_col2, *inputs_col3, *inputs_col4]

# Compute button
if st.button("Compute"):
    x, y, z = gauss_seidel(*all_inputs)
    st.write(f"x = {round(x, 3)}, y = {round(y, 3)}, z = {round(z, 3)}")
