import gradio as gr
import numpy as np


def greet(name):
    return "Hello " + name + "!"


def image(input_img):
    sepia_filter = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


demo = gr.Interface(image, gr.Image(shape=(200, 200)), "image")
demo.launch()

# demo = gr.Interface(
#    fn=greet, inputs="text", outputs="text", description="absoluty awesome!"
# )

demo.launch()
