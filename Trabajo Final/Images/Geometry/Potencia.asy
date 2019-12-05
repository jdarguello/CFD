import settings;
import fontsize;

settings.outformat="pdf";
settings.render=16;
size(14cm, 0);

import graph;
//Tambor
real r = 1;

//Centro de masa
real const = 0.705;
fill((-const*r,-const*r) -- (const*r, const*r) -- arc((0,0), r, 45, 225) -- cycle, rgb(194/255, 194/255, 225/255));
draw((-const*r,-const*r) -- (const*r, const*r),rgb(130/255, 53/255, 158/255));
pair O = (0,0);    //Origen
draw(circle(O, r), rgb(130/255, 53/255, 158/255));

//Función de líneas discontinuas
void Disc(real xi, real xf, real yi, real yf, bool message=false, real num=10) {
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
Disc(0,0,0,-0.55*r);
Disc(0,0.55*r,0,0);


//Movimiento rotacional
real rr = 1.1*r;
path p = (-rr,0) .. (-0.5*rr,-0.9*rr) .. (0,-rr);
draw(p, arrow=Arrow(), rgb(130/255, 53/255, 158/255));

//Diagrama de cuerpo libre
draw((0,0) -- (0.86*r,-0.86*r));
pair Oc = (0.3525*r,-0.3525*r);    //Origen
fill(circle(Oc, r/60));
draw(Oc -- (0.3525*r, -3*r/5), arrow=Arrow);
label("$\vec{W}$", (0.3525*r, -3*r/5), align=S);

label("$\omega$", (-0.5*rr,-0.9*rr), align=SW);
real final = 0.2;
path pp = (0,-0.3*r) .. (0.1*r,-0.3*r) .. (final*r,-final*r);
draw(pp, L=Label("$\theta$", position=MidPoint, align=S));

draw(Oc -- (0.5*r, -0.2*r));
draw((0.45*r,-0.25*r)--(0.1*r,0.1*r), arrow=Arrows, L=Label("$d$", position=MidPoint));