

'''
import os

import numpy as np

import gradio as gr


def reverse_audio(audio):
    print("audio len=",len(audio))
    sr, data = audio
    return (sr, np.flipud(data))

x =  gr.Audio(source="microphone", streaming=True)
demo = gr.Interface(
    reverse_audio,
   x,
    gr.Audio(),
    interpretation="default",
)

x.stream(reverse_audio)


if __name__ == "__main__":
    demo.launch()
'''

import gradio as gr
# import numpy as np

# def reverse_audio(audio):
#     sr, data = audio
#     return (sr, np.flipud(data))

with gr.Blocks() as demo:
    audio = gr.Audio(source="microphone", streaming=True)
    # audio_output = gr.Audio()
    # audio.stream(fn=reverse_audio, inputs=audio, outputs=audio_output)

demo.launch()
