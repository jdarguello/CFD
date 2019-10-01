%---Output format---
%outputformat := "png";
%outputtemplate := "%j-%c.%o";
%hppp := 0.125;
%vppp := 0.125;

%---Document size---
Gx = 215.9mm;
Gy = 279.4mm;


%---Black Box---
beginfig(1);

%Label - entrada
pair O[];
O0 =  (0,0.3cm); O1 = (0, 0);
label("Entradas del", O0);
label("usuario",O1);

%label - arrow
O2 = (1cm,0); O3 = (xpart O2 + 2.5cm, ypart O2);
drawarrow O2--O3;

%label - pre
O4 = (xpart O2 + 1.2cm, 0.2cm);
label("Preprocessing", O4);

%Black Box
h = 2cm; ancho = 3cm;
pair bb[];
bb0 = (xpart O3, h/2); bb1 = (xpart bb0 + ancho, ypart bb0);
bb2 = (xpart  bb1, ypart bb1 - h); bb3 = (xpart bb0, ypart bb2);
fill
	for i=0  upto 3:
		bb[i] --
	endfor
cycle withcolor (129,153,247)/255;

%Blac Box - Label
bb4 = (xpart bb1 - ancho/2, 0);
label("Black Box", bb4) withcolor white;

%Output arrow
pair out[];
out0 = (xpart bb1, 0); out1 = (xpart out0 + 2.5cm, ypart out0);
drawarrow out0--out1;

%Postprocessing - label
out2 = (xpart out0 + 1.2cm, 0.2cm);
label("Postprocessing", out2);

%Label - brace
out3 = (xpart out1, ypart out1 - h/2); out4 = (xpart out3, ypart out3 + h);
label.rt((btex $\lbrace$ etex) xscaled 1.3yscaled 5, 1/2[out3,out4]);

%outs - labels
out5 = (xpart out3 + 1.1cm, h/2 - 0.2cm); out6 = (xpart out5, 0);
out7 = (xpart out5 + 0.3cm, -h/2 + 0.2cm);
label("- Figuras", out5);
label("- Tablas", out6);
label("- Error Info", out7);


endfig;

%---Grey Box---
beginfig(2);

%Preprocessing - label
pair O[];
O0 =  (0,0);
label("Preprocessing", O0);

%label - arrow
O2 = (1.1cm,0); O3 = (xpart O2 + 1cm, ypart O2);
drawarrow O2--O3;

%Black Box
hh = 3cm; an = 7.4cm;
pair bb[];
bb0 = (xpart O3, hh/2); bb1 = (xpart bb0 + an, ypart bb0);
bb2 = (xpart  bb1, ypart bb1 - hh); bb3 = (xpart bb0, ypart bb2);
draw
	for i=0  upto 3:
		bb[i] --
	endfor
cycle withcolor (129,153,247)/255;

%MathModel Box
hM = 1.2cm; anM = 2.5cm;
pair MM[];
MM0 = (xpart O3 + 0.2cm, hM/2); MM1 = (xpart MM0 + anM, ypart MM0);
MM2 = (xpart  MM1, ypart MM1 - hM); MM3 = (xpart MM0, ypart MM2);
draw
	for i=0  upto 3:
		MM[i] --
	endfor
cycle dashed evenly withcolor (168,0,255)/255;

%MathModel label
MM4 = (xpart MM0 + 1cm + 0.2cm, ypart O2 + 0.15cm); MM5 = (xpart MM4 + 0.1cm, ypart O2 - 0.15cm);
label("Modelo", MM4) withcolor (168,0,255)/255;
label("Matematico", MM5) withcolor (168,0,255)/255;

%Sim Num - Arrow
pair SM[];
SM0 = (xpart MM1, 0); SM1 = (xpart SM0 + 2cm, ypart SM0);
drawarrow SM0--SM1 dashed evenly withcolor (168,0,255)/255;

%Sim Num - label
SM2 = (xpart SM0 + 0.9cm, ypart SM0 + 0.2cm);
SM3 = (xpart SM2, ypart SM0 - 0.2cm);
label("Solucion", SM2);
label("Numerica", SM3);

%Variables
hV = hh - 0.5cm; anV = 2.5cm;
pair VP[];
VP0 = (xpart SM1, hV/2); VP1 = (xpart VP0 + anV, ypart VP0);
VP2 = (xpart  VP1, ypart VP1 - hV); VP3 = (xpart VP0, ypart VP2);
draw
	for i=0  upto 3:
		VP[i] --
	endfor
cycle dashed evenly withcolor (255, 150, 0)/255;

%Variables - label
VP4 = (xpart VP0 + 1.3cm, ypart VP0 - 0.7cm);
VP5 = (xpart VP4, ypart VP4 - 0.3cm);
VP6 = (xpart VP5, ypart VP5 - 0.3cm);
VP7 = (xpart VP6, ypart VP6 - 0.3cm);
label("Variables", VP4) withcolor (255, 150, 0)/255;
label("seleccionadas", VP5) withcolor (255, 150, 0)/255;
label("en puntos", VP6) withcolor (255, 150, 0)/255;
label("especificos", VP7) withcolor (255, 150, 0)/255;

%Output
pair out[];
out0 = (xpart VP1, 0); out1 = (xpart out0 + 0.2cm, ypart out0);
draw out0--out1 dashed evenly;
out2 = (xpart out1, ypart out1); out3 = (xpart out2 + 1cm, ypart out2);
drawarrow out2--out3;

%Output - label
out4 = (xpart out3 + 1.2cm, ypart out3);
label("Postprocessing", out4);

%Física
pair F[];
F0 = (xpart O3 + 0.2cm, -3cm); F1 = (xpart F0 + anM, ypart F0);
F2 = (xpart  F1, ypart F1 - hM); F3 = (xpart F0, ypart F2);
draw
	for i=0  upto 3:
		F[i] --
	endfor
cycle withcolor (255,0,134)/255;

%Física label - principal
F4 = (xpart F0 + 1cm + 0.2cm, ypart F0 - hM/2 + 0.15cm); F5 = (xpart F4 + 0.1cm, ypart F0 - hM/2 - 0.15cm);
label("Problema", F4) withcolor (255,0,134)/255;
label("Fisico", F5) withcolor (255,0,134)/255;

%Física a Sim Num - Arrow
F6 = (xpart F0 + anM/2, ypart F0); F7 = (xpart F6, ypart bb2);
draw F6--F7 withcolor (255,0,134)/255;
F8 = (xpart F7, ypart MM2);
drawarrow F7--F8 dashed evenly withcolor (255,0,134)/255;

%Física label - sec
F9 = (xpart F7 + 1.4cm, ypart F7 - 0.5cm); 
F10 = (xpart F9, ypart F9 - 0.5cm);
label("Principios fisicos", F9);
label("Suposiciones", F10);

%Física flechas - sec
F11 = (xpart F1, ypart F1 - hM/4); F12 = (xpart F11 + 0.5cm, ypart F11);
drawarrow F11--F12 withcolor (255,0,134)/255;
F13 = (xpart F1, ypart F1 - 3*hM/4); F14 = (xpart F11 + 0.5cm, ypart F13);
drawarrow F13--F14 withcolor (255,0,134)/255;

%Física label - secc
F15 = (xpart F12 + 1.5cm, ypart F12);
F16 = (xpart F14 + 1.75cm, ypart F14);
label("Calculos Manuales", F15);
label("Datos Experimentales", F16);

endfig;