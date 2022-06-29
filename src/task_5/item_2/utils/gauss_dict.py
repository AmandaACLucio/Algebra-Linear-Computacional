﻿dict_gauss_quadrature = {
  2: {
    'weights': [1.0, 1.0],
    'zpoints': [-0.577350269189626, 0.577350269189626]

  },
  3: {
    'weights': [0.555555555555556, 0.888888888888889, 0.555555555555556],
    'zpoints': [-0.774596669241483, 0.0, 0.774596669241483]
  },
  4: {
    'weights': [0.347854845137454, 0.652145154862546, 0.652145154862546, 0.347854845137454],
    'zpoints': [-0.861136311594053, -0.339981043584856, 0.339981043584856, 0.861136311594053]
  },
  5: {
    'weights': [0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189],
    'zpoints': [-0.906179845938664, -0.538469310105683, 0.0, 0.538469310105683, 0.906179845938664]
  },
  6: {
    'weights': [0.171324492379170, 0.360761573048139, 0.467913934572691, 0.467913934572691, 0.360761573048139, 0.171324492379170],
    'zpoints': [-0.932469514203152, -0.661209386466265, -0.238619186083197, 0.238619186083197, 0.661209386466265, 0.932469514203152]
  },
  7: {
    'weights': [0.129484966168870, 0.279705391489277, 0.381830050505118, 0.417959183673469, 0.381830050505118, 0.279705391489277, 0.129484966168870],
    'zpoints': [-0.949107912342759, -0.741531185599394, -0.405845151377397, 0.0, 0.405845151377397, 0.741531185599394, 0.949107912342759]
  },
  8: {
    'weights': [0.101228536290376, 0.222381034453374, 0.313706645877887, 0.362683783378362, 0.362683783378362, 0.313706645877887, 0.222381034453374, 0.101228536290376],
    'zpoints': [-0.960289856570432, -0.796666477413627, -0.525532409916329, -0.183434642495650, 0.183434642495650, 0.525532409916329, 0.796666477413627, 0.960289856570432]
  },
  9: {
    'weights': [0.081274388361574, 0.180648160694857, 0.260610696402935, 0.312347077040003, 0.330239355001260, 0.312347077040003, 0.260610696402935, 0.180648160694857, 0.081274388361574],
    'zpoints': [-0.968160239507626, -0.836031107326636, -0.613371432700590, -0.324253423403809, 0.0, 0.324253423403809, 0.613371432700590, 0.836031107326636, 0.968160239507626]

  },
  10: {
    'weights': [0.066671344308688, 0.149451349150581, 0.219086362515982, 0.269266719309996, 0.295524224714753, 0.295524224714753, 0.269266719309996, 0.219086362515982, 0.149451349150581, 0.066671344308688],
    'zpoints': [-0.973906528517172, -0.865063366688985, -0.679409568299024, -0.433395394129247, -0.148874338981631, 0.148874338981631, 0.433395394129247, 0.679409568299024, 0.865063366688985, 0.973906528517172]
  }
}

def select_quadrature(count_points_integration):
  return dict_gauss_quadrature[count_points_integration]