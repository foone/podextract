# podextract
 An extractor for POD archives from Terminal Reality games
 
 Known games using this format are:

 * Terminal Velocity (1995)
 * Fury3 (1995)
 * Hellbender (1996)
 * Monster Truck Madness (1996)

# Usage: 

Simply run:

``` python podextract.py PODNAME.pod "\*.MOD" ```

(Using python 2.7)

# File format details:
There's a 16-bit file count at offset 0, then entries start at 0x54

Each entry is 40 bytes long. The first 32 bytes are the filename(s), null-padded, and then the length and offset, as 32bit integers. 

The filenames sometimes have two filenames packed into them: there'll be a first name, then a NUL byte, then another filename. I have no idea why this is.
