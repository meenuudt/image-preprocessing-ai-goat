from PIL import Image, JpegImagePlugin
image = Image.new('RGB', (100, 100), color=(73, 109, 137))
metadata_comment = 'ls -l /home/ec2-user'
image.save('vulnerable_image.jpeg', "JPEG", quality=95, comment=metadata_comment)
