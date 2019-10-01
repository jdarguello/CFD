settings.outformat="pdf";
unitsize(4cm);

//Ejes coordenados
int Nodos = 4;
draw((0,0) -- (0,Nodos), arrow = Arrow);
label("$T$", (0,Nodos), align=W);
draw((0,0) -- (Nodos,0), arrow = Arrow);
label("$x$", (Nodos,0), align=E);

//Valores
real[] pos = {0.5, 1.5, 3.5, 4};
int suma = 0;
for (int i=0; i <=Nodos-1; i=i+1) {
	dot((i,pos[i]), red);
	string num = (string) (i+1);
	label("$T_{" + num + "}$", (i,pos[i]), align=SE);
	if (i != 0) {
		label("$x_{" + num + "}$", (i,0), align=S);
	}
}

//Lines

for (int i=0; i < Nodos-1; i=i+1){
	draw((i,pos[i]) -- (i+1,pos[i+1]), red);
}