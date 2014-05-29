#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


con = sqlite3.connect('db_tarea1.db')
c = con.cursor()
con.commit()
#funciones por construir donde se aplicaran las consultas
