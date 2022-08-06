# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# Adapted from example: https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/Makefile

# Makefile

# defaults
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

VHDL_SOURCES += ../src/*.vhd
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = and16
TESTCASE=tb_And16_simple

# MODULE is the basename of the Python test file
MODULE = tests

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

#Executar:
#make TOPLEVEL=and16 TESTCASE=tb_And16_simple