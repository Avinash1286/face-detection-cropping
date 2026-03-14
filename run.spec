# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['run.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 ('main/parameters.json', 'main'),
                 ('main/blaze_face_short_range.tflite', 'main'),
                 ('public/logo.png', 'public'),
             ],
             hiddenimports=['mediapipe'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='FaceCrop',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='public/logo.png')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='FaceCrop')
