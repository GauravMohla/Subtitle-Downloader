@echo off
cls
set PATH=%PATH%
:my_loop
IF %1=="" GOTO completed
  python **Set the location of python file. E:\....\subtitleDownloader.py** %1
:completed
