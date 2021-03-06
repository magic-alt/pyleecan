# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath

ROOT_DIR = normpath(abspath(join(dirname(__file__), "..")))
MAIN_DIR = dirname(realpath(__file__))

PACKAGE_NAME = MAIN_DIR[len(ROOT_DIR) + 1 :]  # To allow to change pyleecan directory

GEN_DIR = join(MAIN_DIR, "Generator")
DOC_DIR = join(GEN_DIR, "ClassesRef")  # Absolute path to classes reference dir
INT_DIR = join(GEN_DIR, "Internal")  # Absolute path to  internal classes ref. dir

GUI_DIR = join(MAIN_DIR, "GUI")
RES_PATH = join(GUI_DIR, "Resources")  # Default Resouces folder name
RES_NAME = "pyleecan.qrc"  # Default Resouces file name

DATA_DIR = join(MAIN_DIR, "Data")  # Absolute path to default data dir
MATLIB_DIR = join(DATA_DIR, "Material")

TEST_DIR = join(MAIN_DIR, "../Tests")
