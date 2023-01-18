/*
Program to calculate distances between 3D points.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "piste3d.h"

double power(double i)
{
    i = i * i;

    return i;
}

//Calulcates the distance
double etaisyys(Piste3D a, Piste3D b)
{
    double q = 0;
    double w = 0;
    double e = 0;
    double answer = 0;

    q = a.x - b.x;
    w = a.y - b.y;
    e = a.z - b.z;

    q = power(q);
    w = power(w);
    e = power(e);

    answer = q + w + e;

    answer = sqrt(answer);

    return answer;

}

void tulosta(Piste3D p, int tarkkuus)
{

    printf("(%.*f, ", tarkkuus, p.x);
    printf("%.*f, ", tarkkuus, p.y);
    printf("%.*f)", tarkkuus, p.z);
}
