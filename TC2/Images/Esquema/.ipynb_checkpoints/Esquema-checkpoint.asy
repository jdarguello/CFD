settings.outformat="png";
unitsize(1cm);

//Tamaño del rectángulo
int a = 10*2;
int h = 6*2;

//radio del círculo
real r = 2;

//General
draw(box((0,0), (a,h)));
//draw((0,h/2) -- (a,h/2), red);
//draw((a,h/2) -- (a+1,h/2), green, arrow=Arrow);

//Ejes coordenados
real ex = 1;
draw((a/2,h/2) -- (a/2,h+ex), green, arrow=Arrow);
draw((a/2,h/2) -- (a+ex,h/2), blue, arrow=Arrow);
label("$x$", (a+ex,h/2), align=E);
label("$y$", (a/2,h+ex), align=N);

//Círculo
draw(circle((a/2,h/2), r));