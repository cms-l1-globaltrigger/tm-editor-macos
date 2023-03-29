import os
import tmTable
from tmEditor import __version__ as app_version

DIR = os.path.dirname(".")

block_cipher = None
app_name = "tm-editor"
bundle_name = "tm-editor.app"
entry_point = os.path.join(DIR, "app.py")
icon_filename = os.path.join(DIR, "assets", "tm-editor.icns")

xsd_filenames = [
    "algorithm.xsd",
    "bin.xsd",
    "scale_set.xsd",
    "cut.xsd",
    "menu.xsd",
    "ext_signal_set.xsd",
    "ext_signal.xsd",
    "object_requirement.xsd",
    "external_requirement.xsd",
    "scale.xsd",
    "xsd-type/complex-scale_set.xsd",
    "xsd-type/complex-object_requirement.xsd",
    "xsd-type/complex-menu.xsd",
    "xsd-type/complex-ext_signal.xsd",
    "xsd-type/complex-cut.xsd",
    "xsd-type/complex-bin.xsd",
    "xsd-type/complex-algorithm.xsd",
    "xsd-type/complex-external_requirement.xsd",
    "xsd-type/complex-scale.xsd",
    "xsd-type/complex-ext_signal_set.xsd",
    "xsd-type/simple-types.xsd",
]

datas = [(
    os.path.join(tmTable.UTM_XSD_DIR, filename),
    os.path.join("tmTable", "xsd", os.path.dirname(filename))
    ) for filename in xsd_filenames
]

a = Analysis(
    [entry_point],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "tmEditor",
        "tmTable",
        "tmGrammar",
        "PyQt5",
        "PyQt5.sip",
        "PyQt5.QtCore",
        "PyQt5.QtGui",
        "PyQt5.QtWidgets",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

exe = EXE(
    pyz,
    a.scripts,
    icon=icon_filename,
    exclude_binaries=True,
    name=app_name,
    debug=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name=app_name,
)

app = BUNDLE(
    coll,
    name=bundle_name,
    info_plist={
        "NSHighResolutionCapable": "True",
        "NSPrincipalClass": "NSApplication",
        "NSAppleScriptEnabled": "False"
    },
    icon=icon_filename,
    version=app_version,
    bundle_identifier=None,
)
