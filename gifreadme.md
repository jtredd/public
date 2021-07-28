## Example GIF
```
byte#  hexadecimal  text or
(hex)               value       Meaning
0:     47 49 46
       38 39 61     GIF89a      Header
                                Logical Screen Descriptor
6:     03 00        3            - logical screen width in pixels
8:     05 00        5            - logical screen height in pixels
A:     F7                        - GCT follows for 256 colors with resolution 3 × 8 bits/primary;
                                   the lowest 3 bits represent the bit depth minus 1, the highest true bit means that the GCT is present
B:     00           0            - background color #0
C:     00                        - default pixel aspect ratio
                   R    G    B  Global Color Table
D:     00 00 00    0    0    0   - color #0 black
10:    80 00 00  128    0    0   - color #1
 :                                       :
85:    00 00 00    0    0    0   - color #40 black
 :                                       :
30A:   FF FF FF  255  255  255   - color #255 white
30D:   21 F9                    Graphic Control Extension (comment fields precede this in most files)
30F:   04           4            - 4 bytes of GCE data follow
310:   01                        - there is a transparent background color (bit field; the lowest bit signifies transparency)
311:   00 00                     - delay for animation in hundredths of a second: not used
313:   10          16            - color #16 is transparent
314:   00                        - end of GCE block
315:   2C                       Image Descriptor
316:   00 00 00 00 (0,0)         - NW corner position of image in logical screen
31A:   03 00 05 00 (3,5)         - image width and height in pixels
31E:   00                        - no local color table
31F:   08           8           Start of image - LZW minimum code size
320:   0B          11            - 11 bytes of LZW encoded image data follow
321:   00 51 FC 1B 28 70 A0 C1 83 01 01
32C:   00                        - end of image data
32D:   3B                       GIF file terminator
```

## Animated
```
byte#  hexadecimal  text or
(hex)               value     Meaning
0:     47 49 46
       38 39 61     GIF89a    Header
                              Logical Screen Descriptor
6:     90 01        400        - width in pixels
8:     90 01        400        - height in pixels
A:     F7                      - GCT follows for 256 colors with resolution 3 x 8bits/primary
B:     00           0          - background color #0
C:     00                      - default pixel aspect ratio
D:                            Global Color Table
:
30D:   21 FF                  Application Extension block
30F:   0B           11         - eleven bytes of data follow
310:   4E 45 54
       53 43 41
       50 45        NETSCAPE   - 8-character application name
       32 2E 30     2.0        - application "authentication code"
31B:   03           3          - three more bytes of data
31C:   01           1          - data sub-block index (always 1)
31D:   FF FF        65535      - unsigned number of repetitions
31F:   00                      - end of App Extension block
320:   21 F9                  Graphic Control Extension for frame #1
322:   04           4          - four bytes of data follow
323:   08                      - bit-fields 3x:3:1:1, 000|010|0|0 -> Restore to bg color
324:   09 00                   - 0.09 sec delay before painting next frame
326:   00                      - no transparent color
327:   00                      - end of GCE block
328:   2C                     Image Descriptor
329:   00 00 00 00  (0,0)      - NW corner of frame at 0, 0
32D:   90 01 90 01  (400,400)  - Frame width and height: 400 × 400
331:   00                      - no local color table; no interlace
332:   08           8         LZW min code size
333:   FF           255       - 255 bytes of LZW encoded image data follow
334:                data
433:   FF           255       - 255 bytes of LZW encoded image data follow
                    data
                     :
92BA:  00                    - end of LZW data for this frame
92BB:  21 F9                 Graphic Control Extension for frame #2
 :                                                            :
153B7B:21 F9                 Graphic Control Extension for frame #44
 :
15CF35:3B                    File terminator
```



### COMPRESSED 9-bit codes 
from 3x5 image

*\x100* (CLR) **9-bit-codes *\x101* (STOP)
```
9-bit codes: 100 028 0FF 0FF 0FF 028 0FF 0FF 0FF 0FF 0FF 0FF 0FF 0FF 0FF 0FF 101
```

After the above codes are mapped to bytes, the uncompressed file differs from the compressed file thus:

```
 :
320: 14            20            20 bytes uncompressed image data follow
321: 00 51 FC FB F7 0F C5 BF 7F FF FE FD FB F7 EF DF BF 7F 01 01
335: 00                          - end
 :
 ```


