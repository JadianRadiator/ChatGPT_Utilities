To prevent the command line terminal from opening when running the generated .exe file, you can use the `--noconsole` option with PyInstaller. Here's how you can modify the command:

```bash
pyinstaller --onefile --noconsole your_script.py
```

Adding `--noconsole` tells PyInstaller not to open a terminal window when running the executable. This is useful for GUI applications where you want to launch them without a command prompt window.

After running this command, check the `dist` directory for your generated .exe file, and it should run without opening a command prompt window.
