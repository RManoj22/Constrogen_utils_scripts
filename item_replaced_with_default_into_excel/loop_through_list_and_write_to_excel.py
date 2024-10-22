import pandas as pd

output_file = r'D:\IGS\PB Data Utils Scripts\item_replaced_with_default_into_excel\output\output_file.xlsx'

item_list = ['Surya Cem ', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Motor reapair', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'LED Tube Light [24 W] [Philips]', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Teak Wood [Second Quality ]', 'Teak Wood [Second Quality ]', 'Nanganallur Talk', 'Nanganallur Talk', 'GI Pipe 5 feet', 'Nanganallur Talk', 'LED Fittings [20 W]', 'Wire 1 sq.mm (90 mtr)', 'Nanganallur Talk', 'Nanganallur Talk', 'Bath Room Area Water Proofing', 'Over Head Tank', 'Bolt Nut Washer (1")', 'FTA [PVC] (1" )', 'Nanganallur Talk', 'Isolator 4 pole (63 A)', 'GI Pipe 5 feet', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', 'Nanganallur Talk', '8558 Ultima', '8751 Ultima ', '0419 Ultima ', '8231 Ultima ', 'TRAVALLING EXPENSE', 'Telephone Jack (Rj 11)', 'Gate and Fixed Grill', '8558 Ultima', '8231 Ultima ', '0419 Ultima ', '8571 ULTIMA',
             'Ring (7"X7") &(7"X3")', 'Metal plate 4 model(Remo)', 'Pipe [holder] (6")', '8571 ULTIMA', 'Saddle  [PVC] (4 X 1/2 )', 'FTA  [PVC] (1/2")', 'FTA [PVC] (1" x 1/2")[Bross]', 'Hose ( 1/2 " )', 'Steps Granite [Brown Labota]', 'Bolt Nut Washer (2")', '0470 - Tractor Emelson ', '0615 - Tractor Emelson ', '8417 - Tracter Emulsion', 'Grill', 'Hall Bedroom Floor [NEO MILTON BIANCO]  (2T)', 'Kitchen Wall Tile [Marcos Gris] ', 'Beta', 'Clamp (Bore) (1  " X 1/2 ")', 'Star Drillbit', 'PVC Door Plywood', 'Bib Cock Jade Long Body (G0206A1)', 'Crust Bath Spout With Diverter [G3128A1] (PARRY)', '8571 ULTIMA', '0419 Ultima ', '8558 Ultima', '8231 Ultima ', 'Multi-Flow hand Shower 100mm (T9983A1)', 'Focus Light (20w) LED ', 'Surya Cem (50 Kg)', 'Wash Basin [Kolar] Wall Hung (18x13) (C042E1C)', 'Hinges (EPCO Heal)', 'Pipe Gate', 'Koches Screw', 'Balcony And Angle', 'FTA [PVC] (1" )', 'Reeper (1.5 x1)', 'Reeper 3 X 1 (7 feet)', '0643 Enamel', 'Pipe (5" X 5 " )', 'POP', 'Automatic Motor System Fixing', 'Ceramic Board', 'Bolt Nut ( 1 3/4" X 1/4 ") ', 'Bedroom Door [HDHMR] [6 3/4 x 2 1/4]', 'Reeper 3 X 1 (7 feet)', 'laminated door(6.75 x 2.75)']

df = pd.DataFrame(item_list, columns=['Item Name'])


df.to_excel(output_file)

print('Successfully created the output file')
