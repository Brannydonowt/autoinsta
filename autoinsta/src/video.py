import ffmpeg
import sys
import utils

def init():
    # Add ffmpeg exe's to local path (windows only?)
    paths = [utils.abs_path('ffmpeg/ffmpeg.exe'), utils.abs_path('ffmpeg/ffplay.exe'), utils.abs_path('ffmpeg/ffprobe.exe')]

    for s in paths:
        print(s)
        sys.path.insert(0,s)

def get_video_resolution(video_path):
    probe = ffmpeg.probe(video_path)
    video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
    h = utils.get_json_value(video_streams[0], "height")
    w = utils.get_json_value(video_streams[0], "width")

    print("height", h)
    print("width", w)
    return w, h

def get_optimal_padding(w, h):
    pad_w = 0
    pad_h = 0
    if h > w:
        pad_w = h - w
    else:
        pad_h = w - h

    return pad_w, pad_h

def add_video_pad(video_path, padding_x, padding_y):
    utils.clean_log(f"Processing Video at path: {video_path}")

    input = ffmpeg.input(utils.abs_path(video_path))
    #Padding - 'pad=ih*4/3:ih:(ow-iw)/2:(oh-ih)/2:color=white'
    output = ffmpeg.output(input, utils.abs_path('autoinsta/videos/final.mp4'), vcodec='libx264', vf=f'pad=ih*4/3:ih:(ow-iw)/2:(oh-ih)/2:color=white')
    output.run(overwrite_output=True)
    return 'autoinsta/videos/final.mp4'