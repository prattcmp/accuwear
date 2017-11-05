# -*- mode: python -*-

block_cipher = None


a = Analysis(['Coatmeter.py'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Coatmeter',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='Coatmeter.app',
             icon=None,
             bundle_identifier=None)
