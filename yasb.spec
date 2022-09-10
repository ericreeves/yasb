# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src/main.py'],
             pathex=['../src'],
             datas=[('src/core', 'core')],
             binaries=[],
             hiddenimports=['json', 'psutil', 'pytz'],
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
          Tree('./src/core', prefix='core'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='yasb',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
