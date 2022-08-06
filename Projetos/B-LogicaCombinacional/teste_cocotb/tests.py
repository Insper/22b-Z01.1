# Adapted from https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/test_my_design.py

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_Nand2(dut):

    inA =   [0, 1, 0, 1]
    inB =   [0, 0, 1, 1]
    outq =  [1, 1, 1, 0]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")
        
        
@cocotb.test()
async def tb_And16(dut):

    inA = [0b1111000011110000, 0b1010101010101010, 0b0101010101010101, 0b0000000000000000, 0b0000000000000000, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    inB = [0b0000111100001111, 0b0000000000000000, 0b0000000000000000, 0b1010101010101010, 0b0101010101010101, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    outq =[0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Or16(dut):

    inA = [0b1111000011110000, 0b1010101010101010, 0b0101010101010101, 0b0101010101010101, 0b0000000000000000, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    inB = [0b0000111100001111, 0b0000000000000000, 0b0000000000000000, 0b1010101010101010, 0b0000000000000000, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    outq =[0b1111111111111111, 0b1010101010101010, 0b0101010101010101, 0b1111111111111111, 0b0000000000000000, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Not16(dut):

    inA = [0b1111000011110000, 0b1010101010101010, 0b1111111111111111, 0b0000000000000000]
    outq =[0b0000111100001111, 0b0101010101010101, 0b0000000000000000, 0b1111111111111111]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Or8Way(dut):

    inA =   [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    inB =   [0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
    inC =   [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
    inD =   [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    inE =   [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    inF =   [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    inG =   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    inH =   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    outq =  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.c.value = inC[i]
        dut.d.value = inD[i]
        dut.e.value = inE[i]
        dut.f.value = inF[i]
        dut.g.value = inG[i]
        dut.h.value = inH[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Nor8Way(dut):

    inA =   [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    inB =   [0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
    inC =   [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
    inD =   [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    inE =   [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    inF =   [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    inG =   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    inH =   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    outq =  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.c.value = inC[i]
        dut.d.value = inD[i]
        dut.e.value = inE[i]
        dut.f.value = inF[i]
        dut.g.value = inG[i]
        dut.h.value = inH[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_BarrelShifter16(dut):

    inA = [0b0000000000000010, 0b0000000000000010, 0b0000000000000010, 0b0000000000000010, 0b0000000000000010, 0b0100000000000000, 0b0100000000000000, 0b0100000000000000, 0b0100000000000000, 0b0100000000000000]
    inDir = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    inSize = [0b000, 0b001, 0b010, 0b011, 0b100, 0b000, 0b001, 0b010, 0b011, 0b100]
    outq =[0b0000000000000010, 0b0000000000000100, 0b0000000000001000, 0b0000000000010000, 0b0000000000100000, 0b0100000000000000, 0b0010000000000000, 0b0001000000000000, 0b0000100000000000, 0b0000010000000000]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.dir.value = inDir[i]
        dut.size.value = inSize[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_DMux2Way(dut):

    inA =   [1, 1, 0, 0]
    inSel = [0, 1, 0, 1]
    outq0 = [1, 0, 0, 0]
    outq1 = [0, 1, 0, 0]

    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q0.value == outq0[i] and dut.q1.value == outq1[i])
        if not condition:
            if not (dut.q0.value == outq0[i]):
                dut._log.error("Expected value q0: " + "{0:b}".format(outq0[i]) + " Obtained value q0: " + str(dut.q0.value) )
            if not (dut.q1.value == outq1[i]):
                dut._log.error("Expected value q1: " + "{0:b}".format(outq1[i]) + " Obtained value q1: " + str(dut.q1.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_DMux4Way(dut):

    inA =   [1, 1, 1, 1, 0, 0, 0, 0]
    inSel = [0b00, 0b01, 0b10, 0b11, 0b00, 0b01, 0b10, 0b11]
    outq0 = [1, 0, 0, 0, 0, 0, 0, 0]
    outq1 = [0, 1, 0, 0, 0, 0, 0, 0]
    outq2 = [0, 0, 1, 0, 0, 0, 0, 0]
    outq3 = [0, 0, 0, 1, 0, 0, 0, 0]

    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q0.value == outq0[i] and dut.q1.value == outq1[i] and dut.q2.value == outq2[i] and dut.q3.value == outq3[i])
        if not condition:
            if not (dut.q0.value == outq0[i]):
                dut._log.error("Expected value q0: " + "{0:b}".format(outq0[i]) + " Obtained value q0: " + str(dut.q0.value) )
            if not (dut.q1.value == outq1[i]):
                dut._log.error("Expected value q1: " + "{0:b}".format(outq1[i]) + " Obtained value q1: " + str(dut.q1.value) )
            if not (dut.q2.value == outq2[i]):
                dut._log.error("Expected value q2: " + "{0:b}".format(outq2[i]) + " Obtained value q2: " + str(dut.q2.value) )
            if not (dut.q3.value == outq3[i]):
                dut._log.error("Expected value q3: " + "{0:b}".format(outq3[i]) + " Obtained value q3: " + str(dut.q3.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_DMux8Way(dut):

    inA =   [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    inSel = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111, 0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
    outq0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outq1 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outq2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outq3 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outq4 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outq5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outq6 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outq7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q0.value == outq0[i] and dut.q1.value == outq1[i] and dut.q2.value == outq2[i] and dut.q3.value == outq3[i] and
                     dut.q4.value == outq4[i] and dut.q5.value == outq5[i] and dut.q6.value == outq6[i] and dut.q7.value == outq7[i]) 
        if not condition:
            if not (dut.q0.value == outq0[i]):
                dut._log.error("Expected value q0: " + "{0:b}".format(outq0[i]) + " Obtained value q0: " + str(dut.q0.value) )
            if not (dut.q1.value == outq1[i]):
                dut._log.error("Expected value q1: " + "{0:b}".format(outq1[i]) + " Obtained value q1: " + str(dut.q1.value) )
            if not (dut.q2.value == outq2[i]):
                dut._log.error("Expected value q2: " + "{0:b}".format(outq2[i]) + " Obtained value q2: " + str(dut.q2.value) )
            if not (dut.q3.value == outq3[i]):
                dut._log.error("Expected value q3: " + "{0:b}".format(outq3[i]) + " Obtained value q3: " + str(dut.q3.value) )
            if not (dut.q4.value == outq4[i]):
                dut._log.error("Expected value q4: " + "{0:b}".format(outq4[i]) + " Obtained value q4: " + str(dut.q4.value) )
            if not (dut.q5.value == outq5[i]):
                dut._log.error("Expected value q5: " + "{0:b}".format(outq5[i]) + " Obtained value q5: " + str(dut.q5.value) )
            if not (dut.q6.value == outq6[i]):
                dut._log.error("Expected value q6: " + "{0:b}".format(outq6[i]) + " Obtained value q6: " + str(dut.q6.value) )
            if not (dut.q7.value == outq7[i]):
                dut._log.error("Expected value q7: " + "{0:b}".format(outq7[i]) + " Obtained value q7: " + str(dut.q7.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Mux2Way(dut):

    inA =   [0, 1, 1, 0]
    inB =   [1, 0, 0, 1]
    inSel = [0, 0, 1, 1]
    outq =  [0, 1, 0, 1]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Mux4Way(dut):

    inA =   [1, 1, 1, 1, 0, 0, 0, 0]
    inB =   [0, 0, 0, 0, 1, 1, 1, 1]
    inC =   [1, 1, 1, 1, 0, 0, 0, 0]
    inD =   [0, 0, 0, 0, 1, 1, 1, 1]
    inSel = [0b00, 0b01, 0b10, 0b11, 0b00, 0b01, 0b10, 0b11]
    outq =  [1, 0, 1, 0, 0, 1, 0, 1]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.c.value = inC[i]
        dut.d.value = inD[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Mux8Way(dut):

    inA =   [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    inB =   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    inC =   [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    inD =   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    inE =   [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    inF =   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    inG =   [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    inH =   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    inSel = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111, 0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
    outq =  [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.c.value = inC[i]
        dut.d.value = inD[i]
        dut.e.value = inE[i]
        dut.f.value = inF[i]
        dut.g.value = inG[i]
        dut.h.value = inH[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Mux16(dut):

    inA =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inB =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inSel = [0, 1, 1, 0]
    outq =  [0b1111000011110000, 0b1111000011110000, 0b0000000000000000, 0b0000000000000000]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Mux4Way16(dut):

    inA =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inB =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inC =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inD =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inSel = [0b00, 0b01, 0b10, 0b11, 0b11, 0b10]
    outq =  [0b1111000011110000, 0b1111000011110000, 0b1111000011110000, 0b1111000011110000, 0b0000000000000000, 0b0000000000000000]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.c.value = inC[i]
        dut.d.value = inD[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_Mux8Way16(dut):

    inA =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inB =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inC =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inD =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inE =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inF =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inG =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inH =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inSel = [0b000, 0b101, 0b110, 0b111, 0b111, 0b010]
    outq =  [0b1111000011110000, 0b1111000011110000, 0b1111000011110000, 0b1111000011110000, 0b0000000000000000, 0b0000000000000000]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.c.value = inC[i]
        dut.d.value = inD[i]
        dut.e.value = inE[i]
        dut.f.value = inF[i]
        dut.g.value = inG[i]
        dut.h.value = inH[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_detectorDeMoedas(dut):

    inq =       [0, 1, 0, 0]
    inD =       [0, 0, 1, 0]
    inN =       [0, 0, 0, 1]
    outcents =  [0b00000, 0b11001, 0b01010, 0b00101]


    for i in range(len(inq)):
        dut.q.value = inq[i]
        dut.D.value = inD[i]
        dut.N.value = inN[i]

        await Timer(1, units="ns")
        condition = (dut.cents.value == outcents[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:05b}".format(outcents[i]) + " Obtained value: " + str(dut.cents.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_circuito(dut):

    inA =   [0, 1, 1]
    inB =   [0, 1, 1]
    inC =   [0, 0, 1]
    outX =  [0, 1, 0]


    for i in range(len(inA)):
        dut.A.value = inA[i]
        dut.B.value = inB[i]
        dut.C.value = inC[i]

        await Timer(1, units="ns")
        condition = (dut.X.value == outX[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outX[i]) + " Obtained value: " + str(dut.X.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_impressora(dut):

    insw1 = [0, 1, 1, 0, 0, 0, 1]
    insw2 = [0, 0, 1, 1, 1, 0, 1]
    insw3 = [0, 0, 0, 0, 1, 1, 1]
    insw4 = [1, 1, 0, 0, 1, 0, 1]
    outx =  [1, 1, 1, 1, 0, 1, 0]


    for i in range(len(insw1)):
        dut.sw1.value = insw1[i]
        dut.sw2.value = insw2[i]
        dut.sw3.value = insw3[i]
        dut.sw4.value = insw4[i]

        await Timer(1, units="ns")
        condition = (dut.x.value == outx[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outx[i]) + " Obtained value: " + str(dut.x.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_sevenSeg(dut):

    inbcd =   [0b0000, 0b0011, 0b0111]
    outleds = [0b1000000, 0b0110000, 0b1111000]


    for i in range(len(inbcd)):
        dut.bcd.value = inbcd[i]

        await Timer(1, units="ns")
        condition = (dut.leds.value == outleds[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:07b}".format(outleds[i]) + " Obtained value: " + str(dut.leds.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_ConceitoB(dut):

    inSW =   [0b0000000000, 0b0000001111, 0b0011110000, 0b0111110000]
    outHEX0 = [0b1000000, 0b0001110, 0b1000000, 0b1000000]
    outHEX1 = [0b1000000, 0b1000000, 0b0001110, 0b0001110]
    outHEX2 = [0b1000000, 0b1000000, 0b1000000, 0b1111001]


    for i in range(len(inSW)):
        dut.SW.value = inSW[i]

        await Timer(1, units="ns")
        condition = (dut.HEX0.value == outHEX0[i] and dut.HEX1.value == outHEX1[i] and dut.HEX2.value == outHEX2[i])
        if not condition:
            if not (dut.HEX0.value == outHEX0[i]):
                dut._log.error("Expected value HEX0: " + "{0:07b}".format(outHEX0[i]) + " Obtained value HEX0: " + str(dut.HEX0.value) )
            if not (dut.HEX1.value == outHEX1[i]):
                dut._log.error("Expected value HEX1: " + "{0:07b}".format(outHEX1[i]) + " Obtained value HEX1: " + str(dut.HEX1.value) )
            if not (dut.HEX2.value == outHEX2[i]):
                dut._log.error("Expected value HEX2: " + "{0:07b}".format(outHEX2[i]) + " Obtained value HEX2: " + str(dut.HEX2.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_ConceitoA(dut):

    inSW =   [0b0000001010, 0b0000010110, 0b0101001101]
    outHEX0 = [0b1000000, 0b0100100, 0b0110000]
    outHEX1 = [0b1111001, 0b0100100, 0b0110000]
    outHEX2 = [0b1000000, 0b1000000, 0b0110000]


    for i in range(len(inSW)):
        dut.SW.value = inSW[i]

        await Timer(1, units="ns")
        condition = (dut.HEX0.value == outHEX0[i] and dut.HEX1.value == outHEX1[i] and dut.HEX2.value == outHEX2[i])
        if not condition:
            if not (dut.HEX0.value == outHEX0[i]):
                dut._log.error("Expected value HEX0: " + "{0:07b}".format(outHEX0[i]) + " Obtained value HEX0: " + str(dut.HEX0.value) )
            if not (dut.HEX1.value == outHEX1[i]):
                dut._log.error("Expected value HEX1: " + "{0:07b}".format(outHEX1[i]) + " Obtained value HEX1: " + str(dut.HEX1.value) )
            if not (dut.HEX2.value == outHEX2[i]):
                dut._log.error("Expected value HEX2: " + "{0:07b}".format(outHEX2[i]) + " Obtained value HEX2: " + str(dut.HEX2.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")