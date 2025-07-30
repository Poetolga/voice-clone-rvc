import gradio as gr

def dummy_clone(audio):
    # Здесь должна быть логика RVC, пока заглушка — просто возвращает то же аудио
    return audio

app = gr.Interface(
    fn=dummy_clone,
    inputs=gr.Audio(type="filepath", label="Загрузите аудиофайл"),
    outputs=gr.Audio(type="filepath", label="Готовый результат"),
    title="RVC Voice Clone",
    description="Голосовой клонер на основе RVC. Загрузите аудиофайл и получите результат."
)

app.launch(server_name="0.0.0.0", server_port=10000)
