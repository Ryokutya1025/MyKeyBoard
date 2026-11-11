OrbitSplit PMW3610DM-SUDU + LM18-LSI
====================================
MECHANICAL CONCEPT MODELS ONLY. NOT OFFICIAL PIXART CAD. NOT VALIDATED FOR PRODUCTION.

Files:
- PMW3610DM-SUDU.step : simplified sensor package and illustrative pins.
- LM18-LSI.step        : simplified lens envelope and illustrative apertures and locating posts.
- PMW3610_Assembly.step : nominal reference-plane concept assembly.

Source: User-supplied PMW3610DM-SUDU datasheet, p.3-4,6;
        User-supplied LM18-LSI datasheet, p.1-3.

Known dimensions:
- Sensor body plan: 16.20 x 10.10 mm (datasheet outline). 4.05 mm section dimension.
- Sensor pins: 16, pitch 1.78 mm; pin shapes depicted approximately.
- Lens overall plan: 12.90 x 8.25 mm; profile/cross-section dimensions include 2.12 mm.
- Object to lens reference plane A: 2.20 to 2.60 mm, typ 2.40 mm.
- Object to sensor pin reference plane B: typ 8.35 mm.

Model conventions:
- z=0 represents FLAT navigation/object reference plane, not a modeled 19mm ball.
- lens bottom nominally z=2.40; sensor pin reference plane nominally z=8.35.
- Optical surface geometry, sensor optical-center positioning, lens retention features,
  post dimensions, pins, contact plane, exact body sections and relative assembly details
  are SCHEMATIC and MUST be confirmed against actual hardware / manufacturer CAD.
- Lens geometry is intentionally simplified. The page-1 '5.95' dimension is NOT
  interpreted as lens height.
- Use the manufacturer's baseplate STEP/IGES (available on request) for accurate
  mounting/retention features.

Before KiCad mechanical decisions: align coordinate frame to actual footprint;
confirm STEP rotation/offset, PCB thickness and the optical center/ball clearance
against real parts. Do not manufacture an optical mechanism based only on these files.
