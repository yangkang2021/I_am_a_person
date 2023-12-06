'''
import gradio as gr

def snap(image, video):
    return [image, video]

demo = gr.Interface(
    snap,
    [gr.Image(source="webcam", tool=None, streaming=True), gr.Video(source="webcam", streaming=True)],
    ["image", "video"],
)

if __name__ == "__main__":
    demo.launch(share=True)

'''

# demo.live =True
# demo.interactive=True



import numpy as np
import gradio as gr
import tempfile

def flip(img):
    return img[:,::-1,:]

list = []
def reverse_audio(audiodata):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        gr.Audio.update(value=fp.name, visible=True)
        # return fp.name
    #
    # if(len(list) < 10) :
    #     print("audio_output.append",audiodata)
    #     list.append(audiodata)
    # else:
    #     list_temp = list.copy();
    #     list.clear()
    #     print("audio_output.update:",np.array(audiodata))
    #     audio_output.update(value = np.array(audiodata), visible=True)

with gr.Blocks() as demo:
    audio = gr.Audio(source="microphone", streaming=True, autoplay=True, interactive=True, max_batch_size=1024, batch=True, every=5)
    audio_output = gr.Audio(interactive=True)
    audio.stream(fn=reverse_audio, inputs=audio, outputs=None)

    # img = gr.Image(source="webcam", tool=None, streaming=True)
    # img_ouput = gr.Image()
    # img.stream(fn=flip, inputs=img, outputs=img_ouput)

demo.live =True
demo.interactive=True
demo.launch()