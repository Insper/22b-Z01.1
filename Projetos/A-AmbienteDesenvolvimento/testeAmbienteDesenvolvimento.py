#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Curso de Elementos de Sistemas
# Desenvolvido por: Rafael Corsi <rafael.corsi@insper.edu.br>

import sys, subprocess, os
import json

FILE = ["GRUPO.json", "INTEGRANTES.json"]

erro = 0
for f in FILE:
    try:
        with open(os.path.dirname(sys.argv[0]) + '/../../' + f) as j:

            data = json.load(j)
            print("===================================================")
            print("[OK] {}".format(f))
            print("===================================================")

    except:
        print("===================================================")
        print("[FAIL] {}".format(f))
        print("===================================================")
        erro = 1

sys.exit(erro)


