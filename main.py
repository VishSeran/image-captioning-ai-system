import gradio as gr

def image_caption_process(image, user_query):
    
    try:
        
    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise
    
    except Exception as e:
        logger.error(f"user query fetch error: : {e}")
        raise 

def gradio_interface():
    
    
    image_input = gr.Image(label="Drag and drop the image or url",sources="upload",type="filepath")
    input_url = gr.Textbox(label="Type the image url", placeholder="Image url")
    user_query = gr.Textbox(label="User query", placeholder="Input your question here")
    text_output = gr.Textbox(label="Image caption")
    
    interface = gr.Interface(
        fn=
    )