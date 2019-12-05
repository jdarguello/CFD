import settings;
import fontsize;

settings.outformat="pdf";
settings.render=16;
size(16cm, 0);

import graph;
//Río
real h = 4;
real l = 16;
draw(box((0,0), (l,h)));

//Obstáculo
real Ox = 2;
real Oy = 2;
pair O = (Ox,Oy);
real r = 0.5;
real rb = r/10;
fill(circle(O, r), rgb(181/255, 192/255, 202/255));
draw(circle(O, r));
fill(circle(O, rb));

//Dimensiones
real dim = 1;
draw((0,0) -- (-dim,0));
draw((0,h) -- (-dim,h));
draw((-3*dim/4,0) -- (-3*dim/4,h), arrow=Arrows, L = Label("$h$", position=MidPoint, align=W));

draw((0,0) -- (0,-dim));
draw((l,0) -- (l,-dim));
draw((0,-3*dim/4) -- (l,-3*dim/4), arrow=Arrows, L=Label("$l$", position=MidPoint, align=S));

real dim2 = dim/2;
draw(O -- (Ox, -dim2));
draw((0,-dim2/3) -- (Ox, -dim2/3), arrow=Arrows, L=Label("$O_x$", position=MidPoint, align=S));

draw(O -- (r + Ox + dim2, Oy));
draw((r + Ox + dim2/2, Oy) -- (r + Ox + dim2/2, 0), arrow=Arrows, L=Label("$O_y$", position=MidPoint, align=E));

draw((Ox, Oy-r) -- (Ox -r - dim2, Oy-r));
draw((Ox, Oy+r) -- (Ox -r - dim2, Oy+r));
draw((Ox - r - dim2/2, Oy-r) -- (Ox - r - dim2/2, Oy+r), arrow=Arrows, L=Label("$D$", position=MidPoint, align=W));








/*
//Tambor
real r = 1;
pair O = (0,0);    //Origen
draw(circle(O, r), rgb(43/255, 46/255, 145/255));

//Función de líneas discontinuas
void Disc(real xi, real xf, real yi, real yf, bool message=false, real num=20) {
   real suma_ant = 0;
   real suma, signox, signoy, size;
   if (xi != xf){
       signoy = 0;
       if (xi < xf) {
           size = (xf-xi)/num;
           signox = 1;
       } else {
           signox=-1;
           size = (xi-xf)/num;
       }
   } else {
       signox = 0;
       if (yi < yf) {
           signoy = 1;
           size = (yf-yi)/num;
       } else {
           signoy = -1;
           size = (yi-yf)/num;
       }
   }
   for (int i=0; i<=num; i=i+1) {
       if (signox != 0) {
           suma = suma_ant + signox*size;
           draw((xi+suma_ant,yi) -- (xi+suma, yi));
           suma_ant = suma + signox*size;
       } else {
           suma = suma_ant + signoy*size;
           draw((xi,yi+suma_ant) -- (xi, yi+suma));
           suma_ant = suma + signoy*size;
       }
   }
}

//Ejes coordenados
Disc(0,0,-r,-r/20);
Disc(-r,-r/20,0,0);

//Bola
real rb = 0.055;
pair Ob = (-2*r/3, 2*r/3);
fill(circle(Ob, rb), rgb(181/255, 192/255, 202/255));
fill(circle(Ob, rb/5));
draw(circle(Ob, rb));

//Movimiento rotacional
real rr = 1.1*r;
path p = (0,-rr) .. (-0.5*rr,-0.9*rr) .. (-rr,0);
draw(p, arrow=Arrow(), rgb(62/255, 66/255, 168/255));

//Diagrama de cuerpo libre
draw((0,0) -- (0,r));
draw((0,0) -- Ob);
draw(Ob -- (-2*r/3, r/4), arrow=Arrow);
label("$\vec{W}$", (-2*r/3, r/4), align=S);
draw(Ob -- (-r, r), arrow=Arrow);
label("$\vec{C}$", (-r, r), align=NE);
label("$B$", (-2*r/3 + 0.02, 2*r/3), align=E);
label("$\omega$", (-0.5*rr,-0.9*rr), align=SW);
path pp = (0,r/6) .. (-r/12,r/6) .. (-r/8,r/8);
draw(pp);
label("$\alpha$", (-r/12,r/6), align=N);

*/