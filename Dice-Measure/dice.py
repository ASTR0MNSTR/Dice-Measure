import statistics as st
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression


def rounding(massive_in):
    massive_out = [round(item, 5) for item in massive_in]
    return massive_out


def dice_error_count(a, b, c, m):

    vars = [a, b, c, m]

    delta_side = 0.02
    delta_mass = 0.0001
    delta_mass_exp = 0.0004

    st_mean = [st.mean(item) for item in vars]
    st_dev = [st.stdev(item) for item in vars]
    st_dev_mean = [st.stdev(item)/(np.sqrt(len(item))) for item in vars]
    st_full_error = []

    for i in range(len(vars) - 1):
        st_full_error.append(
            np.sqrt(st_dev_mean[i]**2 + (0.3333*((delta_side)**2))))

    st_full_error.append(np.sqrt(st_dev_mean[3]**2 + 0.3333*(
        (delta_mass*st_mean[3])**2) + 0.3333*((delta_mass_exp)**2)))

    mean_density = []
    mean_density.append(
        ((1/(st_mean[0]*st_mean[1]*st_mean[2]))**2)*((st_full_error[3])**2))
    mean_density.append(
        ((st_mean[3]/(st_mean[0]*st_mean[0]*st_mean[1]*st_mean[2]))**2)*((st_full_error[0])**2))
    mean_density.append(
        ((st_mean[3]/(st_mean[0]*st_mean[1]*st_mean[1]*st_mean[2]))**2)*((st_full_error[1])**2))
    mean_density.append(
        ((st_mean[3]/(st_mean[0]*st_mean[1]*st_mean[2]*st_mean[2]))**2)*((st_full_error[2])**2))

    error_density = np.sqrt(sum(mean_density))
    

    density = st_mean[3]/(st_mean[0]*st_mean[1]*st_mean[2])
    table_density = 0.001180

    student_function = (round(density, 6) - table_density)/error_density


    print('Average of variables: ', rounding(st_mean))
    print('SEM: ', st_dev_mean)
    print('Full error: ', st_full_error)
    print('Density, %e' % (st_mean[3]/(st_mean[0]*st_mean[1]
          * st_mean[2])))
    print ('Error of density', error_density)
    print('t-distribution', student_function)


if __name__ == '__main__':
    a = [25.12, 25.00, 25.50]  # mm
    b = [24.44, 24.42, 24.60]  # mm
    c = [15.68, 15.70, 15.80]  # mm
    m = [11.4390, 11.4396, 11.4397]  # g
    dice_error_count(a, b, c, m)
