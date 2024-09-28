#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task 1


# In[40]:


def calculate_sale(sales):
    total_sale = sum(sales)
    average_sale = total_sale / len(sales)
    print("Total Sales is:", total_sale)
    print("Average Sales is:", average_sale)
sales = [100, 200, 300, 400, 500, 600, 700]
calculate_sale(sales)


# In[38]:


#Task 2


# In[22]:


def calculate_discost(products, basket):
    total_cost = sum(products[i] * basket[i] for i in basket)
    total_discounted = total_cost * 0.9 
    print("The Discounted Total:", total_discounted)

products = {"apple": 10.0, "banana": 7, "orange": 0.5}
basket = {"apple": 2, "banana": 3}
calculate_discost(products, basket)


# In[ ]:


#Task 3


# In[23]:


class Product:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity


product = Product("apple", 1.0, 30)


# In[24]:


#Task 4


# In[25]:


class Product:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def total_cost(self, quantity):
        return self.cost * quantity

product = Product("apple", 1.0, 30)
print(product.total_cost(5))


# In[26]:


#Task 5


# In[46]:


def multiply_matrix(A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result


A = [[5, 6], [2, 8]]
B = [[3, 1], [9, 7]]
print(multiply_matrix(A, B))


# In[47]:


def determinant_2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]


matrix = [[5, 6], [2, 8]]
print("The Determinant of 2x2 Matrix:", determinant_2(matrix))


# In[48]:


def determinant_3(matrix):
    D = 0
    for i in range(3):
        D += (matrix[0][i] * (matrix[1][(i+1)%3] * matrix[2][(i+2)%3] - matrix[1][(i+2)%3] * matrix[2][(i+1)%3]))
    return D


matrix = [[2, 5, 1], [7, 4, 3], [1, 2, 8]]
print("The Determinant of 3x3 Matrix:", determinant_3(matrix))


# In[63]:


def inverse_3(matrix):
    D = determinant_3(matrix)
    if D == 0:
        return None
    else:
        inverse = [[0, 0, 0] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                v = [[matrix[x][y] for y in range(3) if y != col] for x in range(3) if x != row]
                inverse[row][col] = ((-1) ** (row + col)) * determinant_2(v)
        inverse = [[inverse[j][i] for j in range(3)] for i in range(3)]  
        inverse = [[inverse[i][j] / D for j in range(3)] for i in range(3)]
        return inverse

matrix = [[1, 2, 1], [1, 4, 3], [1, 2, 5]]
print("The Inverse of 3x3 Matrix:", inverse_3(matrix))


# In[50]:


#Task 6


# In[64]:


def solve_lequation(A, b):
    inverse_1 = inverse_3(A)
    if inverse_1 is None:
        return None
    return multiply_matrix(inverse_1, [[x] for x in b])

A = [[1, 2, 3], [2, 5, 3], [2, 0, 8]]
b = [10, 15, 20]
answer = solve_lequation(A, b)
print("The final answer of the Linear Equations:", answer)


# In[ ]:




