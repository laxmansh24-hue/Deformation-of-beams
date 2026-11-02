def ss_centre(P,L,x,E,I):
    if 0<=x<L/2:
        return P*x*(3*L**2-4*x**2)/(48*E*I)
    else:
        return P*(L-x)*(3*L**2-4*(L-x)**2)/(48*E*I)


def ss_point(P,L,a,x,E,I):
    if 0<=x<=a:
        return P*(L-a)*x*(L**2-(L-a)**2-x**2)/(6*L*E*I)
    else:
        return P*a*(L-x)*(L**2-a**2-(L-x)**2)/(6*L*E*I)
    
    
def ss_UDL(P,L,x,E,I):
    return P*x*(L**3-2*L*x**2+x**3)/(24*E*I)

    
def cl_point(P,L,a,x,E,I):
    if 0<=x<=a:
        return P*x**2*(3*a-x)/(6*E*I)
    else:
        return P*a**2*(3*x-a)/(6*E*I)


def cl_UDL(P,L,x,E,I):
    return P*x**2*(6*L**2-4*L*x+x**2)/(24*E*I)


# def ss(P,L,E,I):
#     return P*L**3/(48*E*I)
# def cl(P,L,E,I):
#     return P*L**3/(3*E*I)

