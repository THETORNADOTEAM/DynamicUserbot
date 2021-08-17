os.system("git clone https://github.com/Speedo-OP/Speedo_PLUGS.git ./")
    path = "*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_module(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    print ('INSTALLING ALL MODULES', plugin_name)
            except:
                pass
