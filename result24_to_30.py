import imageio
from tqdm import *
from PIL import Image
import numpy as np

writer_top = imageio.get_writer('result30_top.mp4', 'ffmpeg', fps=30)
writer_bottom = imageio.get_writer('result30_bottom.mp4', 'ffmpeg', fps=30)
reader = imageio.get_reader('result.mp4', 'ffmpeg')

for frame in trange(0, len(reader)):
    data = reader.get_data(frame)
    im = Image.fromarray(data)
    top = im.crop((0, 0, im.size[0], im.size[1] // 2))
    bottom = im.crop((0, im.size[1] // 2, im.size[0], im.size[1]))
    writer_top.append_data(np.array(top))
    writer_bottom.append_data(np.array(bottom))

writer_top.close()
writer_bottom.close()
reader.close()