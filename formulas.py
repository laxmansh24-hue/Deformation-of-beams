# def ss_beam():
#     if 0<=x<=L/2:
#         return P*b*x*(L**2-b**2-x**2)/(6*L*E*I)
#     else:
#         return P*a*(L-x)*(L**2-a**2-(L-x)**2)/(6*L*E*I)
    
# def cl_beam():
#     if 0<=x<=a:
#         return P*x**2*(3*a-x)/(6*E*I)
#     else:
#         return P*a**2*(3*x-a)/(6*E*I)

def ss(P,L,E,I):
    return P*L**3/(48*E*I)
def cl(P,L,E,I):
    return P*L**3/(3*E*I)

