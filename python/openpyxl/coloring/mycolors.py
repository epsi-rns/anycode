from openpyxl.styles import Color, PatternFill, Font, Border

blueScale = {
  0: 'FFE3F2FD',
  1: 'FFBBDEFB',
  2: 'FF90CAF9',
  3: 'FF64B5F6',
  4: 'FF42A5F5',
  5: 'FF2196F3',
  6: 'FF1E88E5',
  7: 'FF1976D2',
  8: 'FF1565C0',
  9: 'FF0D47A1'
}

limeScale = {
  0: 'FFF9FBE7',
  1: 'FFF0F4C3',
  2: 'FFE6EE9C',
  3: 'FFDCE775',
  4: 'FFD4E157',
  5: 'FFCDDC39',
  6: 'FFC0CA33',
  7: 'FFAFB42B',
  8: 'FF9E9D24',
  9: 'FF827717',
}

greenScale = {
  0: 'FFE8F5E9',
  1: 'FFC8E6C9',
  2: 'FFA5D6A7',
  3: 'FF81C784',
  4: 'FF66BB6A',
  5: 'FF4CAF50',
  6: 'FF43A047',
  7: 'FF388E3C',
  8: 'FF2E7D32',
  9: 'FF1B5E20',
}

blueScaleFill  = {}
limeScaleFill  = {}
greenScaleFill = {}

for key, value in blueScale.items():
  blueScaleFill[key] = PatternFill(
    start_color=value,
    end_color=value,
    fill_type='solid')

for key, value in limeScale.items():
  limeScaleFill[key] = PatternFill(
    start_color=value,
    end_color=value,
    fill_type='solid')

for key, value in greenScale.items():
  greenScaleFill[key] = PatternFill(
    start_color=value,
    end_color=value,
    fill_type='solid')
