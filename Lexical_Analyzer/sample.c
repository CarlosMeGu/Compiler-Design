int gcd (int u, int v)
{   if (v == 0) return u ;
    else return gcd(v, u-u/v*v)
    /* u-u/v*v == u mod v */
}

void main(void)
{   int x; int y;
    4x = input(); y = input();
    output(gcd(x,y));
}