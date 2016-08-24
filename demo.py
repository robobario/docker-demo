#!/usr/bin/env python

import pty
import subprocess
import sys
import os
import time

with open(sys.argv[1],'rb') as f:


  def read(fd):
    return os.read(fd,1024)

  blocked = False

  def stdin(fd):
    global blocked
    data = os.read(fd, 1) 
    if blocked:
      if data.isspace():
        blocked = False
        return '\n'
      else:
        return " "
    c = f.read(1)
    if c == "\n":
      blocked = True
      return " "
    if c == "" or c == None:
      return data   
    return c

  pty.spawn('/bin/bash', read, stdin)
