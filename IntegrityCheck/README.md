# IntegrityCheck

## Adding to path on windows

download pyinstaller
```
pip3 install pyinstaller
```

Create .exe from your script
```
pyinstaller -F IntegrityChecker
```

Now add the folder that the .exe is residing to the environment variables path.
Restart your cmd and test out the script
```
IntegrityCheck file
```

# IntrgrityCheck_v2
```
IntegrityCheck_v2.py -h
IntegrityCheck -f <filename>

Example: IntegrityCheck_v2.py -f app.exe --sha256 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
```
