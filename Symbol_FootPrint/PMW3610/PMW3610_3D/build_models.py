import cadquery as cq
from cadquery import exporters
from pathlib import Path
p=Path(__file__).parent
# Modeling coordinate frame: z=0 object/navigation surface; lens reference plane z=2.40;
# sensor pin reference plane z=8.35. Mechanical approximation, not production CAD.
A=2.40; B=8.35
# Lens plan envelope 12.90 x 8.25, schematic body height 2.12 per section view.
# 5.95 on page 1 is a horizontal profile dimension, NOT a confirmed lens height.
lens=cq.Workplane('XY').box(12.90,8.25,2.12,centered=(True,True,False)).translate((0,0,A))
# Open top pocket is schematic, not an exact manufacturer's optical profile
lens=lens.cut(cq.Workplane('XY').box(10.2,6.0,1.1,centered=(True,True,False)).translate((0,0,A+1.25)))
# two schematic imaging/illumination channels, not optically validated
for x,r in [(-2.15,1.60),(2.2,1.05)]:
 lens=lens.cut(cq.Workplane('XY').center(x,0).circle(r).extrude(2.6).translate((0,0,A)))
# locating protrusions diagrammatic only
for x in [-5.15,5.15]:
 for y in [-3.25,3.25]:
  lens=lens.union(cq.Workplane('XY').center(x,y).circle(.38).extrude(.65).translate((0,0,A+2.12)))
lens=lens.val()
# sensor envelope: 16.20 x 10.10; section max 4.05. PIN layout approximate, visual aid only
sensor=cq.Workplane('XY').box(16.2,10.1,3.85,centered=(True,True,False)).translate((0,0,B+.20))
# lower optic protrusion only to depict physical feature
sensor=sensor.union(cq.Workplane('XY').center(-1.7,0).circle(1.75).extrude(.55).translate((0,0,B-.35)))
# 8 contacts per side, x pitch 1.78, approx outer row offset; pin shape simplified
for x in [(-6.23+i*1.78) for i in range(8)]:
 for y in [-5.42,5.42]:
  pin=cq.Workplane('XY').box(.50,1.1,.45,centered=(True,True,False)).translate((x,y,B-.15))
  sensor=sensor.union(pin)
sensor=sensor.val()
exporters.export(sensor,str(p/'PMW3610DM-SUDU.step'))
exporters.export(lens,str(p/'LM18-LSI.step'))
assy=cq.Assembly(name='PMW3610_LM18_Approximate_Assembly')
assy.add(sensor,name='PMW3610_sensor_simplified',color=cq.Color(.25,.25,.27))
assy.add(lens,name='LM18_LSI_lens_simplified',color=cq.Color(.48,.75,.65))
assy.save(str(p/'PMW3610_Assembly.step'),exportType='STEP')
print([(v.name,round(v.stat().st_size/1024)) for v in p.glob('*.step')])
