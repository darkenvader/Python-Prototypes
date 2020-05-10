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
IntegrityCheck *file*
```
