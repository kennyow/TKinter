def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetPRocessDpiAwareness(1)
    except:
        pass