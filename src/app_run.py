# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from warnings import warn_explicit
    from datetime import datetime
    import uvicorn

    warn_explicit(f"\nEDUCATION-server (uvicorn {uvicorn.__version__}) started at "
                  f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S, %A')}...",
                  category=UserWarning, filename='', lineno=-1)

    from config.app import cfg
    cfg = cfg.uvicorn

    uvicorn.run("app.app_init:app", host=cfg.host, port=cfg.port, log_level=cfg.log, workers=cfg.workers)
