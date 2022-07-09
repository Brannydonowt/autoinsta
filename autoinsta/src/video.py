import ffmpeg
import sys
import utils

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

def add_video_pad(video_path):
    utils.clean_log(f"Processing Video at path: {video_path}")

    input = ffmpeg.input(utils.abs_path(video_path))
    #Padding - 'pad=ih*4/3:ih:(ow-iw)/2:(oh-ih)/2:color=white'
    output = ffmpeg.output(input, utils.abs_path('autoinsta/videos/final.mp4'), vcodec='libx264', vf=f'pad=ih*4/3:ih:(ow-iw)/2:(oh-ih)/2:color=white')
    try:
        output.run(overwrite_output=True)
        return 'autoinsta/videos/final.mp4'
    except:
        utils.error_log("Failed to produce edited video")
        utils.clean_log("Ensure you have correctly installed ffmpeg and that it is included in your system path.")
        utils.clean_log("You can skip the video edit by setting VIDEO_EDIT to false in bot.py")
        utils.clean_log("Continuing with un-edited video.")
        return video_path