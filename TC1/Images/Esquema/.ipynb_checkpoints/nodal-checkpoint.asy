settings.outformat="pdf";
unitsize(4cm);

//Tamaño del rectángulo
int a = 2;
int h = 1;

//General
draw((0,h/2) -- (a,h/2), red);
draw((a,h/2) -- (a+1,h/2), green, arrow=Arrow);

//Puntos y labels
real suma = 0;
int ref = 1;
int div = 4;
for (int i=div; i>= 1; i=i-1) {
	string num = (string) ref;
	dot((suma, h/2), red);
	if (i == div){
		label(num, (suma, h/2), align=NW);
	}	else if (i == 1) {
		label(num, (suma, h/2), align=NE);
	} else {label(num, (suma, h/2), align=N);}
	suma = suma + a/(div-1);
	ref = ref + 1;
}
label("$x$", (a+1,h/2), align=E);

//Arcos
int Nodos = 4;
int Elementos = Nodos-1;
real dif = 0.06;
suma = a/6;
for (int i=0; i< Elementos; i = i+1){
	draw(arc((suma - dif,h/2 -0.2), r=(a/Elementos)/2, angle1=90, angle2=45+90), blue, arrow=Arrow);
	draw(arc((suma + dif,h/2 -0.2), r=(a/Elementos)/2, angle1=90, angle2=45), blue, arrow=Arrow);
	draw((suma,h/2-0.08) -- (suma, h/2 + (a/Elementos)/2 - 0.2));
	suma = suma + a/3;
}