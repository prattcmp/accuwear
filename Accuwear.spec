# -*- mode: python -*-

block_cipher = None


a = Analysis(['Accuwear.py'],
             pathex=['/Users/Chris/Documents/OneDrive/HackPSU'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('images/accuweather.png', '/Users/Chris/Documents/OneDrive/HackPSU/images/accuweather.png',  'DATA'),
			('images/Sweatshirt.gif','/Users/Chris/Documents/OneDrive/HackPSU/images/Sweatshirt.gif','DATA'),
			('images/parka.jpg','/Users/Chris/Documents/OneDrive/HackPSU/images/parka.jpg','DATA'),
			('images/longsleeve.jpg','/Users/Chris/Documents/OneDrive/HackPSU/images/longsleeve.jpg','DATA'),
			('images/fleece.png','/Users/Chris/Documents/OneDrive/HackPSU/images/fleece.png','DATA'),
			('images/tank.png','/Users/Chris/Documents/OneDrive/HackPSU/images/tank.png','DATA'),
			('images/Tshirt.png','/Users/Chris/Documents/OneDrive/HackPSU/images/Tshirt.png','DATA'),
			]   

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Accuwear',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='Accuwear.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
            	'NSHighResolutionCapable': 'True'
             },
            )
