
def select_polynomial_quadrature(point_a, point_b, count_points_integration):
    L = point_b - point_a
    delta = L/(count_points_integration-1)
    dict_weights = {
        2: [L/2, L/2],
        3: [L/6, (2*L)/3, L/6],
        4: [L/8, (3*L)/8, (3*L)/8, L/8],
        5: [(7*L)/90, (16*L)/45, (2*L)/15, (16*L)/45, (7*L)/90],
        6: [(19*L)/288, (75*L)/288, (50*L)/288, (50*L)/288, (75*L)/288, (19*L)/288],
        7: [(41*L)/(140*6), (216*L)/(140*6), (27*L)/(140*6), (272*L)/(140*6), (27*L)/(140*6), (216*L)/(140*6), (41*L)/(140*6)],
        8: [(751*L)/(17280), (3577*L)/(17280), (1323*L)/(17280), (2989*L)/(17280), (2989*L)/(17280), (1323*L)/(17280), (3577*L)/(17280), (751*L)/(17280)],
        9: [(989*L)/(28350), (5888*L)/(28350), (-928*L)/(28350), (10496*L)/(28350), (-4540*L)/(28350), (10496*L)/(28350), (-928*L)/(28350), (5888*L)/(28350), (989*L)/(28350)],
        10:[(2857*L)/(89600),(15741*L)/(89600),(1080*L)/(89600),(19344*L)/(89600),(5778*L)/(89600),(5778*L)/(89600),(19344*L)/(89600),(1080*L)/(89600),(15741*L)/(89600),(2857*L)/(89600)]
    }
    dict_points = {
        2: [point_a,point_b],
        3: [point_a, (point_a+point_b)/2, point_b],
        4: [point_a, point_a + delta, point_a + (2*delta), point_b],
        5: [point_a, point_a + delta, point_a + (2*delta), point_a + (3*delta), point_b],
        6: [point_a, point_a + delta, point_a + (2*delta), point_a + (3*delta), point_a + (4*delta), point_b],
        7: [point_a, point_a + delta, point_a + (2*delta), point_a + (3*delta), point_a + (4*delta), point_a + (5*delta), point_b],
        8: [point_a, point_a + delta, point_a + (2*delta), point_a + (3*delta), point_a + (4*delta), point_a + (5*delta), point_a + (6*delta), point_b],
        9: [point_a, point_a + delta, point_a + (2*delta), point_a + (3*delta), point_a + (4*delta), point_a + (5*delta), point_a + (6*delta), point_a + (7*delta), point_b],
        10: [point_a, point_a + delta,point_a + (2*delta),point_a + (3*delta),point_a + (4*delta),point_a + (5*delta),point_a + (6*delta),point_a + (7*delta),point_a + (8*delta), point_b],
    }
    return dict_weights, dict_points