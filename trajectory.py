import math
import function as f
import alphafind


def get_trajectory(x_0, y_0, n, flag):
    counter = 1
    vector_x = [x_0]
    vector_y = [y_0]
    if flag == 0:
        alpha = 0.001
    while counter <= n:
        v_x = f.f(vector_x[counter - 1], vector_y[counter - 1])[0]
        v_y = f.f(vector_x[counter - 1], vector_y[counter - 1])[1]
        normalized_vector_of_speed_x = v_x / math.sqrt(v_x ** 2 + v_y ** 2)
        normalized_vector_of_speed_y = v_y / math.sqrt(v_x ** 2 + v_y ** 2)
        if flag == 1:
            alpha = abs(alphafind.alpha_1(counter))
        elif flag == 2:
            alpha = abs(alphafind.alpha_2(counter+1, n))
        vector_x.append(vector_x[counter - 1] + alpha * normalized_vector_of_speed_x)
        vector_y.append(vector_y[counter - 1] + alpha * normalized_vector_of_speed_y)
        counter += 1
    return vector_x, vector_y

