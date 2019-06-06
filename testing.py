
# run - python3 set_up.py build_ext --inplace



# Importing test function 
# import example_cy
# example_cy.test(5)

#  will time how long the operations take, between cy and py. 
import timeit

cy = timeit.timeit('example_cy.test(500)', setup='import example_cy', number = 100)
py = timeit.timeit('example_py.test(500)', setup='import example_py', number = 100)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))
