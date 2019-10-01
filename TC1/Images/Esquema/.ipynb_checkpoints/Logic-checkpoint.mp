%---Output format---
outputformat := "png";
outputtemplate := "%j-%c.%o";
hppp := 0.125;
vppp := 0.125;

%---Document size---
Gx = 215.9mm;
Gy = 279.4mm;

beginfig(1);

%MathModel Box
h = 2.5cm; ancho = 4cm;
pair bb[];
bb0 = (0,-h/2); bb1 = (ancho,ypart bb0);
bb2 = (xpart bb1, ypart bb1 + h); bb3 = (xpart bb0, ypart bb2);
fill
	for i=0  upto 3:
		bb[i] --
	endfor
cycle withcolor (129,153,247)/255;

%MathModel Label
bb4 = (xpart bb1 - ancho/2, 0.25cm); bb5 = (xpart bb4, ypart bb4 - 0.5cm);
label("Modelo Matematico", bb4) withcolor white;
label("(Prob. Valor de frontera)", bb5) withcolor white;

%Math arrow
pair out[];
out0 = (xpart bb1, 0); out1 = (xpart out0 + 2.5cm, ypart out0);
drawarrow out0--out1 withcolor (129,153,247)/255;

%Algebra Box
hh = 2.5cm; anchoh = 4cm;
pair bbb[];
bbb0 = (xpart out1,-hh/2); bbb1 = (xpart bbb0 + anchoh,ypart bbb0);
bbb2 = (xpart bbb1, ypart bbb1 + hh); bbb3 = (xpart bbb0, ypart bbb2);
fill
	for i=0  upto 3:
		bbb[i] --
	endfor
cycle withcolor (81,207,246)/255;

%Algebra Label
bbb4 = (xpart bbb1 - anchoh/2, 0.25cm); bbb5 = (xpart bbb4, ypart bbb4 - 0.5cm);
label("Sistema nodal de", bbb4) withcolor white;
label("Ecuaciones algebraicas", bbb5) withcolor white;

%Algebra arrow
out2 = (xpart bbb1, 0); out3 = (xpart out2 + 2.5cm, ypart out2);
drawarrow out2--out3 withcolor (81,207,246)/255;

%Nodal Box
%hh = 2.5cm; anchoh = 4cm;
pair bbbb[];
bbbb0 = (xpart out3,-hh/2); bbbb1 = (xpart bbbb0 + anchoh,ypart bbbb0);
bbbb2 = (xpart bbbb1, ypart bbbb1 + hh); bbbb3 = (xpart bbbb0, ypart bbbb2);
fill
	for i=0  upto 3:
		bbbb[i] --
	endfor
cycle withcolor (182,171,250)/255;

%Nodal Label
bbbb4 = (xpart bbbb1 - anchoh/2, 0.25cm); bbbb5 = (xpart bbbb4, ypart bbb4 - 0.5cm);
label("Temperaturas", bbbb4) withcolor white;
label("Nodales", bbbb5) withcolor white;

endfig;