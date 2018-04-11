###Tells user to input flash drive size in GB###
size_GB = float(input("Enter USB size (GB): "))
size = size_GB * (10**9) ###Size is measured in 'bytes'

###The next 4 lines of code are formats with the size of USB divided by the bytes of a format###
gif_size = int(size / 96000)
jpeg_size = int(size / 57600)
png_size = int(size / 18000)
tiff_size = int(size / 2880000)

###Will print user how many images can be stored###
print(gif_size,"images in GIF format can be stored")
print(jpeg_size,"images in JPEG format can be stored")
print(png_size,"images in PNG format can be stored")
print(tiff_size,"images in TIFF format can be stored")