def test(x,y,z):
    k=0
    j=0
    if x>3 and z<10:
        k=x*y-1
        j=sqrt(k)
    if x==4 or y>5:
        j=x*y+10
        j=j%3
    return(j,k)