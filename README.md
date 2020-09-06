# podextract
 An extractor for POD archives from Terminal Reality games
 
 Known games using this format are:

 * Terminal Velocity (1995)
 * Fury3 (1995)
 * Hellbender (1996)
 * Monster Truck Madness (1996)
 * CART Precision Racing (1997)
 * Monster Truck Madness 2 (1998)

Known games using the POD2/POD3 formats (which are NOT supported):

 * Nocturne (1999)
 * 4x4 Evo (2000)
 * BloodRayne (2002)

Known Terminal Reality games which do not use POD:

 * Fly! (1999)

# Usage: 

Simply run:

``` python podextract.py PODNAME.pod "*.MOD" ```

(Using python 2.7)

# File format details:
There's a 16-bit file count at offset 0, then entries start at 0x54

Each entry is 40 bytes long. The first 32 bytes are the filename(s), null-padded, and then the length and offset, as 32bit integers. 

The filenames sometimes have two filenames packed into them: there'll be a first name, then a NUL byte, then another filename. This second filename is believed to be the palette for that file, but this hasn't been confirmed. 
