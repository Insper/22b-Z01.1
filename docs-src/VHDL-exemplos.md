# Exemplos completos

- http://esd.cs.ucr.edu/labs/tutorial/

- https://www.intel.com/content/www/us/en/programmable/support/support-resources/design-examples/design-software/vhdl.html

- http://ftp.smart-dv.com/examples/vhdl/index.html

## Combinacional

### `END`

```vhdl
library ieee;
use ieee.std_logic_1164.all;

--------------------------------------------------

entity AND_ent is
port( x: in std_logic;
      y: in std_logic;
      F: out std_logic
);
end AND_ent;

--------------------------------------------------

architecture behav2 of AND_ent is
begin

    F <= x and y;

end behav2;
```

> Exemplo extraído de: http://esd.cs.ucr.edu/labs/tutorial/

### mux

```vhdl
-------------------------------------------------------
-- Design Name : mux_using_when
-- File Name   : mux_using_assign.v
-- Function    : 2:1 Mux using when
-- Coder       : Deepak Kumar Tala
-------------------------------------------------------
library ieee;
    use ieee.std_logic_1164.all;

entity mux_using_when is
    port (
        din_0   :in  std_logic;-- Mux first input
        din_1   :in  std_logic;-- Mux Second input
        sel     :in  std_logic;-- Select input
        mux_out :out std_logic -- Mux output

    );
end entity;

architecture behavior of mux_using_when is

begin
    mux_out <= din_0 when (sel = '0') else
               din_1;
        
end architecture;
```

ou

```vhdl
 -------------------------------------------------------
 -- Design Name : mux_using_when
 -- File Name   : mux_using_assign.v
 -- Function    : 2:1 Mux using when
 -- Coder       : Deepak Kumar Tala
 -------------------------------------------------------
 library ieee;
     use ieee.std_logic_1164.all;
 
 entity mux_using_when is
     port (
         din_0   :in  std_logic;-- Mux first input
         din_1   :in  std_logic;-- Mux Second input
         sel     :in  std_logic;-- Select input
         mux_out :out std_logic -- Mux output
 
     );
 end entity;
 
 architecture behavior of mux_using_when is
 
 begin
     mux_out <= din_0 when (sel = '0') else
                din_1;
         
 end architecture;
```

> Exemplo extraído de: http://ftp.smart-dv.com/examples/vhdl/mux.html

### demux

- Saída sendo 4 sinais independentes:

```vhdl
library ieee;
    use ieee.std_logic_1164.all;

entity demux is
    port (
        din     :in  std_logic; -- Mux first input
        sel     :in  std_logic_vector(1 downto 0); -- Select output
        dout_0  :out std_logic; -- demux first out
        dout_1  :out std_logic; -- demux second out
        dout_2  :out std_logic; -- demux ...
        dout_3  :out std_logic  -- demux ...
    );
end entity;

architecture behavior of mux_using_when is

begin

    dout_0 <= din when sel = "00" else '0';
    dout_1 <= din when sel = "01" else '0';
    dout_2 <= din when sel = "10" else '0';
    dout_3 <= din when sel = "11" else '0';
        
end architecture;
```

- Saída sendo um vetor:

```vhdl
library ieee;
    use ieee.std_logic_1164.all;

entity demux is
    port (
        din     :in  std_logic; -- Mux first input
        sel     :in  std_logic_vector(1 downto 0); -- Select output
        dout    :out std_logic_vector(3 downto 0) -- demux out vector
    );
end entity;

architecture behavior of mux_using_when is

begin

    dout(0) <= din when sel = "00" else '0';
    dout(1) <= din when sel = "01" else '0';
    dout(2) <= din when sel = "10" else '0';
    dout(3) <= din when sel = "11" else '0';
        
end architecture;
```

### Enconder 

```vhdl
-------------------------------------------------------
-- Design Name : pri_encoder_using_when
-- File Name   : pri_encoder_using_when.vhd
-- Function    : Pri Encoder using when-else
-- Coder       : Deepak Kumar Tala (Verilog)
-- Translator  : Alexander H Pham (VHDL)
-- Fixed       : Tomasz Olszewski 
-------------------------------------------------------
library ieee;
    use ieee.std_logic_1164.all;

entity pri_encoder_using_when is
    port (
        enable     :in  std_logic;                     --  Enable for the encoder
        encoder_in :in  std_logic_vector (15 downto 0);--  16-bit Input
        binary_out :out std_logic_vector (3 downto 0)  --  4 bit binary Output

    );
end entity;

architecture behavior of pri_encoder_using_when is

begin
    binary_out <= "0000" when enable = '0' else
              "0001" when encoder_in( 1 ) = '1' else
              "0010" when encoder_in( 2 ) = '1' else
              "0011" when encoder_in( 3 ) = '1' else
              "0100" when encoder_in( 4 ) = '1' else
              "0101" when encoder_in( 5 ) = '1' else
              "0110" when encoder_in( 6 ) = '1' else
              "0111" when encoder_in( 7 ) = '1' else
              "1000" when encoder_in( 8 ) = '1' else
              "1001" when encoder_in( 9 ) = '1' else
              "1010" when encoder_in( 10 ) = '1' else
              "1011" when encoder_in( 11 ) = '1' else
              "1100" when encoder_in( 12 ) = '1' else
              "1101" when encoder_in( 13 ) = '1' else
              "1110" when encoder_in( 14 ) = '1' else
              "1111" when encoder_in( 15 ) = '1' else
              "0000"; 

end architecture;
```

> Exemplo extraído de: http://ftp.smart-dv.com/examples/vhdl/pri_encoder.html#Encoder_-_Using_when_Statement

### Paridade

```vhdl
-------------------------------------------------------
-- Design Name : parity_using_assign
-- File Name   : parity_using_assign.vhd
-- Function    : Parity using direct assignment
-- Coder       : Deepak Kumar Tala (Verilog)
-- Translator  : Alexander H Pham (VHDL)
-------------------------------------------------------
library ieee;
    use ieee.std_logic_1164.all;

entity parity_using_assign is
    port (
        data_in     :in  std_logic_vector (7 downto 0);
        parity_out  :out std_logic
    );
end entity;

architecture rtl of parity_using_assign is
    
begin

    parity_out <= (data_in(0) xor data_in(1)) xor
                  (data_in(2) xor data_in(3)) xor
                  (data_in(4) xor data_in(5)) xor
                  (data_in(6) xor data_in(7));
end architecture;
```

> Exemplo estraído de: http://ftp.smart-dv.com/examples/vhdl/parity.html#Using_Assign
